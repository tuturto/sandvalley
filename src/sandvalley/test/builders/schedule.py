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
Module for building schedules
"""
from sandvalley.people.schedule import Appointment, Schedule

class ScheduleBuilder():
    """
    Builder for schedules
    """
    def __init__(self):
        """
        Default constructor
        """
        super(ScheduleBuilder, self).__init__()
        self.appointments = []

    def with_appointment(self, season, time, weekday, location):
        """
        Configure an appointment
        """
        self.appointments.append(Appointment(season = season,
                                             weekday = weekday,
                                             time = time, 
                                             location = location))
        return self

    def build(self):
        """
        Build the schedule
        """
        schedule = Schedule()

        for appointment in self.appointments:
            schedule.add(appointment)

        return schedule
