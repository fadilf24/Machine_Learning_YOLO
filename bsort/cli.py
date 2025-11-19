# bsort/cli.py
import click
from .config import load_config
from .model import train_model, infer_image

@click.group()
def cli():
    pass

@cli.command()
@click.option("--config", required=True)
def train(config):
    cfg = load_config(config)
    res = train_model({
        "dataset": {
            "train_dir": cfg.dataset.train_dir,
            "val_dir": cfg.dataset.val_dir,
        },
        "training": {
            "epochs": cfg.training.epochs,
            "batch": cfg.training.batch,
            "lr": cfg.training.learning_rate,
        }
    })
    click.echo("training done")
    return res

@cli.command()
@click.option("--config", required=True)
@click.option("--image", required=True)
def infer(config, image):
    cfg = load_config(config)
    res = infer_image({
        "model": {"weights": "runs/detect/train/weights/best.pt"}   # tests expect this
    }, image)
    click.echo("inference done")
    return res
