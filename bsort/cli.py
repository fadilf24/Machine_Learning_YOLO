import click
from .config import load_config
from .model import train_model, infer_image


@click.group()
def cli():
    """BottleSort CLI"""
    pass


@cli.command()
@click.option("--config", required=True)
def train(config):
    cfg = load_config(config)
    train_model(cfg)
    click.echo("Training completed")


@cli.command()
@click.option("--config", required=True)
@click.option("--image", required=True)
def infer(config, image):
    cfg = load_config(config)
    infer_image(cfg, image)
    click.echo("Inference result")
