# -*- coding: utf-8 -*-

"""Console script for postalcodes_mexico."""
import sys
import click

from postalcodes_mexico import postalcodes_mexico


@click.command()
@click.argument('postalcode', type=str)
def main(postalcode):
    """Console script for postalcodes_mexico."""
    places = postalcodes_mexico.places(postalcode)
    click.echo(places)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
