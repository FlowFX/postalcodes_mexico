# -*- coding: utf-8 -*-
"""Utils module of 'postalcodes_mexico'."""
import sqlite3

import xmltodict


def update_db(db_name, xml_file):
    """Update the places database.

    Use the XML files provided by Correos Mexico.
    """
    places = xmltolist(xml_file)
    con = sqlite3.connect(db_name)

    with con:
        con.execute("DROP TABLE IF EXISTS places")

        sql = ("CREATE TABLE places("
               "cp, place, place_type, municipality, city,  state)")
        con.execute(sql)

        sql = ("INSERT INTO places("
               "cp, place, place_type, municipality, city, state) "
               "VALUES (?, ?, ?, ?, ?, ?)")
        con.executemany(sql, places)


def xmltolist(xml_file):
    """Convert the original XML file to a list of places as tuples."""
    with open(xml_file, 'r') as f:
        xml = f.read()

        data = xmltodict.parse(xml, process_namespaces=True)
        clean_data = data['NewDataSet']['NewDataSet:table']

    # Some places don't have e.g. a municipality.
    places = [(catch(lambda: row['NewDataSet:d_codigo']),
               catch(lambda: row['NewDataSet:d_asenta']),
               catch(lambda: row['NewDataSet:d_tipo_asenta']),
               catch(lambda: row['NewDataSet:D_mnpio']),
               catch(lambda: row['NewDataSet:d_ciudad']),
               catch(lambda: row['NewDataSet:d_estado']),
               ) for row in clean_data]

    return places


def catch(func, handle=lambda e: e, *args, **kwargs):
    """Helper function to enable the list comprehension in xmltolist.

    Whenenver a data field doesn't have an entry, put an empty string.

    cf. http://stackoverflow.com/a/8915613
    """
    try:
        return func(*args, **kwargs)
    except KeyError:
        return ''
