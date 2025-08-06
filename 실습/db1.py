# db1.py
import sqlite3

#연결객체를 리턴 (메모리 임시)
#con = sqlite3.connect(':memory:')

# 연결객체를 리턴 (파일로 저장)
con = sqlite3.connect(r"c:\work\sample.db")

# 커서 객체를 생성
cur = con.cursor()
# 테이블 생성
cur.execute("create table PHONEBOOK (NAME text, PHONE text);")
# 데이터 삽입
cur.execute("insert into PHONEBOOK values ('홍길동', '010-1234-5678');")
# 입력 파라미터 처리
name = '이순신'
phone = '010-8765-4321'
cur.execute("insert into PHONEBOOK values (?, ?);", (name, phone))
# 여러건 입력
datalist = ("강감찬", "010-1111-2222"), ("세종대왕", "010-3333-4444")
cur.executemany("insert into PHONEBOOK values (?, ?);", datalist)

con.commit()  # 변경사항 저장

# 데이터 조회
cur.execute("select * from PHONEBOOK")
# 결과를 가져오기
for row in cur:
    print(row)
