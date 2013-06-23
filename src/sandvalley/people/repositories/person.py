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
Module for repositories related to persons
"""
from sandvalley.people.person import Person
from sandvalley.people.repositories.schedule import ScheduleRepository

class PersonRepository():
    """
    Repository to access persons
    """
    def __init__(self, connection):
        """
        Default constructor
        
        :param connection: database connection to use
        :type connection: Connection
        """
        self.connection = connection

    def save(self, person):
        """
        Save given person
        
        :param person: person to save
        :type person: Person
        :returns: saved person
        :rtype: Person
        """
        assert(person != None)
        
        try:
            cursor = self.connection.cursor()
        
            cursor.execute('savepoint personsave')
            params = (person.person_name,
                      person.ID)

            if person.ID:
                cursor.execute('update person set name=? where OID=?',
                               params)            
            else:
                cursor.execute('insert into person (name, OID) values (?, ?)',
                               params)
                person.ID = cursor.lastrowid

            for appointment in person.schedule.appointments:
                appointment.person_id = person.ID

            schedule_repository = ScheduleRepository(self.connection)
            schedule_repository.save(person.schedule)

            cursor.execute('release personsave')
        except:
            cursor.execute('rollback to personsave')
            raise

        return person

    def load(self, ID):
        """
        Load a person
        
        :param ID: id of person to load
        :type ID: string
        :returns: person
        :rtype: Person
        """
        cursor = self.connection.cursor()

        schedule_repository = ScheduleRepository(self.connection)

        params = (ID, )
        cursor.execute('select OID, * from person where OID=?', params)
        row = cursor.fetchone()
        
        person = Person()
        person.ID = row['ROWID']
        person.person_name = row['name']
        person.schedule = schedule_repository.load(ID)
        print(person.schedule)
        
        return person
