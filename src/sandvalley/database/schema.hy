;; -*- coding: utf-8 -*-
;;
;;   Copyright 2013 Tuukka Turto
;;
;;   This file is part of Sand Valley.
;;
;;   Sand Valley is free software: you can redistribute it and/or modify
;;   it under the terms of the GNU General Public License as published by
;;   the Free Software Foundation, either version 3 of the License, or
;;   (at your option) any later version.
;;
;;   Sand Valley is distributed in the hope that it will be useful,
;;   but WITHOUT ANY WARRANTY; without even the implied warranty of
;;   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;;   GNU General Public License for more details.
;;
;;   You should have received a copy of the GNU General Public License
;;   along with Sand Valley.  If not, see <http://www.gnu.org/licenses/>.

(defn create-schema [connection]
  (.execute connection "create table location (name text not null, x_coordinate integer not null, y_coordinate integer not null)")
  (.execute connection "create table person (name text not null)")
  (.execute connection "create table appointment (person_id integer not null, location_id integer not null, season integer, weekday integer, time integer, foreign key(person_id) references person(OID), foreign key(location_id) references location(OID))")
  (.execute connection "create table connection (name text not null, location1_id integer not null, location2_id integer not null, foreign key(location1_id) references location(OID), foreign key(location2_id) references location(OID))")
  (.commit connection))

