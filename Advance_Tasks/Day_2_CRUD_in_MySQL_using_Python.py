import mysql.connector

cnx = mysql.connector.connect(user='yash', password='Miteswati@9', host='localhost', database='example', auth_plugin='mysql_native_password')
cursor = cnx.cursor()

# CREATE OPERATIONS
# cursor.execute("CREATE DATABASE example")
cursor.execute("USE example")
cursor.execute("DROP TABLE INTERNS")
cursor.execute("CREATE TABLE INTERNS(ID INT, NAME VARCHAR(10), COLLEGE VARCHAR(20))")
cursor.execute("INSERT INTO INTERNS VALUES(1, 'YASH', 'CHARUSAT')")
cursor.execute("INSERT INTO INTERNS VALUES(2, 'TANMAY', 'VGEC')")
cursor.execute("INSERT INTO INTERNS VALUES(3, 'YUG', 'SVIT')")

# READ OPERATIONS
print("Data at Starting...")
cursor.execute("SELECT * FROM INTERNS")

for a, b, c in cursor:
	print(a, b, c)

print("\nData after Updating...")
# UPDATE OPERATIONS
cursor.execute("UPDATE INTERNS SET NAME='DEEP' WHERE ID=3")
cursor.execute("SELECT * FROM INTERNS")
for a, b, c in cursor:
	print(a, b, c)

print("\nData after Deleting...")
# DELETE OPERATIONS
cursor.execute("DELETE FROM INTERNS WHERE ID=3")
cursor.execute("SELECT * FROM INTERNS")
for a, b, c in cursor:
	print(a, b, c)

cursor.close()
cnx.close()
