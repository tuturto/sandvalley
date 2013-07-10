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

(defn load-person [id connection]
  (let [[cursor (.cursor connection)]
        [params (, id)]]
    (do (.execute cursor "select OID, * from person where OID=?" params)
	(let [[row (.fetchone cursor)]]
	  (create-person-from-row row)))))

(defn save-person [person connection]
  (let [[cursor (.cursor connection)]
	[params (, (:name person) (:id person))]
	[person-id (:id person)]]
    (if person-id (do (.execute cursor "update person set name=? where OID=?" params)
		      (load-person person-id connection))
	(do (.execute cursor "insert into person (name, OID) values (?, ?)" params)
	    (let [[new-person-id cursor.lastrowid]]
	      (load-person new-person-id connection))))))

(defn create-person-from-row [row]
  {:id (get row 0) 
   :name (get row 1)})

