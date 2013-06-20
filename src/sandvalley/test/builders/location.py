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
Module for location builder
"""
from sandvalley.map import Location

class LocationBuilder():
    """
    Builder for locations
    """
    def __init__(self):
        """
        Default constructor
        """
        self.location_name = 'prototype'
        
    def with_name(self, location_name):
        """
        Configure name of the location
        """
        self.location_name = location_name
        return self

    def build(self):
        """
        Build a location
        """
        location = Location()
        location.location_name = self.location_name
        
        return location
