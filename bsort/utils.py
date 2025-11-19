import os
import cv2
from typing import List
from ultralytics import YOLO


def ensure_exists(path: str) -> None:
    """Ensure folder exists; create if not."""
    os.makedirs(path, exist_ok=True)


def draw_boxes(image_path: str, model: YOLO, save_path: str = None):
    """
    Draw bounding boxes using YOLO predictions.

    Args:
        image_path (str): Path to image.
        model (YOLO): Loaded YOLO model.
        save_path (str, optional): Save output path.

    Returns:
        ndarray: Image with boxes.
    """
    results = model(image_path)[0]
    img = cv2.imread(image_path)

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = f"{model.names[cls]} {conf:.2f}"

        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
        cv2.putText(img, label, (int(x1), int(y1)-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    if save_path:
        cv2.imwrite(save_path, img)

    return img
