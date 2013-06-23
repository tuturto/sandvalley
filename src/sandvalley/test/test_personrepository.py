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
Tests for person repository
"""

from sandvalley.people import PersonRepository
from sandvalley.map import MapRepository
from sandvalley.database import create_schema
import sqlite3

from sandvalley.test.builders import PersonBuilder, LocationBuilder
from sandvalley.test.builders import ScheduleBuilder, ConnectionBuilder
from sandvalley.test.builders import MapBuilder
from hamcrest import assert_that, is_, equal_to

class TestPersonRepository():
    """
    Test person repository
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
        Test that a person can be saved and loaded
        """
        person = PersonBuilder().build()
        
        repository = PersonRepository(self.connection)
        
        person = repository.save(person)
        loaded_person = repository.load(person.ID)
        
        assert_that(loaded_person.ID, is_(equal_to(person.ID)))
        assert_that(loaded_person.person_name, 
                    is_(equal_to(person.person_name)))

    def test_updating_person(self):
        """
        Test that saved person can be updated
        """
        person = (PersonBuilder()
                        .with_name('Jason')
                        .build())
                        
        repository = PersonRepository(self.connection)        
        person = repository.save(person)

        person.person_name = 'Peter'
        person = repository.save(person)
        
        loaded_person = repository.load(person.ID)
        assert_that(loaded_person.person_name, 
                    is_(equal_to('Peter')))

    def test_saving_schedule(self):
        """
        Schedule should be saved with the person
        """
        map_repository = MapRepository(self.connection)        
        repository = PersonRepository(self.connection)
        
        home = (LocationBuilder()
                    .with_name('home')
                    .build())
        station = (LocationBuilder()
                    .with_name('station')
                    .build())
        path = (ConnectionBuilder()
                        .with_name('path')
                        .with_start(station)
                        .with_end(home)
                        .build())
        town_map = (MapBuilder()
                    .with_location(station)
                    .with_location(home)
                    .with_connection(path)
                    .build())

        map_repository.save(town_map)

        schedule = (ScheduleBuilder()
                        .with_appointment(season = None,
                                          time = 'night',
                                          weekday = None,
                                          location = home)
                        .with_appointment(season = 'summer',
                                          time = 'day',
                                          weekday = 'monday',
                                          location = station))
        person = (PersonBuilder()
                    .with_schedule(schedule)
                    .build())
        
        person = repository.save(person)
        loaded_person = repository.load(person.ID)

        night_appointment = loaded_person.get_appointment(season = 'summer',
                                                          time = 'night',
                                                          weekday = 'monday')
        assert_that(night_appointment.location.location_name,
                    is_(equal_to('home')))

        day_appointment = loaded_person.get_appointment(season = 'summer',
                                                        time = 'day',
                                                        weekday = 'monday')
        assert_that(day_appointment.location.location_name,
                    is_(equal_to('station')))
