# insert, update, delete

insert_query = "INSERT INTO student (student_id, student_name) VALUES (104, 'Kim');"
update_query = "UPDATE student SET student_name = 'David' WHERE student_id = 104;"
delete_query = "DELETE FROM student WHERE student_id = 104;"
import mysql.connector

try:
    con = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="root", database="mydatabase")
    curs = con.cursor()  # create cursor
    curs.execute(insert_query)  # execute query through cursor
    con.commit()  # commit transaction
    con.close()  # close the connection
except:
    print("Connection unsuccessful established...")

print("Finished...")
