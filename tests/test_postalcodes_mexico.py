"""Test suit for postalcodes_mexico."""
# -*- coding: utf-8 -*-
import postalcodes_mexico

import pytest


def test_places_with_one_place():
    # GIVEN a single, existing postal code
    CP = '01000'

    # WHEN using the places method
    places = postalcodes_mexico.places(CP)

    # THEN it returns a list with exactly one place
    assert isinstance(places, list)
    assert len(places) == 1

    # AND that place is San Ángel
    place = places[0]
    assert place[1] == 'San Ángel'


def test_places_with_multiple_places():
    # GIVEN another known postal code
    CP = '01030'

    # WHEN using the places method
    places = postalcodes_mexico.places(CP)

    # THEN it returns a list of two places
    assert isinstance(places, list)
    assert len(places) == 2


def test_postalcodes_without_parameter():
    # GIVEN the full database

    # WHEN calling the postalcodes method without a parameter
    cp_list = postalcodes_mexico.postalcodes()

    # THEN it returns a list of all Mexican postal codes
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
    # GIVEN the beginning of a postal code

    # WHEN calling the postalcodes method with the beginning of the CP as a parameter
    cp_list = postalcodes_mexico.postalcodes(cp)

    # THEN a matching full postal code is in the returned list
    assert cp_full in cp_list


@pytest.mark.parametrize('cp', [('00'), ('99999'), ('88888'), ])
def test_non_existing_postalcodes(cp):
    # GIVEN the beginning of a non-existent postal code

    # WHEN calling the postalcodes method with it
    cp_list = postalcodes_mexico.postalcodes(cp)

    # THEN the returned list is empty
    assert len(cp_list) == 0
