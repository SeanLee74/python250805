# 자료형 정의
my_list = [1, 2, 2, 3]
my_set = {1, 2, 2, 3}
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_tuple = (1, 2, 2, 3)

# 각 자료형 출력
print("List:", my_list)     # 중복 허용, 순서 유지
print("Set:", my_set)       # 중복 허용 X, 순서 없음
print("Dict:", my_dict)     # 키-값 쌍, 순서 유지 (Python 3.7+)
print("Tuple:", my_tuple)   # 중복 허용, 순서 유지, 불변

# 가변성 테스트
print("\n[가변성 테스트]")
try:
    my_list[0] = 100
    print("List 수정 가능:", my_list)
except Exception as e:
    print("List 수정 불가:", e)

try:
    my_tuple[0] = 100
    print("Tuple 수정 가능:", my_tuple)
except Exception as e:
    print("Tuple 수정 불가:", e)

try:
    my_set.add(4)
    print("Set 수정 가능 (요소 추가):", my_set)
except Exception as e:
    print("Set 수정 불가:", e)

try:
    my_dict['d'] = 4
    print("Dict 수정 가능 (키 추가):", my_dict)
except Exception as e:
    print("Dict 수정 불가:", e)

# 요소 접근 방법
print("\n[요소 접근]")
print("List[1]:", my_list[1])
print("Tuple[1]:", my_tuple[1])
print("Dict['b']:", my_dict['b'])
print("Set은 인덱싱 불가 - 예시 생략")

# 반복문 비교
print("\n[반복문 예시]")
print("List 반복:", [x for x in my_list])
print("Set 반복:", [x for x in my_set])
print("Dict 키 반복:", [k for k in my_dict])
print("Tuple 반복:", [x for x in my_tuple])
