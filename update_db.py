#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import utils

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, 'postalcodes_mexico/data/postalcodes.sqlite3'))
XML_PATH = os.path.abspath(os.path.join(BASE_DIR, 'data/CPdescarga.xml'))


utils.update_db(db=DB_PATH, xml_file=XML_PATH)
