# select

import mysql.connector

try:
    con = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="root", database="mydatabase")
    curs = con.cursor() # create cursor
    curs.execute("SELECT * FROM student") # execute query through cursor
    for row in curs:
        print(row[0],row[1])
    con.close() # close the connection
except:
    print("Connection unsuccessful established...")

print("Finished...")