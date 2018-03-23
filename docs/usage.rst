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


Updating the database
---------------------

The PyPI package comes with the database of Mexican postal codes included. In
order to update the database in the development package, I use the following
steps:

1. Go to http://www.correosdemexico.gob.mx/lservicios/servicios/CodigoPostal_Exportar.aspx
2. Select 'Todos' and 'XML'
3. Click 'Descarga'
4. Unzip the `CPDescargaxml.zip` to the dev folder
5. Start the Python repl from inside the dev folder

    >>> from postalcodes_mexico import utils
    >>> utils('postalcodes_mexico/data/postalcodes.sqlite3', 'CPDescarga.xml')

Hopefully, no-one besides me ever has to do this. Or someone implements this as `a command-line option`_.

.. _a command-line option: https://github.com/FlowFX/postalcodes_mexico/issues/88
