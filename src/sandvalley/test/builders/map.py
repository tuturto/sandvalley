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
Module for map builder
"""
from sandvalley.map import Map

class MapBuilder():
    """
    Builder for maps
    """
    def __init__(self):
        """
        Default constructor
        """
        self.locations = []
        self.connections = []

    def with_location(self, location):
        """
        Add a location to map
        
        .. note: can be called multiple times
        """
        self.locations.append(location)
        return self
    
    def with_connection(self, connection):
        """
        Add a connection to map
        
        .. note: can be called multiple times
        """
        self.connections.append(connection)
        return self
        
    def build(self):
        """
        Build a map
        """
        map = Map()
        
        for connection in self.connections:
            map.connections.append(connection)
        
        for location in self.locations:
            map.locations.append(location)

        return map
