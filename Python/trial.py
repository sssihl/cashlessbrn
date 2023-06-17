import mysql.connector as sq

sql = sq.connect(host="localhost",
                                 user="root",
                                 password="sairam",
                                 database="cashless")
cursor = sql.cursor()
data = (16001,)
cursor.execute("SELECT balance FROM STUDENT_INFO WHERE id=%s", data)
name = cursor.fetchone()
print(name)