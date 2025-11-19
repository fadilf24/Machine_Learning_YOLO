import click
from .config import load_config
from .train import train_model
from .infer import infer_image

@click.group()
def cli():
    """Root CLI for bsort."""
    pass

@cli.command()
@click.option("--config", required=True)
def train(config):
    cfg = load_config(config)
    res = train_model(cfg)
    click.echo("ok")
    return res

@cli.command()
@click.option("--config", required=True)
@click.option("--image", required=True)
def infer(config, image):
    cfg = load_config(config)
    out = infer_image(cfg, image)
    click.echo(out)
    return out

if __name__ == "__main__":
    cli()
