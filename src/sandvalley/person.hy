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

(defn load-person [id])

(defn save-person [person connection]
  (try
    (let [[cursor (.cursor connection)]
          [params (, (get person "person-name") (get person "id"))]]
      (if (get person "id")
        (do
          (.execute cursor "update person set name=? where OID=?" params)
          (load-person (get person "id")))
        (load-person (do 
           .execute cursor "insert into person (name, OID) values (?, ?)" params)
          (.lastrowid cursor)))))
    (catch [e] (error-handling)))
)
