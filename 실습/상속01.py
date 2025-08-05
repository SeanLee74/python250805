class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        super().__init__(name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    #def printInfo(self):
    #    super().printInfo()
    #    print("Student Info(Subject: {0}, Student ID: {1})".format(self.subject, self.studentID))

    def printInfo(self):
        print("Info(이름: {0}, 전화번호: {1})".format(self.subject, self.studentID))
        print("Info(학과: {0}, 학생ID: {1})".format(self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "24001")
print(p.__dict__)
print(s.__dict__)

p.printInfo()
s.printInfo()