==================
Postalcodes Mexico
==================


.. image:: https://img.shields.io/pypi/v/postalcodes_mexico.svg
        :target: https://pypi.python.org/pypi/postalcodes_mexico

.. image:: https://img.shields.io/travis/flowfx/postalcodes_mexico.svg
        :target: https://travis-ci.org/flowfx/postalcodes_mexico

.. image:: https://readthedocs.org/projects/postalcodes-mexico/badge/?version=latest
        :target: https://postalcodes-mexico.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Determines large parts of a Mexican postal address from its postal code (C.P.).


* Free software: MIT license
* Documentation: https://postalcodes-mexico.readthedocs.io.


Features
--------

The function `places` returns a list of named tuples with all places that share the postal code.

    >>> from postalcodes_mexico import places
    >>> places('01000')
    [('01000', 'San Ángel', 'Colonia', 'Ciudad de México', 'Álvaro Obregón', 'Ciudad de México')]
    >>> my_places = places('01030')
    >>> len(my_places)
    2
    >>> my_places[0]
    ('01030', 'Axotla', 'Pueblo', 'Ciudad de México', 'Álvaro Obregón', 'Ciudad de México')
    >>> my_places[1]
    ('01030', 'Florida', 'Colonia', 'Ciudad de México', 'Álvaro Obregón', 'Ciudad de México')
    >>> for place in my_places:
    ...     print(place[0], place[1], place[3])
    ...
    01030 Axotla Ciudad de México
    01030 Florida Ciudad de México
    >>> my_place = places('01000')[0]
    >>> my_place.postal_code
    01000
    >>> my_place.city
    Ciudad de Méxic
    >>> my_place.place_type
    Colonia

Reference
---------
The data used in this package comes from the official website of the `Mexican Postal Service`_ (Correos Mexico). On the download page of the `catalogue of postal codes`_ it is stated that this data is not to be commercialized:

    El Catálogo Nacional de Códigos Postales, es elaborado por el Servicio Postal Mexicano y se proporciona en forma gratuita, no estando permitida su comercialización, total o parcial.

http://www.correosdemexico.gob.mx/lservicios/servicios/CodigoPostal_Exportar.aspx

.. _Mexican Postal Service: http://www.correosdemexico.com.mx/Paginas/Inicio.aspx
.. _catalogue of postal codes: http://www.correosdemexico.gob.mx/lservicios/servicios/CodigoPostal_Exportar.aspx

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
