# -*- coding: utf-8 -*-
"""Test suit for postalcodes_mexico."""
import sqlite3

import postalcodes_mexico

import utils


def test_update_db():
    # GIVEN a test database and a short XML file
    test_db = 'test.db'
    xml_file = 'data/ciudad_de_mexico.xml'

    # WHEN calling the update method
    utils.update_db(db=test_db, xml_file=xml_file)

    con = sqlite3.connect(test_db)
    con.row_factory = sqlite3.Row

    # THEN the test database has entries
    CP = '01000'
    places = postalcodes_mexico.places(CP, db=test_db)

    assert len(places) == 1
    assert isinstance(places, list)

    place = places[0]
    assert place[0] == '01000'
    assert place[1] == 'San Ángel'
    assert place[2] == 'Colonia'
    assert place[3] == 'Álvaro Obregón'
    assert place[4] == 'Ciudad de México'
    assert place[5] == 'Ciudad de México'


def test_xmltolist():
    # GIVEN a short XML file
    xml_file = 'data/ciudad_de_mexico.xml'

    # WHEN calling the xmltolist method
    result = utils.xmltolist(xml_file=xml_file)

    # THEN it returns a list with a lot of places
    assert isinstance(result, list)
    assert len(result) > 1000

    # AND they are tuples
    assert isinstance(result[5], tuple)


def test_catch():
    # GIVEN a dictionary
    data = {'one': 'uno', 'two': 'dos'}

    # WHEN using catch and existing dict key
    # THEN it returns the value
    assert utils.catch(lambda: data['one']) == 'uno'

    # WHEN using catch and a non-existing dict key
    # THEN it returns an empty string
    assert utils.catch(lambda: data['three']) == ''
