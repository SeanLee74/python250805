class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
def test_classes():
    # 1. Person 객체 생성 및 정보 출력
    p1 = Person(1, "홍길동")
    p1.printInfo()  # ID: 1, Name: 홍길동

    # 2. Manager 객체 생성 및 정보 출력
    m1 = Manager(2, "김철수", "팀장")
    m1.printInfo()  # ID: 2, Name: 김철수, Title: 팀장

    # 3. Employee 객체 생성 및 정보 출력
    e1 = Employee(3, "이영희", "Python")
    e1.printInfo()  # ID: 3, Name: 이영희, Skill: Python

    # 4. Person의 멤버 변수 확인
    assert p1.id == 1
    assert p1.name == "홍길동"

    # 5. Manager의 멤버 변수 확인
    assert m1.id == 2
    assert m1.name == "김철수"
    assert m1.title == "팀장"

    # 6. Employee의 멤버 변수 확인
    assert e1.id == 3
    assert e1.name == "이영희"
    assert e1.skill == "Python"

    # 7. Manager의 printInfo 오버라이드 확인
    import io, sys
    captured = io.StringIO()
    sys.stdout = captured
    m1.printInfo()
    sys.stdout = sys.__stdout__
    assert "Title: 팀장" in captured.getvalue()

    # 8. Employee의 printInfo 오버라이드 확인
    captured = io.StringIO()
    sys.stdout = captured
    e1.printInfo()
    sys.stdout = sys.__stdout__
    assert "Skill: Python" in captured.getvalue()

    # 9. Person의 printInfo 오버라이드 확인
    captured = io.StringIO()
    sys.stdout = captured
    p1.printInfo()
    sys.stdout = sys.__stdout__
    assert "Name: 홍길동" in captured.getvalue()

    # 10. 상속 관계 확인
    assert isinstance(m1, Person)
    assert isinstance(e1, Person)
    assert not isinstance(p1, Manager)
    assert not isinstance(p1, Employee)

if __name__ == "__main__":
    test_classes()
    print("모든 테스트를 통과하였습니다.")