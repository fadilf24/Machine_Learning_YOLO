"""
CLI for bsort aligned with unit tests.
"""

from __future__ import annotations
import argparse
from dataclasses import dataclass

from bsort.config import load_config
from bsort.model import train_model, infer_image


@dataclass
class CLIResult:
    name: str
    output: str


def cli(argv=None) -> CLIResult:
    """
    CLI entrypoint that returns CLIResult instead of printing.
    """
    parser = argparse.ArgumentParser(prog="bsort")
    sub = parser.add_subparsers(dest="command")

    train_cmd = sub.add_parser("train")
    train_cmd.add_argument("--config", required=True)

    infer_cmd = sub.add_parser("infer")
    infer_cmd.add_argument("--config", required=True)
    infer_cmd.add_argument("--image", required=True)

    args = parser.parse_args(argv)

    if args.command == "train":
        config = load_config(args.config)
        path = train_model(config)
        return CLIResult(name="train", output=path)

    if args.command == "infer":
        config = load_config(args.config)
        result = infer_image(config.model_path, args.image)
        return CLIResult(name="infer", output=str(result))

    return CLIResult(name="none", output="")
