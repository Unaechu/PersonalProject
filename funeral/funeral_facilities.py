import pymysql
db = pymysql.connect(host="database-1.c96y4v8xbpbh.ap-northeast-2.rds.amazonaws.com",
                     port=3306, user="admin", passwd="zofhfl6655", db="facilities", charset="utf8")
cursor= db.cursor()

def main():
    q = """SELECT * FROM funeral"""
    row_funeral_ids = cursor.execute(q)

    q = """SELECT * FROM funeral_facilities"""
    row_funeral_details = cursor.execute(q)

#    q = """SELECT * FROM funeral_info"""
#    row_funeral_infos = cursor.excute(q)

    q = """SELECT * FROM funeral_facilities WHERE 장례식장명 (SELECT 장례식장명 FROM funeral)
    ALTER TABLE funeral_facilities UPDATE id REFERENCES funeral(id)"""
    column_funeral_facilities = cursor.execute(q)

#    q = """SELECT * FROM funeral_info WHERE 시설명 (SELECT 장례식장명 FROM funeral)
#    ALTER TABLE funeral_info UPDATE id REFERENCES funeral(id)"""
#    column_funeral_info = cursor.execute(q)

    # funeral 테이블의 장례식장명과 funeral_facilites 테이블의 장례식이 일치한다면
    # funeral_facilites 테이블의 아이디 값을 funeral 테이블 기준으로 바꿔서 update query 날리기
if __name__ == '__main__':
    main()


