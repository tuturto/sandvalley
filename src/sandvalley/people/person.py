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
Module for persons
"""

from .schedule import Schedule

class Person():
    """
    Person
    """
    def __init__(self):
        """
        Default constructor
        """
        self.ID = None
        self.person_name = None
        self.schedule = Schedule()
    
    def get_appointment(self, season, weekday, time):
        """
        Get appointment
        """
        return self.schedule.get_appointment(season = season,
                                             weekday = weekday,
                                             time = time)
