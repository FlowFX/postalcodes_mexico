=====
Usage
=====

To use Postal codes Mexico in a project::

    from postalcodes_mexico import places

    CP = '01000'

    my_plces = places(CP)

    assert isinstance(my_places, list) == True
    assert isinstance(my_places[0], tuple) == True
