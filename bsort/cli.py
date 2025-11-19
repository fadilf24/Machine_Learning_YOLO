import click
from .model import train_model
from .infer import infer_image
from .config import load_config

@click.group()
def cli():
    """BottleSort CLI"""
    pass

@cli.command()
@click.option("--config", required=True, help="Path to YAML config")
def train(config):
    cfg = load_config(config)
    train_model(cfg.training.to_dict())
    click.echo("Training completed")

@cli.command()
@click.option("--config", required=True)
@click.option("--image", required=True)
def infer(config, image):
    cfg = load_config(config)
    result = infer_image("model_trained.pt", image)
    click.echo(str(result))
