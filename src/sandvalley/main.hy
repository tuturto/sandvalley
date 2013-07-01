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

