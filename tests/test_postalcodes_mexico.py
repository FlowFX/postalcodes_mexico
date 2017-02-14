# -*- coding: utf-8 -*-
import sqlite3
from postalcodes_mexico import postalcodes_mexico


def test_places_with_one_place():

    CP = '01000'

    places = postalcodes_mexico.places(CP)

    assert isinstance(places, list)
    assert len(places) == 1


def test_places_with_multiple_places():

    CP = '01030'

    places = postalcodes_mexico.places(CP)

    assert isinstance(places, list)
    assert len(places) == 2


def test_update_db():
    test_db = 'test.db'
    xml_file = 'data/ciudad_de_mexico.xml'

    postalcodes_mexico.update_db(db=test_db, xml_file=xml_file)

    con = sqlite3.connect(test_db)
    con.row_factory = sqlite3.Row

    CP = '01000'

    places = postalcodes_mexico.places(CP, db=test_db)

    assert len(places) == 1
    assert isinstance(places, list)

    place = places[0]

    assert place[0] == '01000'
    assert place[1] == 'San Ángel'


def test_xmltolist():

    xml_file = 'data/ciudad_de_mexico.xml'
    result = postalcodes_mexico.xmltolist(xml_file)

    assert isinstance(result, list)
    assert len(result) > 1000
