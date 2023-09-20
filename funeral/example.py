import pymysql

db = pymysql.connect(host="localhost",
                     port=3306, user="root", passwd="1221", db="facilities", charset="utf8")
cursor = db.cursor()

def states():
    q = """select distinct 시도
    from funeral_info
    order by 시도 asc;
    """
    cursor.execute(q)
    _do = [s[0] for s in cursor.fetchall()]
    return _do

    db.close()

if __name__ == '__main__':
    states_data = states()
    for s in states_data:
        print(s)


