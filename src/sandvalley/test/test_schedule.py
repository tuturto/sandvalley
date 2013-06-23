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
Module for testing schedules
"""
from sandvalley.test.builders import PersonBuilder, ScheduleBuilder
from sandvalley.test.builders import LocationBuilder

from hamcrest import assert_that, is_, equal_to

class TestSchedule():
    """
    Tests for scheduling
    """
    def __init__(self):
        """
        Default constructor
        """
        super(TestSchedule, self).__init__()
    
    def test_getting_general_appointment(self):
        """
        If there are no specific appointments a general one is used
        """
        location = LocationBuilder().build()
        
        schedule = (ScheduleBuilder()
                        .with_appointment(season = None,
                                          weekday = None,
                                          time = None,
                                          location = location)
                        .build())
                        
        person = (PersonBuilder()
                        .with_schedule(schedule)
                        .build())
        
        appointment = person.get_appointment(season = 'summer',
                                             weekday = 'tuesday',
                                             time = 'evening')
                                             
        assert_that(appointment.location, is_(equal_to(location)))

    def test_getting_very_specific_appointment(self):
        """
        If an appointment in schedule matches completely, it should be returned
        """
        home = (LocationBuilder()
                    .with_name('home')
                    .build())
        summer_house = (LocationBuilder()
                            .with_name('summer house')
                            .build())
        
        schedule = (ScheduleBuilder()
                        .with_appointment(season = None,
                                          weekday = None,
                                          time = None,
                                          location = home)
                        .with_appointment(season = 'summer',
                                          weekday = 'monday',
                                          time = 'day',
                                          location = summer_house)
                        .build())
                        
        person = (PersonBuilder()
                        .with_schedule(schedule)
                        .build())
        
        appointment = person.get_appointment(season = 'summer',
                                             weekday = 'monday',
                                             time = 'day')
                                             
        assert_that(appointment.location, is_(equal_to(summer_house)))

    def test_getting_very_appointment_by_time(self):
        """
        If no appointment matches completely, the one that matches by time should be returned
        """
        home = (LocationBuilder()
                    .with_name('home')
                    .build())
        summer_house = (LocationBuilder()
                            .with_name('summer house')
                            .build())
        
        schedule = (ScheduleBuilder()
                        .with_appointment(season = None,
                                          weekday = None,
                                          time = 'day',
                                          location = home)
                        .with_appointment(season = 'summer',
                                          weekday = None,
                                          time = 'day',
                                          location = summer_house)
                        .build())
                        
        person = (PersonBuilder()
                        .with_schedule(schedule)
                        .build())
        
        appointment = person.get_appointment(season = 'winter',
                                             weekday = 'sunday',
                                             time = 'day')
                                             
        assert_that(appointment.location, is_(equal_to(home)))