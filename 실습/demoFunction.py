# demoFunction.py

#함수 정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("함수 내부:", x)

retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

result = swap(3,4)
print(result)

print("--함수 이름 해석")
x = 5
def func(a):
    return a+x

print(func(1))

def func2(a):
    x = 10
    return a+x

print(func2(1))

print("--기본값--")

def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "https://" + server + ":" + port
    return strURL

print(connectURI("multi.com","80"))
print(connectURI(port="80", server="test.com"))

g = lambda x,y:x*y
print(g(10,20), g(1,2))

urlTest = lambda port, server : "https://" + server + ":" + port

print(urlTest("naver.com","8080"))
print(urlTest(port="80", server="google.com"))