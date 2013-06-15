#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright 2013 Tuukka Turto
#
#   This file is part of Sand Valley.
#
#   Sand Valley is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Sand Valley is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Sand Valley.  If not, see <http://www.gnu.org/licenses/>.

"""
Tests for person repository
"""

from sandvalley.repositories import PersonRepository
import sqlite3

from sandvalley.test.builders import PersonBuilder
from hamcrest import assert_that, is_, equal_to

class TestPersonRepository():
    """
    Test person repository
    """
    def __init__(self):
        """
        Default constructor
        """
        self.connection = None

    def setup(self):
        """
        Setup test cases
        """
        self.connection = sqlite3.connect(':memory:')
        self.connection.row_factory = sqlite3.Row
        cursor = self.connection.cursor()
        
        cursor.execute('''create table person
                          (name text)''')
        self.connection.commit()

    def teardown(self):
        """
        Clean up after test
        """
        self.connection.close()

    def test_persistance(self):
        """
        Test that a person can be saved and loaded
        """
        person = PersonBuilder().build()
        
        repository = PersonRepository(self.connection)
        
        person = repository.save(person)        
        loaded_person = repository.load(person.ID)
        
        assert_that(loaded_person.ID, is_(equal_to(person.ID)))
        assert_that(loaded_person.person_name, 
                    is_(equal_to(person.person_name)))
