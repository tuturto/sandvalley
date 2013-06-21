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
Module for person builder
"""
from sandvalley.people import Person

class PersonBuilder():
    """
    Builder for persons
    """
    def __init__(self):
        """
        Default constructor
        """
        self.person_name = 'prototype'
        self.schedule = None
        
    def with_name(self, person_name):
        """
        Configure name of the person
        """
        self.person_name = person_name
        return self
    
    def with_schedule(self, schedule):
        """"
        Configure schedule
        """
        self.schedule = schedule
        return self

    def build(self):
        """
        Build a person
        """
        person = Person()
        person.person_name = self.person_name
        
        if self.schedule:
            person.schedule = self.schedule
        
        return person
