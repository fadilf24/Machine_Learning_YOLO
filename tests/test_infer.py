from unittest.mock import patch
from bsort.model import infer_image


@patch("bsort.model.YOLO")
def test_infer_image(mock_yolo, tmp_path):
    # Create temporary fake image
    img_file = tmp_path / "sample.jpg"
    img_file.write_bytes(b"\x00\x01")

    # Mock prediction output
    mock_model_instance = mock_yolo.return_value
    mock_model_instance.predict.return_value = ["dummy_result"]

    config = {
        "model": {
            "weights": "runs/detect/train/weights/best.pt"
        }
    }

    result = infer_image(config, str(img_file))

    assert result == ["dummy_result"]
    mock_model_instance.predict.assert_called_once()
