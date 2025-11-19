# bsort/config.py
from dataclasses import dataclass
from typing import Optional
import yaml

@dataclass
class DatasetConfig:
    train_dir: str
    val_dir: str

@dataclass
class TrainConfig:
    epochs: int
    batch: int
    imgsz: int = 640                     # DEFAULT ADDED
    learning_rate: float = 0.001         # DEFAULT ADDED

@dataclass
class AppConfig:
    dataset: DatasetConfig
    training: TrainConfig

def load_config(path: str) -> AppConfig:
    with open(path, "r") as f:
        raw = yaml.safe_load(f)

    dataset = DatasetConfig(
        train_dir=raw["dataset"]["train_dir"],
        val_dir=raw["dataset"]["val_dir"]
    )

    training_raw = raw.get("training", {})

    training = TrainConfig(
        epochs=training_raw.get("epochs", 10),
        batch=training_raw.get("batch", 4),
        imgsz=training_raw.get("imgsz", 640),                 # FIXED
        learning_rate=training_raw.get("learning_rate", training_raw.get("lr", 0.001)),  # FIXED
    )

    return AppConfig(dataset=dataset, training=training)
