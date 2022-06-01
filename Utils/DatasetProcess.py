import csv
import os
import random
from abc import ABC

import cv2
from paddle.vision import transforms as T
import numpy as np
import paddle


class Cutout(paddle.vision.transforms.BaseTransform, ABC):
    def __init__(self, n_holes=1, length=50, prob=0.5, keys=None):
        super(Cutout, self).__init__(keys)
        self.prob = prob
        self.n_holes = n_holes
        self.length = length

    def _get_params(self, inputs):
        var = inputs[self.keys.index('image')]
        params = {'cutout': np.random.random() < self.prob}
        return params

    def _apply_image(self, img):
        """ cutout_image """
        if self.params['cutout']:
            h, w = img.shape[:2]
            np.ones((h, w), np.float32)

            for n in range(self.n_holes):
                y = np.random.randint(h)
                x = np.random.randint(w)

                y1 = np.clip(y - self.length // 2, 0, h)
                y2 = np.clip(y + self.length // 2, 0, h)
                x1 = np.clip(x - self.length // 2, 0, w)
                x2 = np.clip(x + self.length // 2, 0, w)

                img[y1:y2, x1:x2] = 0

        return img


# 定义图像增强函数
transforms = T.Compose([T.Resize((224, 224)),
                        T.ColorJitter(0.3, 0.3, 0.3, 0.3),
                        # T.CenterCrop(224),
                        T.RandomHorizontalFlip(0.5),
                        T.RandomRotation(15),
                        Cutout(),
                        T.Transpose(),
                        # T.Normalize(mean=[127.5, 127.5, 127.5], std=[127.5, 127.5, 127.5], data_format='CHW',
                        # to_rgb=True),
                        ])


# transforms2 = T.Compose([T.Resize((224, 224)), T.Transpose(), ])


def get_image_paths_labels(data_dir):
    label = 0
    label_map = {}
    for i in os.listdir(data_dir):
        label_map[i] = label
        label = label + 1
    image_paths_labels = []

    for i in label_map:
        label_path = os.path.join(data_dir, i)
        for j in os.listdir(label_path):
            image_path = os.path.join(label_path, j)

            image_paths_labels.append([image_path, label_map[i]])

    random.seed(100)
    random.shuffle(image_paths_labels)
    return image_paths_labels, label_map


def load_data(data_dir, mode='train', train_set=80, batch_size=20):
    image_paths_labels, _ = get_image_paths_labels(data_dir)

    total_length = len(image_paths_labels)
    train_data = image_paths_labels[:int(train_set * 0.01 * total_length)]
    valid_data = image_paths_labels[int(train_set * 0.01 * total_length):]

    images = []
    image_labels = []

    if mode == 'train':
        # random.shuffle(train_data)
        for i in train_data:
            # for i in image_paths_labels:
            images.append(transforms(cv2.imread(i[0])))
            image_labels.append(i[1])

    else:
        for i in valid_data:
            # for i in image_paths_labels:
            image = cv2.imread(i[0])
            t = T.Compose([
                T.Resize((224, 224)),
                T.Transpose()
            ])
            images.append(t(image))
            image_labels.append(i[1])

    set_length = len(images)
    print(mode + '集数量:', set_length)

    def reader():
        batch_images = []
        batch_labels = []
        for i in range(len(images)):
            batch_images.append(images[i])
            batch_labels.append(image_labels[i])
            if len(batch_images) == batch_size:
                # 当数据列表的长度等于batch_size的时候，
                # 把这些数据当作一个mini-batch，并作为数据生成器的一个输出
                imgs_array = np.array(batch_images).astype('float32')
                labels_array = np.array(batch_labels).astype('int64').reshape(-1, 1)
                yield imgs_array, labels_array
                batch_images = []
                batch_labels = []

    return reader


def get_label_from_id(id):
    labels = []
    if 'D' in id:
        with open(os.path.abspath('Utils/dataset.csv'), 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if id in row:
                    dataset_path = row[3]
        for i in os.listdir(dataset_path):
            labels.append(i)
    elif 'T' in id:

        with open(os.path.abspath('Utils/train.csv'), 'r', encoding='utf-8') as f:

            reader = csv.reader(f)
            for row in reader:
                if id in row:
                    dataset_id = row[3]
            with open(os.path.abspath('Utils/dataset.csv'), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if dataset_id in row:
                        dataset_path = row[3]
            for i in os.listdir(dataset_path):
                labels.append(i)
    return labels


def get_path_by_id(id):
    if 'D' in id:
        with open(os.path.abspath('Utils/dataset.csv'), 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if id in row:
                    path = row[3]
    elif 'T' in id:
        with open(os.path.abspath('Utils/train.csv'), 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if id in row:
                    path = row[2]
    return path


if __name__ == "__main__":
    print(os.path.abspath('train.csv'))
