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


