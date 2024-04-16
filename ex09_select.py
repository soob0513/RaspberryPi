# select라는 모듈 만들기 
import databas as db

def select_db():
    sql = 'select * from sensordb'
    result = db.db_select(sql)     # result는 이중튜플 형태
    r = '<br>'.join(map(str, result))
    # print(r)
    return r
    
select_db()

# join, map 사용

# for s, t in result :
#     print('sensing : {} / ts : {}'.format(s,t))