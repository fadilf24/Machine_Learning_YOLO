from click.testing import CliRunner
from bsort.cli import cli
from unittest.mock import patch


def test_cli_train():
    runner = CliRunner()

    with patch("bsort.cli.train_model") as mock_train:
        mock_train.return_value = {"status": "ok"}

        result = runner.invoke(cli, ["train", "--config", "settings.yaml"])

        assert result.exit_code == 0
        assert "Training completed" in result.output


def test_cli_infer(tmp_path):
    img = tmp_path / "test.jpg"
    img.write_bytes(b"\x00\x01")

    with patch("bsort.cli.infer_image") as mock_infer:
        mock_infer.return_value = ["dummy"]

        runner = CliRunner()
        result = runner.invoke(
            cli, ["infer", "--config", "settings.yaml", "--image", str(img)]
        )

        assert result.exit_code == 0
        assert "Inference result" in result.output
