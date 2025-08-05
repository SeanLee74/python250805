# 개발자 클래스를 정의
class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def code(self):
        return f"{self.name} is coding in {self.language}."
    
#인스턴스를 2개 생성
dev1 = Developer("Alice", "Python")
dev2 = Developer("Bob", "Java")

#정보 출력
print(dev1.code())
print(dev2.code())