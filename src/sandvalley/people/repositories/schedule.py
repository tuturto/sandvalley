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
Module for repositories related to schedule
"""
from sandvalley.people.schedule import Schedule, Appointment
from sandvalley.map.repositories.location import LocationRepository

class ScheduleRepository():
    """
    Repository to access schedules
    """
    def __init__(self, connection):
        """
        Default constructor
        
        :param connection: database connection to use
        :type connection: Connection
        """
        self.connection = connection

    def save(self, schedule):
        """
        Save given schedule
        """
        assert(schedule != None)
        
        try:
            cursor = self.connection.cursor()
        
            cursor.execute('savepoint schedulesave')
            
            for appointment in schedule.appointments:
                params = (appointment.season,
                          appointment.weekday,
                          appointment.time,
                          appointment.location_id,
                          appointment.person_id,
                          appointment.ID)

                if appointment.ID:
                    cursor.execute('update appointment set season=?, weekday=?, time=?, location_id=?, person_id=? where OID=?',
                                   params)            
                else:
                    cursor.execute('insert into appointment (season, weekday, time, location_id, person_id, OID) values (?, ?, ?, ?, ?, ?)',
                                   params)
                appointment.ID = cursor.lastrowid

            cursor.execute('release schedulesave')
        except:
            cursor.execute('rollback to schedulesave')
            raise

        return schedule

    def load(self, person_id):
        """
        Load a schedule
        """
        locations = LocationRepository(self.connection)
        cursor = self.connection.cursor()
        
        params = (person_id, )
        cursor.execute('select OID, * from appointment where person_id=?', params)
        rows = cursor.fetchall()
        
        schedule = Schedule()
        
        for row in rows:
            appointment = Appointment(season = row['season'],
                                      weekday = row['weekday'],
                                      time = row['time'],
                                      location = locations.load(row['location_id']))
            appointment.ID = row['ROWID']
            appointment.location_id = row['location_id']
            appointment.person_id = row['person_id']
            schedule.add(appointment)
        
        return schedule
