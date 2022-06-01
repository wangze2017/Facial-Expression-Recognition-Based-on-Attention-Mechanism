import os
import time
import paddle
import numpy as np
import paddle.nn.functional as F
import visualdl.server.app
from visualdl import LogWriter
from Utils import DatasetProcess


def train_model(model, data_dir, optimizer, train_set, batch_size, epoch_num, train_id, train_path):
    # 训练可视化
    start = time.time()

    with LogWriter(logdir="{}/Log/{}".format(train_path, train_id)) as writer:

        val_acc_history = []
        val_loss_history = []
        # 开启0号GPU训练
        use_gpu = True
        paddle.set_device('gpu:0') if use_gpu else paddle.set_device('cpu')
        print('start training ... ')

        model.train()
        # 定义数据读取器，训练数据读取器和验证数据读取器
        train_loader = DatasetProcess.load_data(data_dir, mode='train', train_set=train_set, batch_size=batch_size)

        valid_loader = DatasetProcess.load_data(data_dir, mode='valid', train_set=train_set, batch_size=batch_size)

        step = 0
        for epoch in range(epoch_num):

            print('epoch {}'.format(epoch))
            writer.add_hparams(hparams_dict={'lr': optimizer.get_lr(), 'bsize': batch_size, 'opt': 'Adam'},
                               metrics_list=['valid/accuracy', 'valid/loss'])

            for batch_id, data in enumerate(train_loader()):
                x_data, y_data = data
                x_data = paddle.to_tensor(x_data)
                y_data = paddle.to_tensor(y_data)

                # 获取Loss和Acc
                logits = model(x_data)
                train_loss = F.softmax_with_cross_entropy(logits, y_data)
                train_pred = F.softmax(logits)
                train_acc = paddle.metric.accuracy(train_pred, y_data)
                avg_train_loss = paddle.mean(train_loss)

                # 可视化Loss和Acc
                if batch_id % 10 == 0:
                    writer.add_scalar(tag="train/loss", step=step, value=avg_train_loss.numpy())
                    writer.add_scalar(tag="train/accuracy", step=step, value=train_acc.numpy())

                    step = step + 10

                    print("[train] step: {}, loss: {}, accuracy:{}".format(step, avg_train_loss.numpy(),
                                                                           train_acc.numpy()))

                # 反向传播，更新权重，清除梯度

                avg_train_loss.backward()
                optimizer.step()
                optimizer.clear_grad()

            writer.add_scalar(tag='train/lr', step=epoch, value=optimizer.get_lr())

            model.eval()
            accuracies = []
            losses = []
            for batch_id, data in enumerate(valid_loader()):
                x_data, y_data = data
                x_data = paddle.to_tensor(x_data)
                y_data = paddle.to_tensor(y_data)

                # 获取Loss和Acc
                logits = model(x_data)

                pred = F.softmax(logits)

                loss = F.softmax_with_cross_entropy(logits, y_data)

                acc = paddle.metric.accuracy(pred, y_data)

                accuracies.append(acc.numpy())
                losses.append(loss.numpy())
            avg_acc, avg_loss = np.mean(accuracies), np.mean(losses)

            writer.add_scalar(tag="valid/loss", step=epoch, value=avg_loss)
            writer.add_scalar(tag="valid/accuracy", step=epoch, value=avg_acc)

            print("[validation] accuracy/loss: {}/{}".format(avg_acc, avg_loss))
            val_acc_history.append(avg_acc)
            val_loss_history.append(avg_loss)
            model.train()
            last10epoch_acc = val_acc_history[-10:]
            std = np.std(last10epoch_acc)
            # if std < 0.005 and epoch > 10:
            # 这里我为了测试只训练5个Epoch
            if epoch > 4:
                input_spec = paddle.static.InputSpec([None, 3, 224, 224], 'float32', 'image')
                model = paddle.jit.to_static(model, input_spec=[input_spec])
                paddle.jit.save(model, '{}/Model/{}/{}'.format(train_path, train_id, epoch))

                print('训练自动停止，后十个迭代周期准确率的平均差为：{}，最佳迭代周期为：{}'.format(std, epoch))
                end = time.time()
                train_time = end - start
                train_info = [epoch, train_time, avg_acc]
                return train_info



