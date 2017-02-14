# -*- coding: utf-8 -*-
import sqlite3

import postalcodes_mexico
import pytest


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


def test_postalcodes_without_parameter():

    cp_list = postalcodes_mexico.postalcodes()

    assert isinstance(cp_list, list)
    assert len(cp_list) > 100000
    assert '01000' in cp_list


@pytest.mark.parametrize(
    'cp, cp_full', [
        ('01', '01000'),
        ('0103', '01030'),
        ('99', '99998'),
    ]
)
def test_postalcodes_with_beginning_of_postalcode(cp, cp_full):

    cp_list = postalcodes_mexico.postalcodes(cp)

    assert cp_full in cp_list


@pytest.mark.parametrize('cp', [('00'),('99999'),('88888'),])
def test_non_existing_postalcodes(cp):

    cp_list = postalcodes_mexico.postalcodes(cp)

    assert len(cp_list) == 0
