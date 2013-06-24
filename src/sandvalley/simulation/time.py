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
Module for time related objects
"""

class Time():
    """
    Class to represent time
    """
    def __init__(self, day, month, day_of_week, time_of_day):
        """
        Default constructor
        """
        super(Time, self).__init__()

        self.day = day
        self.month = month
        self.day_of_week = day_of_week
        self.time_of_day = time_of_day

    def next_day(self):
        """
        Move to next day
        """
        new_time = Time(day = self.day + 1, 
                        month = self.month, 
                        day_of_week = self.day_of_week, 
                        time_of_day = self.time_of_day)

        return new_time
