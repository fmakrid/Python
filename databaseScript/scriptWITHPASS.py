import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="noobaki32",
    database="covid19"
)

mycursor = mydb.cursor()

sql = 'UPDATE covid19 SET deathpop = cases/population WHERE id>0;'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
