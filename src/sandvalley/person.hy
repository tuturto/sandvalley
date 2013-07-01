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
    (do
      (.execute cursor "select OID, * from person where OID=?" params)
      (let [[row (.fetchone cursor)]]
        (create-person-from-row row)))))

(defn save-person [person connection]
    (let [[cursor (.cursor connection)]
          [params (, (get person "name") (get person "id"))]
          [person-id (get person "id")]]
      (try 
        (if person-id
          (do 
            (.execute cursor "savepoint personsave")
            (.execute cursor "update person set name=? where OID=?" params)
            (.execute cursor "release personsave")
            (load-person person-id connection))
          (do 
            (.execute cursor "savepoint personsave")
            (.execute cursor "insert into person (name, OID) values (?, ?)" params)
            (.execute cursor "release personsave")
            (load-person cursor.lastrowid connection)))
      (catch [e Exception] (do
        (.execute cursor "rollback to personsave")
        (raise))))))

(defn create-person-from-row [row]
  (dict {"id" (get row 0) 
         "name" (get row 1)}))

