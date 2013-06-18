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
Tests for connection repository
"""

from sandvalley.repositories import ConnectionRepository, LocationRepository
from sandvalley.repositories import MapRepository
from sandvalley.repositories.schema import create_schema
import sqlite3

from sandvalley.test.builders import ConnectionBuilder, LocationBuilder
from sandvalley.test.builders import MapBuilder
from sandvalley.test.matchers import has_location
from hamcrest import assert_that, is_, equal_to

class TestMapRepository():
    """
    Test map repository
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
        Test that a connection can be saved and loaded
        """
        location1 = (LocationBuilder()
                        .with_name('service station')
                        .build())
        location2 = (LocationBuilder()
                        .with_name('house')
                        .build())
                        
        connection = (ConnectionBuilder()
                        .with_name('path')
                        .with_start(location1)
                        .with_end(location2)
                        .build())

        map = (MapBuilder()
                    .with_location(location1)
                    .with_location(location2)
                    .with_connection(connection)
                    .build())

        connection_repository = ConnectionRepository(self.connection)
        location_repository = LocationRepository(self.connection)
        
        repository = MapRepository(location_repository, 
                                   connection_repository, 
                                   self.connection)
        repository.save(map)
        
        house = location_repository.load(location2.ID)
        assert_that(house.location_name, is_(equal_to('house')))

        station = location_repository.load(location1.ID)
        assert_that(station.location_name, is_(equal_to('service station')))

        loaded_map = repository.load(map.ID)
        
        assert_that(loaded_map, has_location(house))
        assert_that(loaded_map, has_location(station))
