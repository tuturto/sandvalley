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

        self.times_of_day = ['day', 
                             'evening', 
                             'night']

        self.weekdays = ['monday', 
                         'tuesday', 
                         'wednesday', 
                         'thursday', 
                         'friday', 
                         'saturday', 
                         'sunday']

        self.months = ['january', 
                       'february', 
                       'march', 
                       'april', 
                       'may', 
                       'june', 
                       'july', 
                       'august', 
                       'september', 
                       'october', 
                       'november', 
                       'december']

        self.days_in_month = {'january': 31,
                              'february': 28, 
                              'march': 31, 
                              'april': 30, 
                              'may': 31, 
                              'june': 30, 
                              'july': 31, 
                              'august': 31, 
                              'september': 30, 
                              'october': 31, 
                              'november': 30, 
                              'december': 31}

    def add_time(self):
        """
        Move to next moment in time
        """
        new_time_of_day = self.times_of_day.index(self.time_of_day) + 1
        new_day = self.day
        new_day_of_week = self.day_of_week
        
        if new_time_of_day >= len(self.times_of_day):
            new_time_of_day = 0
            new_day = new_day + 1
            if self.weekdays.index(self.day_of_week) + 1 >= len(self.weekdays):
                new_day_of_week = 'monday'
            else:
                new_day_of_week = self.weekdays[self.weekdays.index(self.day_of_week) + 1]
        
        days_in_month = self.days_in_month[self.month]
        
        if new_day > days_in_month:
            new_day = 1
            if self.months.index(self.month) + 1 >= len(self.months):
                new_month = 'january'
            else:
                new_month = self.months[self.months.index(self.month) + 1]
        else:
            new_month = self.month
        
        new_time = Time(day = new_day,
                        month = new_month,
                        day_of_week = new_day_of_week,
                        time_of_day = self.times_of_day[new_time_of_day])

        return new_time
