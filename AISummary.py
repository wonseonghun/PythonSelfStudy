# ================================
# 파이썬 기초 요약(치트시트)
# ================================

# --------------------------------
# 1) 출력(print) + 자료형(type)
# --------------------------------
print("hello")  # 문자열(str)
print(10)  # 정수(int)

print("안" + "녕")  # 문자열 덧셈(이어붙이기)

# 형변환
print(int("1") + int("2"))  # 3  (문자열 -> 정수)
print(str(1) + str(1))  # "11" (정수 -> 문자열)

# 문자열 + 숫자 => 문자열로 변환 필요
print("1 + 2 = " + str(1 + 2))
print(f"1 + 2 = {1 + 2}")  # f-string (가장 자주 씀)

# 따옴표 출력
print("안녕하세요. 저는 '원성훈'입니다.")
print('안녕하세요. 저는 "원성훈"입니다.')

# format
print("{} + {} = {}".format(1, 2, 1 + 2))

# 타입 확인
a = 10
print(type(a))  # <class 'int'>
print(type(False))  # <class 'bool'>


# --------------------------------
# 2) 변수
# --------------------------------
a = 10
a = a + 5  # a += 5 도 가능

age = 27
name = "원성훈"
print(f"제 나이는 {age}고, 이름은 {name}입니다.")


# --------------------------------
# 3) 연산자
# --------------------------------
# 사칙연산
print(10 / 3)  # 3.333... (나눗셈, float)
print(10 // 3)  # 3        (몫의 정수 부분)
print(10 % 3)  # 1        (나머지)
print(2**3)  # 8        (제곱)

# 비교연산(결과는 True/False)
print(3 != 1)  # True  <- (원본 주석이 False였는데 실제는 True)

# 논리연산
print(10 > 3 and 3 == 3)  # True
print(10 < 3 or 4 != 2)  # True
print(not False)  # True

# 우선순위: 사칙 > 비교 > 논리


# --------------------------------
# 4) if 조건문
# --------------------------------
age = 20
if age > 20:
    print("21살 이상입니다.")
elif age < 20:
    print("미성년입니다.")
else:
    print("20살입니다.")


# --------------------------------
# 5) match-case (Python 3.10+)
# --------------------------------
month = 2

# 짧게: 여러 값을 한 번에
match month:
    case 12 | 1 | 2:
        season = "겨울"
    case 3 | 4 | 5:
        season = "봄"
    case 6 | 7 | 8:
        season = "여름"
    case 9 | 10 | 11:
        season = "가을"
    case _:
        season = "잘못된 월"

print(f"현재 계절은 {season}입니다.")

# ※ 주의: 문자열은 반드시 따옴표!
# season = 여름  (X) -> season = "여름" (O)


# --------------------------------
# 6) 반복문 while / for
# --------------------------------
# while: 조건이 True인 동안 반복
i = 10
while i >= 1:
    print(i)
    i -= 1

# break / continue
i = 1
while True:
    if i == 4:
        i += 1
        continue  # 아래를 건너뛰고 다음 반복
    print(i)
    if i == 10:
        break
    i += 1

# for: range 기반 반복(자주 씀)
for i in range(10):  # 0~9
    print(i)

for i in range(1, 14):  # 1~13
    print(i)

for i in range(2, 11, 2):  # 2,4,6,8,10
    print(i)

for i in range(10, 0, -1):  # 10~1
    print(i)


# --------------------------------
# 7) 함수(def) + 매개변수 + 리턴
# --------------------------------
def print_2_dan():
    dan = 2
    print(f"==={dan}단===")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")


print_2_dan()


# 매개변수(외부에서 값 넣어줌)
def print_dan(start, end):
    # start단부터 end단까지 출력
    for dan in range(start, end + 1):
        print(f"==== {dan}단 ====")
        for num in range(1, 10):
            print(f"{dan} x {num} = {dan * num}")


print_dan(3, 9)


# return: 함수 실행 결과를 밖으로 돌려줌
def func1():
    return 10


x = func1()
print(x)


# --------------------------------
# 8) 지역변수 / 전역변수 / global(비추)
# --------------------------------
a = 20  # 전역변수


def add_local():
    a = 0  # 지역변수(함수 안에서 새로 만든 a)
    a += 1
    return a


def add_global():
    global a  # 전역 a를 수정하겠다는 선언(가능은 하지만 보통 지양)
    a += 1


print(add_local())  # 1
add_global()
print(a)  # 21


# --------------------------------
# 9) 리스트(list) 기본
# --------------------------------
nums = [1, 2, 3, 4]
nums.append(5)  # 끝에 추가
nums.remove(2)  # 값 2를 "한 개" 삭제
del nums[0]  # 인덱스로 삭제
nums[0] = 100  # 수정

print(len(nums))  # 길이
print(min(nums), max(nums))

# 정렬/뒤집기(원본 변경됨)
nums.sort()
nums.reverse()

# sorted(): 원본 유지 + 새 리스트 반환
nums2 = [3, 1, 4]
rs = sorted(nums2)  # 오름차순
rs_desc = sorted(nums2, reverse=True)
print(nums2, rs, rs_desc)


# --------------------------------
# 10) 리스트 슬라이싱
# --------------------------------
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[1:3])  # [2,3]  (1~(3-1))
print(a[:3])  # [1,2,3]
print(a[1:5:2])  # [2,4]
print(a[2:])  # [3,4,5,6,7,8,9,10]
print(a[:])  # 복사본
print(a[::-1])  # 역순 복사본


# --------------------------------
# 11) input / strip / split / map (실전 조합)
# --------------------------------
# input(): 무조건 문자열로 들어옴
# strip(): 양끝 공백 제거
# split(): 문자열을 나눠 리스트로
# map(): 각 요소에 함수 적용(형변환)

# 정수 1개
# n = int(input().strip())

# 정수 2개(공백 구분)
# x, y = map(int, input().split())

# 정수 여러 개(공백 구분)
# arr = list(map(int, input().split()))

# 쉼표 구분
# arr = list(map(int, input().strip().split(",")))


# --------------------------------
# 12) 딕셔너리(dict) = key:value
# --------------------------------
ages = {"철수": 10, "유리": 20, "짱구": 30}
ages["맹구"] = 40  # 추가
ages["유리"] = 21  # 수정
del ages["짱구"]  # 삭제

# 존재 확인
print("철수" in ages)  # True/False

# 반복(자주 쓰는 3가지)
for k in ages.keys():
    print(k, ages[k])

for v in ages.values():
    print(v)

for k, v in ages.items():
    print(k, v)


# --------------------------------
# 13) 클래스(class) + 생성자 + __str__
# --------------------------------
class Person:
    def __init__(self, name, age, home, hobby):
        self.name = name
        self.age = age
        self.home = home
        self.hobby = hobby

    def __str__(self):
        # print(객체) 할 때 보기 좋게 출력됨
        return f"name:{self.name}, age:{self.age}, home:{self.home}, hobby:{self.hobby}"

    def introduce(self):
        print(
            f"저는 {self.home} 사는 {self.age}살, 취미는 {self.hobby}인 {self.name}입니다."
        )


p1 = Person("홍길동", 23, "안산", "테니스")
p2 = Person("김철수", 30, "서울", "축구")

p1.introduce()
p2.introduce()
print(p1)  # __str__ 덕분에 "주소"가 아니라 내용이 출력됨
