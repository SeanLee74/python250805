# demoClass.py

class Person:
    def __init__(self):
        self.name = "default name"

    def print(self):
        # print("My name is {0}".format(self.name)) # 예전 스타일
        print(f"My name is {self.name}") # 최근 코드 경향

p1 = Person()
p2 = Person()
p1.name = "전우치"
p1.print()
p2.print()

