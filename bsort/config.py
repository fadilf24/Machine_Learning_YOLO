import yaml
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class DatasetConfig:
    train_path: str
    val_path: str


@dataclass
class TrainConfig:
    epochs: int
    batch: int
    learning_rate: float
    model_name: str


@dataclass
class AppConfig:
    dataset: DatasetConfig
    train: TrainConfig


def load_config(path: str) -> AppConfig:
    """
    Load YAML configuration into dataclass.

    Args:
        path (str): Path to YAML config file.

    Returns:
        AppConfig: Parsed configuration.
    """
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)

    return AppConfig(
        dataset=DatasetConfig(**cfg["dataset"]),
        train=TrainConfig(**cfg["train"]),
    )
