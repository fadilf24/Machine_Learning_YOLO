import wandb
from typing import Optional
from bsort.model import BottleSortModel
from bsort.config import AppConfig
import os


def run_training(config: AppConfig):
    """
    Run training pipeline using YOLO model.

    Args:
        config (AppConfig): Loaded config.
    """

    # Initialize wandb
    wandb.init(
        project="bottle-cap-detector",
        config={
            "epochs": config.train.epochs,
            "batch": config.train.batch,
            "learning_rate": config.train.learning_rate,
        },
    )

    model = BottleSortModel(config.train.model_name)

    data_yaml = "dataset.yaml"

    # create YOLO data file
    with open(data_yaml, "w") as f:
        f.write(
            f"""
path: .
train: {config.dataset.train_path}/images
val: {config.dataset.val_path}/images

names:
  0: dark_blue
  1: light_blue
  2: other
"""
        )

    print("🚀 Starting training ...")

    results = model.train(
        data_yaml=data_yaml,
        epochs=config.train.epochs,
        batch=config.train.batch,
        lr=config.train.learning_rate,
    )

    print("Training completed.")
    return results
