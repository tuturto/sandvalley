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

from sandvalley.map import MapRepository
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
        station  = (LocationBuilder()
                        .with_name('service station')
                        .build())
        house = (LocationBuilder()
                        .with_name('house')
                        .build())
                        
        path = (ConnectionBuilder()
                        .with_name('path')
                        .with_start(station)
                        .with_end(house)
                        .build())

        town_map = (MapBuilder()
                    .with_location(station)
                    .with_location(house)
                    .with_connection(path)
                    .build())
        
        repository = MapRepository(self.connection)
        repository.save(town_map)

        loaded_map = repository.load()
        
        assert_that(loaded_map, has_location(house))
        assert_that(loaded_map, has_location(station))

    def test_linking(self):
        """
        Loading a map should link locations via connections
        """
        station  = (LocationBuilder()
                        .with_name('service station')
                        .build())
        house = (LocationBuilder()
                        .with_name('house')
                        .build())
                        
        path = (ConnectionBuilder()
                        .with_name('path')
                        .with_start(station)
                        .with_end(house)
                        .build())

        town_map = (MapBuilder()
                    .with_location(station)
                    .with_location(house)
                    .with_connection(path)
                    .build())
        
        repository = MapRepository(self.connection)
        repository.save(town_map)

        loaded_map = repository.load()
        
        houses = [x for x in loaded_map.locations
                  if x.location_name == 'house']
        loaded_house = houses[0]
        
        stations = [x for x in loaded_map.locations
                    if x.location_name == 'service station']
        loaded_station = stations[0]
        
        assert_that(loaded_house.connections[0], 
                    is_(equal_to(loaded_station.connections[0])))
