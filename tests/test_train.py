from unittest.mock import patch
from bsort.model import train_model


@patch("bsort.model.YOLO")
def test_train_model(mock_yolo, tmp_path):
    # Mock model object
    mock_model_instance = mock_yolo.return_value
    mock_model_instance.train.return_value = {"status": "success"}

    config = {
        "dataset": {
            "train_dir": "data/train",
            "val_dir": "data/val",
        },
        "training": {
            "epochs": 1,
            "batch": 2,
            "lr": 0.001,
        },
    }

    result = train_model(config)

    assert "status" in result
    mock_model_instance.train.assert_called_once()
