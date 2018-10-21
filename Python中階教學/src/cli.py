#-*- coding: utf-8 -*-
import click

from crawler_power import main


@click.command()
@click.option('--url', default='https://www.ptt.cc/bbs/', help="ptt web.")
def cli(url):
    main(url=url)


if __name__ == '__main__':
    cli()