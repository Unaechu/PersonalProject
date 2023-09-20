import tkinter
import tkinter.ttk
import pymysql

db = pymysql.connect(host="localhost",
                     port=3306, user="root", passwd="1221", db="facilities", charset="utf8")
cursor = db.cursor()

window = tkinter.Tk()
window.title("장례서비스 견적내기")
window.geometry("640x400+100+100")
window.resizable(True, True)

label = tkinter.Label(window, text= "a")
label.pack()
# funeral_info 테이블의 시도 컬럼 데이터 가져와 콤보박스 생성
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

states = [states_data]
combobox = tkinter.ttk.Combobox(window, height=15, values=states_data)
combobox.set("시도선택")
combobox.pack()


window.mainloop()


