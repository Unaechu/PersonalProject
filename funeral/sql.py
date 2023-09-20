import pymysql

db = pymysql.connect(host="localhost",
                     port=3306, user="root", passwd="1221", db="facilities", charset="utf8")
cursor = db.cursor()

def main():
    q = """SELECT * FROM funeral"""
    row_funeral_ids = cursor.execute(q)

    q = """SELECT * FROM funeral_facilities"""
    row_funeral_details = cursor.execute(q)


    sql = """
        UPDATE funeral a 
        inner join funeral_info b
        on a.장례식장명 = b.시설명
        SET b.info_id = a.id
        WHERE a.장례식장명 = b.시설명
        """
    cursor.execute(sql)
    print(cursor.fetchall())

    # UPDATE funeral a
    # inner join funeral_facilities b
    # on a.장례식장명 = b.장례식장명
    # SET b.facilities_id = a.id
    # WHERE a.장례식장명 = b.장례식장명
    db.commit()
    db.close()

    # funeral 테이블의 장례식장명과 funeral_facilites 테이블의 장례식이 일치한다면
    # funeral_facilites 테이블의 아이디 값을 funeral 테이블 기준으로 바꿔서 update query 날리기
if __name__ == '__main__':
    main()

def main():
    q = """
    select 시도, count(*) as cnt from funeral_info
    group by 시도
    having count(시도)>1;
    """
    a = cursor.execute(q)
    print(a)


if __name__ == '__main__':



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