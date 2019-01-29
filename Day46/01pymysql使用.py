import pymysql

conn = pymysql.connect(host="localhost", user="root", password="zhang6882051", database="exercise")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
unm = input("请输入用户名：")
pwd = input("请输入密码：")
sql = "insert into userinfo(username, password) values(%s, %s)"
# sql = "select * from userinfo"
cursor.execute(sql, (unm, pwd))
conn.commit()
# cursor.execute(sql)
# result = cursor.fetchall()
cursor.close()
conn.close()
# if result:
#     print("Successfully!")
# else:
#     print("Error!")
