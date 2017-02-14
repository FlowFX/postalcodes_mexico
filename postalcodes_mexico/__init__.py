# -*- coding: utf-8 -*-

__author__ = """Florian Posdziech"""
__email__ = 'hallo@flowfx.de'
__version__ = '0.1.0'

import os
import xmltodict
import sqlite3

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, 'postalcodes.sql'))


def places(postalcode, db=DB_PATH):

    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row

    cp = (postalcode, )

    with con:
        c = con.cursor()

        c.execute('SELECT cp, place, place_type, municipality, city, state FROM places WHERE cp =?', cp)

        result = [tuple(row) for row in c]

    return result


def update_db(db=DB_PATH, xml_file='data/CPdescarga.xml'):
    """Update the places database.

    Use the XML files provided by Correos Mexico.
    """

    places = xmltolist(xml_file)
    con = sqlite3.connect(db)

    with con:
        con.execute("DROP TABLE IF EXISTS places")
        con.execute("CREATE TABLE places(cp, place, place_type, municipality, city,  state)")

        con.executemany("INSERT INTO places(cp, place, place_type, municipality, city, state)" +
                        "VALUES (?, ?, ?, ?, ?, ?)", places)


# cf. http://stackoverflow.com/a/8915613
def catch(func, handle=lambda e: e, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except KeyError:
        return ''


def xmltolist(xml_file='data/ciudad_de_mexico.xml'):

    with open(xml_file, 'r') as f:
        xml = f.read()

        data = xmltodict.parse(xml, process_namespaces=True)
        clean_data = data['NewDataSet']['NewDataSet:table']

    places = [(catch(lambda: row['NewDataSet:d_codigo']),
               catch(lambda: row['NewDataSet:d_asenta']),
               catch(lambda: row['NewDataSet:d_tipo_asenta']),
               catch(lambda: row['NewDataSet:d_ciudad']),
               catch(lambda: row['NewDataSet:D_mnpio']),
               catch(lambda: row['NewDataSet:d_estado']),
               ) for row in clean_data]

    return places
