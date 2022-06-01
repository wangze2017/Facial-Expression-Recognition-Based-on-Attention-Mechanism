import math
import paddle
from paddle import nn


class AttentionBlock(nn.Layer):
    def __init__(self, in_channel):
        super(AttentionBlock, self).__init__()
        self.channelAttention = ChannelAttention(in_channel)
        self.spatialAttention = SpatialAttention(in_channel)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.channelAttention(x)
        out = self.spatialAttention(out)
        out = x + out
        out = self.relu(out)
        return out


class ChannelAttention(nn.Layer):
    def __init__(self, in_channel, b=1, gamma=2):
        super(ChannelAttention, self).__init__()
        self.max_pool = nn.AdaptiveMaxPool2D(1)
        kernel_size = int(abs((math.log(in_channel, 2) + b) / gamma))
        kernel_size = kernel_size if kernel_size % 2 else kernel_size + 1

        self.conv = nn.Conv1D(1, 1, kernel_size, padding=((kernel_size - 1) // 2), bias_attr=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        n, c, _, _ = x.shape

        max_pool_out = paddle.reshape(self.max_pool(x), [n, 1, c])

        out = self.conv(max_pool_out)
        out = paddle.reshape(self.sigmoid(out), [n, c, 1, 1])

        return x * out


class SpatialAttention(nn.Layer):
    def __init__(self, in_channel):
        super(SpatialAttention, self).__init__()
        self.conv = nn.Conv2D(2, 1, kernel_size=3, stride=1, padding=1, bias_attr=False)

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        n, c, _, _ = x.shape

        max_pool_out = paddle.max(x, axis=1, keepdim=True)
        avg_pool_out = paddle.mean(x, axis=1, keepdim=True)
        pool_out = paddle.concat([max_pool_out, avg_pool_out], axis=1)
        out = self.conv(pool_out)
        out = self.sigmoid(out)
        return x * out


class BasicBlock(nn.Layer):
    expansion = 1

    def __init__(self,
                 in_channel,
                 out_channel,
                 stride=1,
                 down_sample=None,
                 dilation=1,
                 norm_layer=None):
        super(BasicBlock, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2D

        if dilation > 1:
            raise NotImplementedError(
                "Dilation > 1 not supported in BasicBlock")

        self.conv1 = nn.Conv2D(
            in_channel, out_channel, 3, padding=1, stride=stride, bias_attr=False)
        self.bn1 = norm_layer(out_channel)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2D(out_channel, out_channel, 3, padding=1, bias_attr=False)
        self.bn2 = norm_layer(out_channel)
        self.down_sample = down_sample
        self.stride = stride

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.down_sample is not None:
            identity = self.down_sample(x)

        out += identity
        out = self.relu(out)

        return out


class AttResNet(nn.Layer):
    def __init__(self, num_classes=7):
        super(AttResNet, self).__init__()
        layers = [3, 4, 6, 3]
        self.num_classes = num_classes
        self._norm_layer = nn.BatchNorm2D
        self.in_channel = 64
        self.dilation = 1
        self.soft_max = nn.Softmax()

        self.conv1 = nn.Conv2D(
            3,
            self.in_channel,
            kernel_size=7,
            stride=2,
            padding=3,
            bias_attr=False)
        self.bn1 = self._norm_layer(self.in_channel)
        self.relu = nn.ReLU()
        self.max_pool = nn.MaxPool2D(kernel_size=3, stride=2, padding=1)

        self.layer1 = self._make_layer(64, layers[0])
        self.layer2 = self._make_layer(128, layers[1], stride=2)
        self.layer3 = self._make_layer(256, layers[2], stride=2)
        self.layer4 = self._make_layer(512, layers[3], stride=2)
        self.avg_pool = nn.AdaptiveAvgPool2D((1, 1))
        self.fc = nn.Linear(512, num_classes)

    def _make_layer(self, out_channel, blocks, stride=1, dilate=False):
        norm_layer = self._norm_layer
        down_sample = None
        previous_dilation = self.dilation
        if dilate:
            self.dilation *= stride
            stride = 1

        if stride != 1 or self.in_channel != out_channel:
            down_sample = nn.Sequential(
                AttentionBlock(self.in_channel),
                nn.Conv2D(
                    self.in_channel,
                    out_channel,
                    1,
                    stride=stride,
                    bias_attr=False),
                norm_layer(out_channel)
            )

        layers = [BasicBlock(self.in_channel, out_channel, stride, down_sample, previous_dilation, norm_layer)]
        self.in_channel = out_channel
        for _ in range(1, blocks):
            layers.append(BasicBlock(self.in_channel, out_channel, norm_layer=norm_layer))

        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.max_pool(x)

        x = self.layer1(x)

        # x = self.attention_block1(x)
        x = self.layer2(x)

        # x = self.attention_block2(x)
        x = self.layer3(x)

        # x = self.attention_block3(x)
        x = self.layer4(x)

        # x = self.attention_block4(x)

        x = self.avg_pool(x)
        x = paddle.flatten(x, 1)
        x = self.fc(x)

        return x
