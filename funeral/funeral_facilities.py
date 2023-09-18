import pymysql

db = pymysql.connect(host="database-1.c96y4v8xbpbh.ap-northeast-2.rds.amazonaws.com",
                     port=3306, user="admin", passwd="zofhfl6655", db="facilities", charset="utf8")
cursor = db.cursor()

def main():
    try:
        q = """SELECT * FROM funeral"""
        cursor.execute(q)
        row_funeral_ids = cursor.fetchall()

        q = """SELECT * FROM funeral_facilities"""
        cursor.execute(q)
        row_funeral_details = cursor.fetchall()

#       q = """SELECT * FROM funeral_info"""
#       row_funeral_infos = cursor.execute(q)

        sql = """
            UPDATE funeral_facilities
            JOIN funeral ON funeral_facilities.장례식장명 = funeral.장례식장명
            SET funeral_facilities.id = funeral.id
            """
        cursor.execute(sql)
        db.commit()
        print("업데이트가 성공적으로 수행되었습니다.")

    except Exception as e:
        db.rollback()
        print("업데이트 중 오류가 발생하였습니다:", str(e))

    finally:
        db.close()

    # funeral 테이블의 장례식장명과 funeral_facilites 테이블의 장례식이 일치한다면
    # funeral_facilites 테이블의 아이디 값을 funeral 테이블 기준으로 바꿔서 update query 날리기

if __name__ == '__main__':
    main()

