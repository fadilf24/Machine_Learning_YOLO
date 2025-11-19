from ultralytics import YOLO
from typing import Optional


class BottleSortModel:
    """YOLOv8 wrapper class for bottle cap detection."""

    def __init__(self, model_path: str):
        """
        Initialize YOLO model.

        Args:
            model_path (str): Path to model weight.
        """
        self.model = YOLO(model_path)

    def predict(self, image_path: str):
        """Run inference."""
        return self.model(image_path)

    def train(self, data_yaml: str, epochs: int, batch: int, lr: float):
        """
        Train YOLO model.

        Args:
            data_yaml (str): Dataset config file.
            epochs (int)
            batch (int)
            lr (float)
        """
        return self.model.train(
            data=data_yaml,
            epochs=epochs,
            batch=batch,
            lr0=lr,
        )
