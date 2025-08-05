# demoDict.py

print("~~형식변환~~")
a = set((1,2,3))
print(a)
b = list(a)
b.append(10)
print(b)
c = tuple(b)
print(c)

print("--dict--")
colors = {"apple":"red", "banana":"yellow"}
colors["cherry"] = "red"
print(colors)

print(colors["apple"])

del colors["apple"]
print(colors)

#장비
device = {"아이폰":5, "아이패드":10, "윈도우타블렛":15}
device["맥북"] = 20
print(device)

del device["맥북"]
print(device)

for item in device.items():
    print(item)

for k,v in device.items():
    print(k, v)

