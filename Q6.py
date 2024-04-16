import pymysql as ps
db=ps.connect(host='localhost', user = 'root', passwd= '1234', db='test')
curs=db.cursor()
sql = 'select * from test'
curs.execute(sql)
result=curs.fetchall()
print(result)