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
Module for repositories related to locations
"""
from sandvalley.model import Location

class LocationRepository():
    """
    Repository to access locations
    """
    def __init__(self, connection):
        """
        Default constructor
        
        :param connection: database connection to use
        :type connection: Connection
        """
        self.connection = connection

    def save(self, location):
        """
        Save given location
        
        :param location: location to save
        :type location: Location
        :returns: saved location
        :rtype: Location
        """
        assert(location != None)
        
        try:
            cursor = self.connection.cursor()
        
            cursor.execute('savepoint locationsave')
            params = (location.location_name,
                      location.ID)

            if location.ID:
                cursor.execute('update location set name=? where OID=?',
                               params)            
            else:
                cursor.execute('insert into location (name, OID) values (?, ?)',
                               params)
                location.ID = cursor.lastrowid

            cursor.execute('release locationsave')
        except:
            cursor.execute('rollback to locationsave')
            raise

        return location

    def load(self, ID):
        """
        Load a location
        
        :param ID: id of location to load
        :type ID: string
        :returns: location
        :rtype: Location
        """
        cursor = self.connection.cursor()
        
        params = (ID, )
        cursor.execute('select OID, * from location where OID=?', params)
        row = cursor.fetchone()
        
        location = Location()
        location.ID = row['ROWID']
        location.location_name = row['name']
        
        return location