from bsort.model import BottleSortModel
from bsort.utils import draw_boxes
from bsort.config import AppConfig
import os


def run_inference(config: AppConfig, image_path: str, save_output: bool = True):
    """
    Run inference and return final image.

    Args:
        config (AppConfig)
        image_path (str)
        save_output (bool)

    Returns:
        ndarray: Image with bounding boxes
    """

    model_path = "runs/detect/train/weights/best.pt"

    model = BottleSortModel(model_path)

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    save_path = None
    if save_output:
        save_path = os.path.join(output_dir, "result.jpg")

    img = draw_boxes(image_path, model.model, save_path=save_path)
    return img
