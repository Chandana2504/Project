import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='chandana n',passwd='chandana@04')
mycursor=mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
