import pymysql as ps

conn = ps.Connect(host='localhost', user='root', passwd='1234',db='test')
curs = conn.cursor()


def get_sql(sql):
    curs.execute(sql)
    
def db_insert(sql):
    get_sql(sql)    # curs.execute(sql)
    conn.commit()
    
def db_select(sql):
    get_sql(sql)    # curs.execute(sql)
    return curs.fetchall()