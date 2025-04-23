"""
######################## train lenet example ########################
train lenet and get network model files(.ckpt) :
python train.py --data_path /YourDataPath

python train.py --device_target CPU --data_path C:/Users/aku05/Downloads/ai_lab2/lenet/MNIST_Data --ckpt_path C:/Users/aku05/Downloads/ai_lab2/lenet/ckpt --dataset_sink_mode True
"""

import os
import ast
import argparse
from src.config import mnist_cfg as cfg
from src.dataset import create_dataset
from src.lenet import LeNet5
import mindspore.nn as nn
from mindspore import context
from mindspore.train.callback import (
    ModelCheckpoint,
    CheckpointConfig,
    LossMonitor,
    TimeMonitor,
)
from mindspore.train import Model
from mindspore.nn.metrics import Accuracy
from mindspore.common import set_seed

set_seed(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MindSpore Lenet Example")
    # 设备设置
    parser.add_argument(
        "--device_target",
        type=str,
        default="CPU",
        choices=["Ascend", "GPU", "CPU"],
        help="device where the code will be implemented (default: Ascend)",
    )
    parser.add_argument(
        "--data_path",
        type=str,
        default="C:/Users/aku05/Downloads/ai_lab2/lenet/MNIST_Data",
        help="path where the dataset is saved",
    )
    parser.add_argument(
        "--ckpt_path",
        type=str,
        default="C:/Users/aku05/Downloads/ai_lab2/lenet/ckpt",
        help="if is test, must provide\
                        path where the trained ckpt file",
    )
    parser.add_argument(
        "--dataset_sink_mode",
        type=ast.literal_eval,
        default=True,
        help="dataset_sink_mode is False or True",
    )

    args = parser.parse_args()

    context.set_context(mode=context.GRAPH_MODE, device_target=args.device_target)
    ds_train = create_dataset(os.path.join(args.data_path, "train"), cfg.batch_size)

    network = LeNet5(cfg.num_classes)
    # 设定loss函数
    """your code here"""
    loss = nn.SoftmaxCrossEntropyWithLogits(sparse=True, reduction="mean")
    # 设定优化器
    """your code here"""
    optimizer = nn.Momentum(
        network.trainable_params(), learning_rate=cfg.lr, momentum=cfg.momentum
    )
    time_cb = TimeMonitor(data_size=ds_train.get_dataset_size())
    config_ck = CheckpointConfig(
        save_checkpoint_steps=cfg.save_checkpoint_steps,
        keep_checkpoint_max=cfg.keep_checkpoint_max,
    )
    ckpoint_cb = ModelCheckpoint(
        prefix="checkpoint_lenet", directory=args.ckpt_path, config=config_ck
    )
    # 编译形成模型
    """your code here"""
    model = Model(
        network, loss_fn=loss, optimizer=optimizer, metrics={"Accuracy": Accuracy()}
    )

    print("============== Starting Training ==============")
    # 训练网络 train.py
    """your code here"""
    model.train(
        cfg.epoch_size,
        ds_train,
        callbacks=[time_cb, ckpoint_cb, LossMonitor()],
        dataset_sink_mode=args.dataset_sink_mode,
    )
