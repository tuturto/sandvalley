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
Module for connection builder
"""
from sandvalley.model import Connection

class ConnectionBuilder():
    """
    Builder for connections
    """
    def __init__(self):
        """
        Default constructor
        """
        self.connection_name = 'prototype'
        self.start_location = None
        self.end_location = None
        
    def with_name(self, connection_name):
        """
        Configure name of the connection
        """
        self.connection_name = connection_name
        return self

    def with_start(self, location):
        """
        Configure start location
        """
        self.start_location = location
        return self
    
    def with_end(self, location):
        """
        Configure end location
        """
        self.end_location = location
        return self

    def build(self):
        """
        Build a connection
        """
        connection = Connection()
        connection.connection_name = self.connection_name
        connection.location1 = self.start_location
        connection.location2 = self.end_location
        
        return connection
