(import [sandvalley.database.schema [create-schema]])
(import sqlite3)

(defn create-database []
  (let [[connection (.connect sqlite3 ":memory:")]]
    (setv connection.row-factory sqlite3.Row)
    (setv connection.isolation-level None)
    (create-schema connection)))

(if (= __name__ "__main__")
  (create-database))

