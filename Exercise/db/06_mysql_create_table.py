import pymysql

conn = pymysql.connect(host='localhost', user='root', password = 'password',db= 'pubs', charset='utf8' )

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE5")
try:
    sql = """CREATE TABLE EMPLOYEE5 (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""

    cursor.execute(sql)
except:
    print("Error")

# disconnect from server
conn.close()