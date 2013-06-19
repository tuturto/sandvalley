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

from sandvalley.repositories.connection import ConnectionRepository
from sandvalley.repositories.schema import create_schema
import sqlite3

from sandvalley.test.builders import ConnectionBuilder, LocationBuilder
from hamcrest import assert_that, is_, equal_to

class TestConnectionRepository():
    """
    Test connection repository
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
        connection = (ConnectionBuilder()
                        .with_name('path')
                        .with_start(LocationBuilder().build())
                        .with_end(LocationBuilder().build())
                        .build())
                        
        repository = ConnectionRepository(self.connection)
        repository.save(connection)
        
        loaded = repository.load(connection.ID)
        assert_that(loaded.connection_name, is_(equal_to(connection.connection_name)))
        

    def test_updating_location(self):
        """
        Test that saved connection can be updated
        """
        connection = (ConnectionBuilder()
                        .with_name('path')
                        .with_start(LocationBuilder().build())
                        .with_end(LocationBuilder().build())
                        .build())
                        
        repository = ConnectionRepository(self.connection)
        repository.save(connection)
        
        connection.connection_name = 'road'
        repository.save(connection)
        
        loaded = repository.load(connection.ID)
        
        assert_that(loaded.connection_name, is_(equal_to('road')))
