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
Tests for time
"""

from sandvalley.simulation import Time

from hamcrest import assert_that, is_, equal_to

class TestTime():
    """
    Tests for time
    """
    def __init__(self):
        """
        Default constructor
        """
        super(TestTime, self).__init__()
    
    def test_next_time_of_day(self):
        """
        Test moving to next time of day
        """
        time = Time(day = 1,
                    month = 'january',
                    day_of_week = 'monday',
                    time_of_day = 'day')

        new_time = time.add_time()
        
        assert_that(new_time.time_of_day, is_(equal_to('evening')))

    def test_next_day(self):
        """
        Test moving to next day
        """
        time = Time(day = 1,
                    month = 'january',
                    day_of_week = 'monday',
                    time_of_day = 'night')

        new_time = time.add_time()

        assert_that(new_time.time_of_day, is_(equal_to('day')))
        assert_that(new_time.day, is_(equal_to(2)))

    def test_next_month(self):
        """
        Test moving to next month
        """
        time = Time(day = 31,
                    month = 'january',
                    day_of_week = 'monday',
                    time_of_day = 'night')

        new_time = time.add_time()
        assert_that(new_time.day, is_(equal_to(1)))
        assert_that(new_time.month, is_(equal_to('february')))
