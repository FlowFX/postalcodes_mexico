# -*- coding: utf-8 -*-
"""Main package of 'postalcodes_mexico'."""

__author__ = """Florian Posdziech"""
__email__ = 'hallo@flowfx.de'
__version__ = '0.1.0'

import os
import sqlite3

from collections import namedtuple

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, 'data/postalcodes.sqlite3'))

Location = namedtuple(
    'Location',
    [
        'postal_code',
        'place',
        'place_type',
        'municipality',
        'city',
        'state',
    ]
)


def places(postalcode, db_name=DB_PATH):
    """Return a list of tuples with address information."""
    con = sqlite3.connect(db_name)
    con.row_factory = sqlite3.Row

    try:
        assert len(postalcode) >= 4
        assert len(postalcode) <= 5
        int(postalcode)
    except Exception:
        msg = 'Valid postal codes consist of 4 or 5 digits.'
        raise ValueError(msg)

    if len(postalcode) == 4:
        postalcode = '0{}'.format(postalcode)

    cp = (postalcode, )

    with con:
        c = con.cursor()

        c.execute('SELECT cp, place, place_type, municipality, city, state\
                   FROM places WHERE cp =?', cp)

        # create a list of named tuples
        result = [location for location in map(Location._make, c.fetchall())]

    return result


def postalcodes(postalcode='', db=DB_PATH):
    """Return a list of postal codes."""
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row

    with con:
        c = con.cursor()

        c.execute(
            'SELECT cp FROM places WHERE cp LIKE ?',
            ('{}%'.format(postalcode),)
        )

        # Return a list of unique postal codes.
        # The set comprehension does that for us.
        result = list({row[0] for row in c})

    return result
