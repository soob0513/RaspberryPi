import spidevRead as sr
import pymysql as ps
import time
import databas as db

read = sr.analog_read(0)
print(f'Data:{read}')

# conn = ps.connect(host='localhost', user = 'root', passwd= '1234', db='test')
# curs = conn.cursor()
sql = f'insert into sensordb(sensing) values({read})'
# curs.execute(sql)
# conn.commit()
db.db_insert(sql)