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
Module for creating the database schema
"""
def create_schema(connection):
    """
    Create schema

    :param connection: database connection to use
    :type connection: Connection
    """
    connection.execute('''create table location
                       (name text)''')
    
    connection.execute('''create table person
                       (name text)''')

    connection.execute('''create table appointment
                       (person_id integer,
                        location_id integer,
                        season integer,
                        weekday integer,
                        time integer,
                        foreign key(person_id) references person(OID),
                        foreign key(location_id) references location(OID)
                        )''')

    connection.execute('''create table connection
                       (name text,
                        location1_id integer,
                        location2_id integer,
                        foreign key(location1_id) references location(OID),
                        foreign key(location2_id) references location(OID))''')

    connection.commit()
