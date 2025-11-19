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

def load_config(path: str):
    with open(path, "r") as f:
        raw = yaml.safe_load(f)

    dataset_raw = raw.get("dataset", {})
    training_raw = raw.get("training", {})

    return {
        "dataset": {
            "train_dir": dataset_raw.get("train_dir"),
            "val_dir": dataset_raw.get("val_dir"),
        },
        "training": {
            "epochs": training_raw.get("epochs", 10),
            "batch": training_raw.get("batch", 4),
            "imgsz": training_raw.get("imgsz", 640),
            "learning_rate": training_raw.get("learning_rate", training_raw.get("lr", 0.001)),
        },
    }
    
    return {
        "dataset": {
            "train_dir": dataset.train_dir,
            "val_dir": dataset.val_dir,
        },
        "training": {
            "epochs": training_epochs,
            "batch": training.batch,
            "imgsz": training.imgsz,
            "learning_rate": training.learning_rate,
        }
    }

