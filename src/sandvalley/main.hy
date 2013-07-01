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

(import [sandvalley.database.schema [create-schema]])
(import [sandvalley.person [load-person save-person]])
(import [sandvalley.tests.helpers [get-in-memory-connection]])

(defn create-database [connection]
  (create-schema connection))

(if (= __name__ "__main__")
  (let [[connection (get-in-memory-connection)]]
    (do (create-database connection)
      (save-person (dict {"id" None 
                          "name" "Jaska"}) connection))))

