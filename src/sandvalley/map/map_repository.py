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
from .map import Map
from sandvalley.map.repositories.location import LocationRepository
from sandvalley.map.repositories.connection import ConnectionRepository

class MapRepository():
    """
    Repository to access maps
    """
    def __init__(self, connection):
        """
        Default constructor
        
        :param connection: database connection to use
        :type connection: Connection
        """
        self.location_repository = LocationRepository(connection)
        self.connection_repository = ConnectionRepository(connection)
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

    def load(self):
        """
        Load a map
        """
        town_map = Map()
        
        locations = self.location_repository.load_all()
        connections = self.connection_repository.load_all()
        
        for location in locations:
            town_map.locations.append(location)

        for connection in connections:
            town_map.connections.append(connection)

        self.__link_locations(town_map)

        return town_map

    def __link_locations(self, town_map):
        """
        Link locations via connections
        """
        for connection in town_map.connections:
            loc1 = [x for x in town_map.locations
                    if x.ID == connection.location1_ID][0]

            loc2 = [x for x in town_map.locations
                    if x.ID == connection.location2_ID][0]
                    
            loc1.connections.append(connection)
            loc2.connections.append(connection)
            connection.location1 = loc1
            connection.location2 = loc2
