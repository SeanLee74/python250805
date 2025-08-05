# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    # 생성자 메소드
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
        
    # 잔액을 초기화하는 생성자            
    def deposit(self, amount):
        self.__balance += amount 
    
    # 잔액을 반환하는 메소드
    def withdraw(self, amount):
        self.__balance -= amount
    
    # 잔액을 반환하는 메소드
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)

#print(account1.__balance)
