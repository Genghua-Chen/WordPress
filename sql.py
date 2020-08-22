import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="database-2.crlv16tsuwz8.us-east-1.rds.amazonaws.com",
  user="genghua",
  password="fl3166006",
  database="Genghua"
)

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t',1)


    mycursor = mydb.cursor()

    sql = "INSERT INTO WordPress (Word, Count) VALUES ('{}',{})".format(word, count)

    mycursor.execute(sql)

    mydb.commit()