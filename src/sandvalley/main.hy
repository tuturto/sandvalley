(import [sandvalley.database.schema [create-schema]])
(import [sandvalley.person [load-person save-person]])
(import sqlite3)

(defn create-connection []
  (do 
    (let [[connection (.connect sqlite3 ":memory:")]]
      (setv connection.row-factory sqlite3.Row)
      (setv connection.isolation-level None)
    (get [connection] 0))))

(defn create-database [connection]
  (create-schema connection))

(if (= __name__ "__main__")
  (let [[connection (create-connection)]]
    (do (create-database connection)
      (save-person (dict {"id" None 
                          "name" "Jaska"}) connection))))

