#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `postalcodes_mexico` package."""

from click.testing import CliRunner

from postalcodes_mexico import postalcodes_mexico
from postalcodes_mexico import cli


class TestPlaces:
    """Test function `places`."""

    def test_places_are_named_tuples(self):
        # GIVEN an existing postal code
        CP = '01000'

        # WHEN using the places method
        my_places = postalcodes_mexico.places(CP)
        my_place = my_places[0]

        # THEN it returns a list of named tuples
        assert isinstance(my_places, list)
        assert isinstance(my_place, tuple)

        # AND all attributes can be called
        assert my_place.postal_code == CP
        assert my_place.place == 'San Ángel'
        assert my_place.place_type == 'Colonia'
        assert my_place.municipality == 'Álvaro Obregón'
        assert my_place.city == 'Ciudad de México'
        assert my_place.state == 'Ciudad de México'

    def test_postal_code_with_one_place(self):
        # GIVEN postal code for San Ángel in Mexico City
        CP = '01000'

        # WHEN using the places method on this postal code
        my_places = postalcodes_mexico.places(CP)

        # THEN it returns a list with exactly one place that is San Ángel
        assert len(my_places) == 1

        my_place = my_places[0]
        assert my_place.postal_code == CP
        assert my_place.place == 'San Ángel'
        assert my_place.place_type == 'Colonia'
        assert my_place.municipality == 'Álvaro Obregón'
        assert my_place.city == 'Ciudad de México'
        assert my_place.state == 'Ciudad de México'

    def test_four_digit_postal_code(self):
        # GIVEN an existing, 4-digit postal code for San Ángel
        CP = '1000'

        # WHEN using the places method
        places = postalcodes_mexico.places(CP)

        # THEN it returns San Ángel
        place = places[0]
        assert place.place == 'San Ángel'

    def test_postal_code_with_multiple_places(self):
        # GIVEN a known postal code with exactly two places
        CP = '01030'

        # WHEN using the places method
        places = postalcodes_mexico.places(CP)

        # THEN it returns a list of two places
        assert isinstance(places, list)
        assert len(places) == 2


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['01000'])
    assert result.exit_code == 0
    assert 'San Ángel' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
