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
Module for repositories related to connections
"""
from sandvalley.model import Connection

class ConnectionRepository():
    """
    Repository to access connection
    """
    def __init__(self, connection):
        """
        Default constructor
        
        :param connection: database connection to use
        :type connection: Connection
        """
        self.connection = connection

    def save(self, connection):
        """
        Save given connection
        
        :param person: connection to save
        :type person: Connection
        :returns: saved connection
        :rtype: Connection
        """
        assert(connection != None)
        
        try:
            cursor = self.connection.cursor()
        
            cursor.execute('savepoint connectionsave')
            params = (connection.connection_name,
                      connection.location1.ID, 
                      connection.location2.ID, 
                      connection.ID)

            if connection.ID:
                cursor.execute('update connection set name=?, location1_id=?, location2_id=? where OID=?',
                               params)            
            else:
                cursor.execute('insert into connection (name, location1_id, location2_id, OID) values (?, ?, ?, ?)',
                               params)
                connection.ID = cursor.lastrowid

            cursor.execute('release connectionsave')
        except:
            cursor.execute('rollback to connectionsave')
            raise

        return connection
        
    def load(self, ID):
        """
        Load a connection
        
        :param ID: id of connection to load
        :type ID: string
        :returns: connection
        :rtype: Connection
        """
        cursor = self.connection.cursor()
        
        params = (ID, )
        cursor.execute('select OID, * from connection where OID=?', params)
        row = cursor.fetchone()
        
        connection = Connection()
        connection.ID = row['ROWID']
        connection.connection_name = row['name']
        connection.location1_ID = row['location1_id']
        connection.location2_ID = row['location2_id']
        
        return connection

    def load_all(self):
        """
        Load all connections
        """
        cursor = self.connection.cursor()
        
        cursor.execute('select OID, * from connection')
        
        rows = cursor.fetchall()
        connections = []
        
        for row in rows:
            connection = Connection()
            connection.ID = row['ROWID']
            connection.connection_name = row['name']
            connection.location1_ID = row['location1_id']
            connection.location2_ID = row['location2_id']
            
            connections.append(connection)
        
        return connections
