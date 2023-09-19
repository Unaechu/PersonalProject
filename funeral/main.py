import pymysql

db = pymysql.connect(host="localhost",
                     port=3306, user="root", passwd="1221", db="facilities", charset="utf8")
cursor = db.cursor()
def states():
    q = """select distinct 시도
    from funeral_info;
    """
    cursor.execute(q)
    _do = cursor.fetchall()
    for s in _do:
        print(s[0])

    q = """select * from funeral_info
    where 시도 like '서울%';"""
    cursor.execute(q)
    gg = cursor.fetchall()
    print(gg)

    q = """select * from funeral_info
    inner join funeral_facilities
    on funeral_info.시설명 = funeral_facilities.장례식장명
    where 시설명 like '국립중앙%';"""
    cursor.execute(q)
    _f = cursor.fetchall()
    print(_f)

    db.commit()
    db.close()

if __name__ == '__main__':
    states()
