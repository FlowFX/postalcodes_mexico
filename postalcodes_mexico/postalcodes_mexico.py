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


def places(postalcode, db=DB_PATH):
    """Return a list of tuples with address information."""
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row

    try:
        assert len(postalcode) >= 4
        assert len(postalcode) <= 5
    except AssertionError:
        raise ValueError

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

        result = [row[0] for row in c]

    return result
