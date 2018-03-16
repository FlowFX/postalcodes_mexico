=====
Usage
=====

To use Postalcodes Mexico in a project::

    >>> from postalcodes_mexico.postalcodes_mexico import places
    >>> places('01000')
    [Location(postal_code='01000', place='San Ángel', place_type='Colonia', municipality='Álvaro Obregón', city='Ciudad de México', state='Ciudad de México')]
    >>> my_place = places('01030')[1]
    >>> my_place.postal_code
    01030
    >>> my_place.place
    Florida
    >>> my_place.place_type
    Colonia
    >>> my_place.municipality
    Álvaro Obregón
    >>> my_place.city
    Ciudad de México
    >>> my_place.state
    Ciudad de México
