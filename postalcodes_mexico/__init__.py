"""Main package of 'postalcodes_mexico'."""
# -*- coding: utf-8 -*-

__author__ = """Florian Posdziech"""
__email__ = 'hallo@flowfx.de'
__version__ = '0.1.0'

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, 'postalcodes.sql'))


def places(postalcode, db=DB_PATH):
    """Return a list of tuples with address information."""
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row

    cp = (postalcode, )

    with con:
        c = con.cursor()

        c.execute('SELECT cp, place, place_type, municipality, city, state FROM places WHERE cp =?', cp)

        result = [tuple(row) for row in c]

    return result


def postalcodes(postalcode='', db=DB_PATH):
    """Return a list of postal codes."""
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row

    with con:
        c = con.cursor()

        c.execute('SELECT cp FROM places WHERE cp LIKE ?', ('{}%'.format(postalcode),))
        # cursor.execute("SELECT * FROM posts WHERE tags LIKE ?", ('%{}%'.format(tag),))

        result = [row[0] for row in c]

    return result
