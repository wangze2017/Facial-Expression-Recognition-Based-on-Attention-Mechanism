import os
import cv2
import numpy as np
import paddle
from ppqi import InferenceModel
import paddle.nn.functional as F


def predict(model_path, image, labels):

    image = cv2.resize(image, (224, 224),
                       cv2.INTER_NEAREST)
    image = np.swapaxes(image, 1, 2)
    image = np.swapaxes(image, 1, 0)
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    model = InferenceModel(model_path, use_gpu=True, gpu_id=0)
    model.eval()

    x = [image]
    x = np.array(x).astype('float32')
    x = paddle.to_tensor(x)
    y = model(x)
    y = F.softmax(paddle.to_tensor(y)).flatten().tolist()
    result = labels[y.index(max(y))]
    prediction = dict(zip(labels, y))
    print(result, prediction)

    return result, prediction


