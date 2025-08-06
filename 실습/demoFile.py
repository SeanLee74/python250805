# demoFile.py

#파일쓰기
f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일읽기
f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
print(f.read())
f.close()

#파일읽기 (한줄씩)
f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    print(line.strip())
f.close()

#파일읽기 (raw string notation)
f = open(r"c:\work\test.txt", "rt", encoding="utf-8")
print(f.read())
f.close()