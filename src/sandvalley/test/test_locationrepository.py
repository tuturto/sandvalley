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
Tests for location repository
"""

from sandvalley.map.repositories.location import LocationRepository
from sandvalley.database import create_schema
import sqlite3

from sandvalley.test.builders import LocationBuilder
from hamcrest import assert_that, is_, equal_to

class TestLocationRepository():
    """
    Test location repository
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
        self.connection.isolation_level = None
        
        create_schema(self.connection)

    def teardown(self):
        """
        Clean up after test
        """
        self.connection.close()

    def test_persistance(self):
        """
        Test that a location can be saved and loaded
        """
        location = LocationBuilder().build()
        
        repository = LocationRepository(self.connection)
        
        location = repository.save(location)
        loaded_location = repository.load(location.ID)
        
        assert_that(loaded_location.ID, is_(equal_to(location.ID)))
        assert_that(loaded_location.location_name, 
                    is_(equal_to(location.location_name)))

    def test_updating_location(self):
        """
        Test that saved location can be updated
        """
        location = (LocationBuilder()
                        .with_name('Car repairs')
                        .build())
                        
        repository = LocationRepository(self.connection)        
        location = repository.save(location)

        location.location_name = 'Pharmacy'
        location = repository.save(location)
        
        loaded_location = repository.load(location.ID)
        assert_that(loaded_location.location_name,
                    is_(equal_to('Pharmacy')))
