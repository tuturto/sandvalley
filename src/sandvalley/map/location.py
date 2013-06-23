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
Module for locations
"""

class Location():
    """
    Location within town
    """
    def __init__(self):
        """
        Default constructor
        """
        self.ID = None
        self.location_name = None
        self.coordinates = None
        self.connections = []

    def __str__(self):
        """
        String representation of this location
        """
        return '{0}:{1}'.format(self.ID, self.location_name)

    def __repr__(self):
        """
        String representation of this location
        """
        return self.__str__()
