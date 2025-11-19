import argparse
from bsort.config import load_config
from bsort.train import run_training
from bsort.infer import run_inference


def main():
    parser = argparse.ArgumentParser(description="Bottle cap detection CLI")

    sub = parser.add_subparsers(dest="command")

    # TRAIN
    train_cmd = sub.add_parser("train")
    train_cmd.add_argument("--config", required=True)

    # INFER
    infer_cmd = sub.add_parser("infer")
    infer_cmd.add_argument("--config", required=True)
    infer_cmd.add_argument("--image", required=True)

    args = parser.parse_args()

    config = load_config(args.config)

    if args.command == "train":
        run_training(config)

    elif args.command == "infer":
        run_inference(config, args.image)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
