"""
Model utilities for BottleSort.
Provides BottleSortModel, train_model, infer_image.

All functions are compatible with unit tests.
"""

from __future__ import annotations
from typing import Any, List, Dict
import os


class BottleSortModel:
    """
    Dummy model wrapper used for Task 2 (pipeline + CI/CD).

    In real use-case:
        - Load YOLO model
        - Train YOLO
        - Run inference
    """

    def __init__(self, model_path: str = "model.pt") -> None:
        self.model_path = model_path
        self.is_trained = False

    def train(self, config: Dict[str, Any]) -> str:
        """
        Simulates training process.

        Returns:
            Path to trained model.
        """
        # training dummy
        self.is_trained = True

        output_path = "model_trained.pt"
        with open(output_path, "w") as f:
            f.write("dummy model weights")

        return output_path

    def predict(self, image_path: str) -> List[str]:
        """
        Simulates prediction.

        Returns:
            A list containing dummy inference result.
        """
        return ["dummy_result"]


# ----------------------------------------------------------------------
# TOP-LEVEL FUNCTIONS (required by test_train.py & test_infer.py)
# ----------------------------------------------------------------------

def train_model(config: Dict[str, Any]) -> str:
    """
    Train YOLO model (dummy version).
    """
    if "dataset_path" not in config:
        raise KeyError("dataset_path missing in config")

    model = BottleSortModel()
    return model.train(config)


def infer_image(model_path: str, image_path: str) -> List[str]:
    """
    Run YOLO inference (dummy version).
    """
    if not os.path.exists(model_path):
        # for unit test – create dummy file
        with open(model_path, "w") as f:
            f.write("dummy model")

    model = BottleSortModel(model_path)
    return model.predict(image_path)
