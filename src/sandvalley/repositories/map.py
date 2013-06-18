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
Module for repositories related to maps
"""
from sandvalley.model import Map

class MapRepository():
    """
    Repository to access maps
    """
    def __init__(self, location_repository, connection_repository, connection):
        """
        Default constructor
        
        :param connection: database connection to use
        :type connection: Connection
        """
        self.location_repository = location_repository
        self.connection_repository = connection_repository
        self.connection = connection

    def save(self, map):
        """
        Save given map
        """
        assert(map != None)
        
        try:
            cursor = self.connection.cursor()
        
            cursor.execute('savepoint mapsave')
            
            for location in map.locations:
                self.location_repository.save(location)
            for connection in map.connections:
                self.connection_repository.save(connection)
            
            cursor.execute('release mapsave')
        except:
            cursor.execute('rollback to mapsave')
            raise

        return map

    def load(self, ID):
        """
        Load a map
        """
        map = Map()
        return map
