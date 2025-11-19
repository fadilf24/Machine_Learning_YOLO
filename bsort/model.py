# bsort/model.py
import os
from typing import Dict, Any
from ultralytics import YOLO

def train_model(config: Dict[str, Any]):
    """Training dummy model - adapted to what's expected from tests."""

    dataset = config.get("dataset", {})
    train_dir = dataset.get("train_dir")
    val_dir = dataset.get("val_dir")

    training = config.get("training", {})
    epochs = training.get("epochs", 10)
    batch = training.get("batch", 4)
    lr = training.get("lr", training.get("learning_rate", 0.001))

    # Mock-compatible output
    model = YOLO("yolov8n.pt")
    result = model.train(
        data={"train": train_dir, "val": val_dir},
        epochs=epochs,
        batch=batch,
        lr=lr,
    )

    return result

def infer_image(config: Dict[str, Any], image_path: str):
    """Inference wrapper compatible with tests."""

    model_path = config["model"]["weights"]      # FIXED

    model = YOLO(model_path)
    results = model.predict(image_path)

    return results
