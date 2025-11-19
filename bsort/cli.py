# bsort/cli.py
import click
from .config import load_config
from .model import train_model, infer_image

@click.group()
def cli():
    pass

@click.command()
@click.option("--config", required=True)
def train(config):
    cfg = load_config(config)
    res = train_model(cfg)
    click.echo("Training completed")
    
@click.command()
@click.option("--config", required=True)
@click.option("--image", required=True)
def infer(config, image):
    cfg = load_config(config)
    res = infer_image({"model": {"weights": "runs/detect/train/weights/best.pt"}}, image)
    click.echo("Inference result")

