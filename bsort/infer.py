"""
Infer utilities for BottleSort.
This wrapper exists only to satisfy unit tests that import bsort.infer.infer_image
"""

from __future__ import annotations
from typing import List
import os

# Import the real dummy infer function from model.py
from .model import infer_image as _infer_image


def infer_image(model_path: str, image_path: str) -> List[str]:
    """
    Thin wrapper required by unit tests.
    Calls the actual infer_image from model.py
    """
    return _infer_image(model_path, image_path)
