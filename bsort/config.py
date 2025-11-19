"""
Configuration models for the bsort application.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class DatasetConfig:
    train_dir: str
    val_dir: str


@dataclass
class TrainConfig:
    epochs: int
    batch: int
    imgsz: int
    learning_rate: float


@dataclass
class AppConfig:
    dataset: DatasetConfig
    training: TrainConfig
    model_path: str


def load_config(path: str) -> AppConfig:
    """Load YAML config into dataclasses."""
    import yaml

    with open(path, "r") as f:
        raw = yaml.safe_load(f)

    dataset = DatasetConfig(
        train_dir=raw["dataset"]["train_dir"],
        val_dir=raw["dataset"]["val_dir"],
    )

    training = TrainConfig(
        epochs=raw["training"]["epochs"],
        batch=raw["training"]["batch"],
        imgsz=raw["training"]["imgsz"],
        learning_rate=raw["training"]["learning_rate"],
    )

    return AppConfig(
        dataset=dataset,
        training=training,
        model_path=raw["model_path"],
    )
