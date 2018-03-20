#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `postalcodes_mexico.utils` module."""

import sqlite3

from postalcodes_mexico import postalcodes_mexico, utils


def test_update_db():
    # GIVEN a test database and a short XML file
    test_db = 'test.db'
    xml_file = 'tests/data/ciudad_de_mexico.xml'

    # WHEN calling the database update function
    utils.update_db(db_name=test_db, xml_file=xml_file)

    con = sqlite3.connect(test_db)
    con.row_factory = sqlite3.Row

    # THEN the test database has entries
    CP = '01000'
    places = postalcodes_mexico.places(CP, db_name=test_db)

    assert len(places) == 1
    assert isinstance(places, list)

    place = places[0]
    assert place.postal_code == '01000'
    assert place.place == 'San Ángel'
    assert place.place_type == 'Colonia'
    assert place.municipality == 'Álvaro Obregón'
    assert place.city == 'Ciudad de México'
    assert place.state == 'Ciudad de México'


def test_xmltolist():
    # GIVEN a short XML file
    xml_file = 'tests/data/ciudad_de_mexico.xml'

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
