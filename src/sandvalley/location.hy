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

(defn load-location [id connection]
  (let [[cursor (.cursor connection)]
        [params (, id)]]
    (do (.execute cursor "select OID, * from location where OID=?" params)
	(let [[row (.fetchone cursor)]]
	  (create-location-from-row row)))))

(defn save-location [location connection]
  (let [[cursor (.cursor connection)]
	[params (, (:name location) (:x-coordinate location) (:y-coordinate location) (:id location))]
	[location-id (:id location)]]
    (if location-id (do (.execute cursor "update location set name=?, x_coordinate=?, y_coordinate=? where OID=?" params)
		      (load-location location-id connection))
	(do (.execute cursor "insert into location (name, x_coordinate, y_coordinate, OID) values (?,?,?,?)" params)
	    (let [[new-location-id cursor.lastrowid]]
	      (load-location new-location-id connection))))))

(defn create-location-from-row [row]
  {:id (get row 0) 
   :name (get row 1)
   :x-coordinate (get row 2)
   :y-coordinate (get row 3)})
