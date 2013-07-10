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
(import [sandvalley.person [save-person load-person]])
(import [sandvalley.database.schema [create-schema]])
(import [hamcrest [assert-that is- equal-to]])

(defn test-save-person []
  (with [connection (create-schema (get-in-memory-connection))] 
	(let [[person {:id None :name "Pete"}]
	      [saved-person (save-person person connection)]
	      [loaded-person (load-person (:id saved-person) connection)]]
	  (assert-that (:name loaded-person) (is- (equal-to "Pete"))))))

(defn test-update-person []
  (with [connection (create-schema (get-in-memory-connection))]
	(let [[person {:id None :name "Pete"}]
	      [saved-person (save-person person connection)]
	      [loaded-person (load-person (:id saved-person) connection)]]
	  (assoc loaded-person :name "Uglak")
	  (save-person loaded-person connection)
	  (let [[updated-person (load-person (:id saved-person) connection)]]
	    (assert-that (:name updated-person) (is- (equal-to "Uglak")))))))

