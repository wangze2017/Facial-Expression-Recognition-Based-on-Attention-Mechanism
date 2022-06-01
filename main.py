import csv
import re
import sys
import os
import cv2
import visualdl.server.app
from PySide6 import QtGui
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFileDialog)

from Pages.AddDatasetWidget import Ui_AddDatasetWidget
from Pages.AddTrainWidget import Ui_newTrain
from Pages.CreateDataset import Ui_CreateDataset
from Pages.Inference import Ui_Inference
from Pages.MainWindow import Ui_MainWindow
from Pages.NewDatasetWidget import Ui_NewDataset
from Pages.StartTrainWidget import Ui_Train
from Pages.TrainFinish import Ui_TrainFinish
from Utils import FaceDetection
from Utils import VisualTrain
from Utils.AttResNet import *
from Utils.DatasetProcess import get_label_from_id
from Utils.Predict import predict


class CreateDataset(QWidget, Ui_CreateDataset):
    def __init__(self):
        super(CreateDataset, self).__init__()
        self.pause = False
        self.current_label = None
        self.current_label_path = None
        self.start = False
        self.face_image = None
        self.camera_image = None
        self.camera = None
        self.image_count = 0
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.OpenCamera.clicked.connect(self.on_click_open_camera)
        self.InputLabel.clicked.connect(self.input_label)
        self.Start.clicked.connect(self.on_click_start)
        self.Pause.clicked.connect(self.on_click_pause)
        self.Continue.clicked.connect(self.on_click_continue)
        self.NextLabel.clicked.connect(self.on_click_next_label)
        self.Finish.clicked.connect(self.on_click_ok)

    def input_label(self):
        self.current_label = self.DatasetLabel.text()
        with open('./Utils/dataset.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ids = []
            for row in reader:
                ids.append(row)
            path = ids[-1][-1]
        self.current_label_path = path + '/{}'.format(self.current_label)
        os.mkdir(self.current_label_path)
        self.InputLabel.setDisabled(True)

    def on_click_open_camera(self):
        if self.camera is None:
            self.camera = cv2.VideoCapture(0)
            self.OpenCamera.setText('关闭摄像头')
            while True:
                ret, self.camera_image = self.camera.read()
                cv2.waitKey(int(1000 / 60))
                try:
                    label_show(label=self.VideoCapture, image=self.camera_image)
                    self.face_image = FaceDetection.get_face_image(self.camera_image)
                    label_show(self.ShowFaceImage, self.face_image)
                    if self.start:
                        self.image_count = self.image_count + 1
                        if self.image_count % 10 == 0:
                            print(r'{}/{}.png'.format(self.current_label_path, self.image_count / 10))
                            cv2.imwrite(r'{}/{}.png'.format(self.current_label_path, int(self.image_count / 10)),
                                        self.face_image)
                            self.ImageCount.setText(str(int(self.image_count / 10)))
                except:
                    pass

        else:
            self.camera.release()
            self.camera = None
            self.VideoCapture.setPixmap(QPixmap(u":/emoji/Pages/assets/emoji/1.png"))
            self.OpenCamera.setText('打开摄像头')

    def on_click_start(self):
        self.start = True
        self.Pause.setEnabled(True)
        self.Start.setDisabled(True)

    def on_click_pause(self):
        self.start = False
        self.Continue.setEnabled(True)
        self.Pause.setDisabled(True)

    def on_click_continue(self):
        self.start = True
        self.Continue.setDisabled(True)
        self.Pause.setEnabled(True)

    def on_click_next_label(self):
        self.Start.setEnabled(True)
        self.Pause.setDisabled(True)
        self.Continue.setDisabled(True)
        self.start = False
        self.pause = False
        self.DatasetLabel.setEnabled(True)
        self.InputLabel.setEnabled(True)
        self.DatasetLabel.clear()
        self.image_count = 0

    def on_click_ok(self):
        self.close()
        self.camera.release()


class Inference(QWidget, Ui_Inference):
    def __init__(self):
        super(Inference, self).__init__()
        self.camera = None
        self.labels = None
        self.model_path = None
        self.setupUi(self)
        self.init_ui()
        self.click_times = 0
        self.start_camera = False
        self.image_path = None
        self.train_id = None
        self.face_image = None

    def init_ui(self):
        self.SelectInferenceModel.clicked.connect(self.on_click_select_inference_model)
        self.Start.clicked.connect(self.on_click_start_image)
        self.OpenCamera.clicked.connect(self.on_click_open_camera)
        self.Start_2.clicked.connect(self.on_click_start_camera)

    def on_click_select_inference_model(self):
        self.train_id = self.InferenceModels.currentText()
        self.model_path = r'Models/40/40'
        # '{}/Model/{}/InferenceModel/{}'.format(get_path_by_id(self.train_id),
        #                                        self.train_id,
        #                                        self.train_id)

        # 这里使用之前的模型不是刚刚训练的模型
        self.labels = get_label_from_id(self.train_id)
        self.labels = ['sadness',
                       'anger',
                       'fear',
                       'happy',
                       'disgust',
                       'surprise',
                       'contempt']

    #     这里Labels注意要一致

    def on_click_start_image(self):

        if self.click_times == 0:
            self.train_id = self.InferenceModels.currentText()
            self.CurrentImage.clear()
            image_path, image_type = QFileDialog.getOpenFileName(self, '打开图片', r'./', '图片 (*.png *.jpg *.jpeg)')
            self.image_path = image_path
            self.CurrentImage.setText(image_path)
            cv2_image = cv2.imread(image_path)
            label_show(self.ShowSelectedImage, cv2_image)
            self.Start.setText('截取面部区域')
            self.click_times = self.click_times + 1
        elif self.click_times == 1:
            self.face_image = FaceDetection.get_face_image(
                cv2.imread(self.image_path))
            self.Start.setText('预测')
            label_show(self.ShowFaceImage, self.face_image)
            self.click_times = self.click_times + 1
        elif self.click_times == 2:
            self.ResultEmotion.setText('预测中....')
            result, _ = predict(model_path=self.model_path,
                                image=self.face_image,
                                labels=self.labels)
            self.ResultEmotion.setText(result)
            self.ShowEmoji.setPixmap(
                QPixmap(u":/emoji/Pages/assets/emoji/{}.png".format(result)))
            self.Start.setText('预测完成')

            self.click_times = self.click_times + 1
        else:
            self.click_times = 0
            self.Start.setText('读取图片')

    def on_click_open_camera(self):
        if self.camera is None:
            self.camera = cv2.VideoCapture(0)
            self.OpenCamera.setText('关闭摄像头')
            while True:
                ret, camera_image = self.camera.read()
                cv2.waitKey(int(1000 / 60))
                try:
                    label_show(label=self.VideoCapture, image=camera_image)
                    if self.start_camera:
                        self.face_image = FaceDetection.get_face_image(camera_image)
                        label_show(self.ShowFaceImage_2, self.face_image)
                        result, _ = predict(model_path=self.model_path,
                                            image=self.face_image,
                                            labels=self.labels)
                        print(result)
                        self.ResultEmotion_2.setText(result)
                        self.ShowEmoji_2.setPixmap(
                            QPixmap(u":/emoji/Pages/assets/emoji/{}.png".format(result)))
                except:
                    pass

        else:
            self.camera.release()
            self.camera = None
            self.VideoCapture.setPixmap(QPixmap(u":/emoji/Pages/assets/emoji/1.png"))
            self.OpenCamera.setText('打开摄像头')

    def on_click_start_camera(self):
        if not self.start_camera:
            self.start_camera = True
            self.Start_2.setText('停止识别')
            self.ResultEmotion_2.setText('请稍后')
        else:
            self.start_camera = False


class TrainFinish(QWidget, Ui_TrainFinish):
    def __init__(self):
        super(TrainFinish, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        pass


class StartTrainWidget(QWidget, Ui_Train):
    def __init__(self):
        super(StartTrainWidget, self).__init__()
        self.train_param = None
        self.train_info = None
        self.train_id = None
        self.train_path = None
        self.model = None
        self.dataset_path = None
        self.current_train_id = None
        self.setupUi(self)
        self.init_ui()
        self.train_finish_window = TrainFinish()

    def init_ui(self):
        self.VisualTrain.clicked.connect(self.visual_train)

    def visual_train(self):

        self.current_train_id = self.SelectTrainID.currentText()
        with open('./Utils/train.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for _, rows in enumerate(reader):
                if self.current_train_id in rows:
                    self.train_param = rows
                    break
        with open('./Utils/dataset.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for _, rows in enumerate(reader):
                if self.train_param[3] in rows:
                    self.dataset_path = rows[3]
                    break
        if self.train_param[6] == '方法二':
            self.model = AttResNet()
        self.train_path = self.train_param[2]
        self.train_id = self.train_param[0]
        opt = paddle.optimizer.Adam(learning_rate=float(self.train_param[8]), parameters=self.model.parameters(),
                                    grad_clip=paddle.nn.ClipGradByGlobalNorm(clip_norm=1.0))
        visualdl.server.app.run(logdir='{}/Log/{}'.format(self.train_path, self.train_id))
        # os.system(r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" 127.0.0.1:8040')

        self.train_info = VisualTrain.train_model(model=self.model,
                                                  data_dir=self.dataset_path,
                                                  optimizer=opt,
                                                  train_set=int(self.train_param[4]),
                                                  batch_size=int(self.train_param[9]),
                                                  epoch_num=int(self.train_param[7]),
                                                  train_id=self.train_id,
                                                  train_path=self.train_path)

        self.train_info.append(self.train_path)
        self.close()
        self.train_finish_window.show()
        self.train_finish_window.TrainEpoch.setText(str(self.train_info[0]))
        self.train_finish_window.TrainTime.setText(str(self.train_info[1]) + 's')
        self.train_finish_window.ValidAcc.setText(str(self.train_info[2]))
        self.train_finish_window.ModelSavePath.setText('{}/Model/{}'.format(self.train_path, self.train_id))


class AddDatasetWidget(QWidget, Ui_AddDatasetWidget):
    def __init__(self):
        super(AddDatasetWidget, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.findPath.clicked.connect(self.on_click_find_path)
        self.DatasetOK.clicked.connect(self.on_click_add_dataset)

    def on_click_find_path(self):
        self.datasetPath.clear()
        dataset_path = QFileDialog.getExistingDirectory()
        self.datasetPath.setText(dataset_path)

    def on_click_add_dataset(self):
        dataset_id = self.DatasetID.text()
        dataset_name = self.DatasetName.text()
        dataset_description = self.DatasetDescription.toPlainText()
        dataset_path = self.datasetPath.text()
        with open('./Utils/dataset.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([dataset_id, dataset_name, dataset_description, dataset_path])
        self.close()


class NewDataset(QWidget, Ui_NewDataset):
    def __init__(self):
        super(NewDataset, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.create_dataset_window = CreateDataset()

    def init_ui(self):
        self.savePath.clicked.connect(self.save_path)
        self.DatasetOK.clicked.connect(self.on_click_add_dataset)

    def save_path(self):
        self.datasetPath.clear()
        dataset_path = QFileDialog.getExistingDirectory()
        self.datasetPath.setText(dataset_path)

    def on_click_add_dataset(self):
        dataset_id = self.DatasetID.text()
        dataset_name = self.DatasetName.text()
        dataset_description = self.DatasetDescription.toPlainText()
        dataset_path = self.datasetPath.text() + '/{}'.format(dataset_name)
        os.mkdir(dataset_path)

        with open('./Utils/dataset.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([dataset_id, dataset_name, dataset_description, dataset_path])
        self.close()
        self.create_dataset_window.show()


class AddTrainWidget(QWidget, Ui_newTrain):
    def __init__(self):
        super(AddTrainWidget, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.TrainOK.clicked.connect(self.on_click_add_train)
        self.SelectPath.clicked.connect(self.on_click_select_path)

    def on_click_add_train(self):
        train_id = self.TrainID.text()
        train_name = self.TrainName.text()
        train_path = self.TrainPath.text()
        dataset = self.SelectDataset.currentText()
        model = self.SelectModel.currentText()
        train_set = self.TrainSet.text()
        valid_set = self.ValidSet.text()
        epoch = self.Epoch.text()
        learning_rate = self.LearningRate.text()
        batch_size = self.BatchSize.text()
        bright = self.BrightOn.isChecked()
        flip = self.flipOn.isChecked()
        contrast = self.contrastOn.isChecked()
        rotate = self.rotateOn.isChecked()
        saturation = self.saturationOn.isChecked()
        shelter = self.shelterOn.isChecked()
        with open('./Utils/train.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(
                [train_id, train_name, train_path, dataset, train_set, valid_set, model, epoch, learning_rate,
                 batch_size, bright, rotate, contrast, saturation, flip, shelter])
        self.close()

    def on_click_select_path(self):
        self.TrainPath.clear()
        train_path = QFileDialog.getExistingDirectory()
        self.TrainPath.setText(train_path)


def label_show(label, image):
    qt_img_buf = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    qt_img = QtGui.QImage(qt_img_buf.data, qt_img_buf.shape[1], qt_img_buf.shape[0], QtGui.QImage.Format_RGB32)
    image = QPixmap.fromImage(qt_img).scaled(label.width(), label.height())
    label.setPixmap(image)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.add_dataset_window = AddDatasetWidget()
        self.new_dataset_setting = NewDataset()
        self.add_train_window = AddTrainWidget()
        self.start_train_window = StartTrainWidget()
        self.train_finish_window = TrainFinish()
        self.inference_window = Inference()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ActionNewTrain.triggered.connect(self.new_train)
        self.ActionLoadDataset.triggered.connect(self.load_dataset)
        self.ActionStartTrain.triggered.connect(self.start_train)
        self.ActionStartInference.triggered.connect(self.start_inference)
        self.ActionNewDataset.triggered.connect(self.new_dataset)

    def new_dataset(self):
        self.new_dataset_setting.show()
        current_id = self.new_dataset_setting.DatasetID.text()
        with open('./Utils/dataset.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ids = []
            for row in reader:
                ids.append(row[0])

        if current_id in ids:
            d = re.sub(r'\D', '', ids[-1])
            d = int(d) + 1
            current_id = 'D' + str(d)
            self.new_dataset_setting.DatasetID.setText(current_id)

    def start_train(self):
        self.start_train_window.show()
        with open('./Utils/train.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ids = []
            for row in reader:
                ids.append(row[0])
        self.start_train_window.SelectTrainID.addItems(ids[1:])

    def start_inference(self):
        self.inference_window.show()
        with open('./Utils/train.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ids = []
            for row in reader:
                ids.append(row[0])
        self.inference_window.InferenceModels.addItems(ids[1:])

    def new_train(self):
        self.add_train_window.show()
        current_id = self.add_train_window.TrainID.text()
        with open('./Utils/train.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ids = []
            for row in reader:
                ids.append(row[0])

        if current_id in ids:
            d = re.sub(r'\D', '', ids[-1])
            d = int(d) + 1
            current_id = 'T' + str(d)
            self.add_train_window.TrainID.setText(current_id)

        with open('./Utils/dataset.csv', mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ids = []
            for row in reader:
                ids.append(row[0])
        self.add_train_window.SelectDataset.addItems(ids[1:])

    def load_dataset(self):
        self.add_dataset_window.show()
        current_id = self.add_dataset_window.DatasetID.text()
        with open('./Utils/dataset.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ids = []
            for row in reader:
                ids.append(row[0])

        if current_id in ids:
            d = re.sub(r'\D', '', ids[-1])
            d = int(d) + 1
            current_id = 'D' + str(d)
            self.add_dataset_window.DatasetID.setText(current_id)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()

    MainWindow.show()
    sys.exit(app.exec())
