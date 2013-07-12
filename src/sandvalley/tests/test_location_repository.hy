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

(import [sandvalley.tests.helpers [get-in-memory-connection]])
(import [sandvalley.location [save-location load-location]])
(import [sandvalley.database.schema [create-schema]])
(import [hamcrest [assert-that is- equal-to]])

(defn test-save-location []
  (with [connection (create-schema (get-in-memory-connection))] 
	(let [[location {:id None :name "Gas station" :x-coordinate 0 :y-coordinate 0}]
	      [saved-location (save-location location connection)]
	      [loaded-location (load-location (:id saved-location) connection)]]
	  (assert-that (:name loaded-location) (is- (equal-to "Gas station"))))))
