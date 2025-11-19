"""
Model utilities for training and inference.
"""

from __future__ import annotations
from ultralytics import YOLO
from typing import Dict, Any


def train_model(config: Dict[str, Any]) -> str:
    """
    Train YOLO model using the provided configuration.

    Args:
        config (Dict[str, Any]): Configuration dictionary.

    Returns:
        str: Path to the trained model weights.
    """
    model = YOLO("yolov8n.pt")

    results = model.train(
        data=config["dataset_path"],
        epochs=config["training"]["epochs"],
        imgsz=config["training"]["imgsz"],
        batch=config["training"]["batch"],
        lr0=config["training"]["learning_rate"],
        project="runs/train",
        name="bsort_model",
    )

    return results.save_dir


def infer_image(model_path: str, image_path: str) -> Any:
    """
    Run YOLO inference on a single image.

    Args:
        model_path (str): Path to YOLO model weights.
        image_path (str): Path to input image.

    Returns:
        Any: YOLO prediction results.
    """
    model = YOLO(model_path)
    results = model(image_path)
    return results
