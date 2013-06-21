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
Module for schedules
"""

class Appointment():
    """
    Class for an appointment
    """
    def __init__(self, season, time, location):
        """
        Default constructor
        """
        super(Appointment, self).__init__()
        
        self.season = season
        self.time = time
        self.location = location

class Schedule():
    """
    Class to represent a schedule
    """
    def __init__(self):
        """
        Default constructor
        """
        super(Schedule, self).__init__()
        self.appointments = []
    
    def add(self, appointment):
        """
        Add an appointment
        """
        self.appointments.append(appointment)

    def get_appointment(self, season, time):
        """
        Get appointment
        """
        matches = [x for x in self.appointments
                   if x.season == season
                   and x.time == time]

        if len(matches):            
            return matches[0]

        matches = [x for x in self.appointments
                   if x.season == None
                   and x.time == None]

        if len(matches):            
            return matches[0]
