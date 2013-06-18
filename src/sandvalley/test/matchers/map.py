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
Module for map related matchers
"""
from mockito.matchers import Matcher # pylint: disable=E0611

class HasLocationMatcher(Matcher):
    """
    Matcher to check if a location exists
    """
    def __init__(self, location):
        """
        Default constructor

        :param location: location to check
        :type location: Location
        """
        super(HasLocationMatcher, self).__init__()
        self.location = location

    def _matches(self, item):
        """
        Check if matcher matches item

        :param item: object to match against
        :returns: True if matching, otherwise False
        :rtype: Boolean
        """
        return False

    def describe_to(self, description):
        """
        Describe this matcher
        """
        description.append('Character who is dead')

    def describe_mismatch(self, item, mismatch_description):
        """
        Describe this mismatch
        """
        mismatch_description.append('Was character with {0} hit points'
                                    .format(0))

def has_location(location):
    return HasLocationMatcher(location)

