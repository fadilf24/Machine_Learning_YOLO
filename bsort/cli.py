"""
Command-line interface for bsort tool.
"""

from __future__ import annotations
import argparse
import yaml
from bsort.model import train_model, infer_image


def load_config(path: str) -> dict:
    """Load YAML config file."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def cli() -> None:
    """Main CLI entrypoint."""
    parser = argparse.ArgumentParser(prog="bsort")

    sub = parser.add_subparsers(dest="command")

    train_cmd = sub.add_parser("train")
    train_cmd.add_argument("--config", required=True)

    infer_cmd = sub.add_parser("infer")
    infer_cmd.add_argument("--config", required=True)
    infer_cmd.add_argument("--image", required=True)

    args = parser.parse_args()

    if args.command == "train":
        config = load_config(args.config)
        output = train_model(config)
        print(f"Model trained and saved at: {output}")

    elif args.command == "infer":
        config = load_config(args.config)
        model_path = config["model_path"]
        result = infer_image(model_path, args.image)
        print(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    cli()
