import yaml
from bsort.config import load_config


def test_load_config(tmp_path):
    # Create temporary config YAML
    config_content = """
    dataset:
      train_dir: "data/train"
      val_dir: "data/val"
    training:
      epochs: 10
      batch: 4
      lr: 0.001
    """
    config_file = tmp_path / "config.yaml"
    config_file.write_text(config_content)

    config = load_config(str(config_file))

    assert config["dataset"]["train_dir"] == "data/train"
    assert config["training"]["epochs"] == 10
    assert isinstance(config, dict)
