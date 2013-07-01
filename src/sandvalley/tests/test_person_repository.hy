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
  (let [[person (dict {"id" None "name" "Pete"})]
        [connection (get-in-memory-connection)]]
    (do (create-schema connection)
      (let [[saved-person (save-person person connection)]
            [loaded-person (load-person (get saved-person "id") connection)]]
        (assert-that (get loaded-person "name") (is- (equal-to "Pete")))))))

(if (= __name__ "__main__")
  (test-save-person))

