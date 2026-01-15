# ✅ 6~36강 핵심 정리 (출력/자료형 ~ 함수 return)

# ---------------------------
# 6강 출력/자료형 + 형변환
print("hello")          # 문자열(str)
print(10)               # 정수(int)
print("안" + "녕")      # 문자열 연결
print(int("1") + int("2"))      # 문자열 -> 숫자
print(str(1) + str(1))          # 숫자 -> 문자열
print("1 + 2 = " + str(1 + 2))  # 숫자 결과를 문자열로 합치기

# 따옴표 출력
print("저는 '원성훈'입니다.")
print('저는 "원성훈"입니다.')

# 출력 포맷
print("{} + {} = {}".format(1, 2, 3))
print(f"{1} + {2} = {3}")       # f-string

# ---------------------------
# 7강 출력 반복
print("안녕하세요" * 10)         # 문자열 * n

# ---------------------------
# 8강 변수/타입
a = 10
a = a + 5
print(type(a))          # int
print(type(False))      # bool

age = 27
name = "원성훈"
print(f"제 나이는 {age}고, 이름은 {name}입니다.")

# ---------------------------
# 11강 연산자
print(10 / 3)   # 나눗셈(실수)
print(10 // 3)  # 몫(정수)
print(10 % 3)   # 나머지

# 비교/논리
print(3 != 1)                   # True/False
print(10 > 3 and 3 == 3)         # and
print(10 < 3 or 4 != 2)          # or
print(not False)                 # not
# 우선순위: 사칙 > 비교 > 논리

# ---------------------------
# 14강 if / elif / else
age = 20
if age > 20:
    print("21살 이상")
elif age < 20:
    print("미성년")
else:
    print("20살")

# ---------------------------
# 18강 match-case (여러 값 묶기)
month = 2
match month:
    case 12 | 1 | 2:
        season = "겨울"
    case 3 | 4 | 5:
        season = "봄"
    case 6 | 7 | 8:
        season = "여름"
    case _:
        season = "가을"
print(f"현재 계절은 {season}입니다.")

# ---------------------------
# 19강 while / break / continue
i = 10
while i >= 1:
    print(i)
    i -= 1

i = 1
while True:
    if i == 10:
        break
    i += 1

dan = 2
i = 1
while True:
    if i == 4:
        i += 1
        continue
    print(f"{dan} x {i} = {dan * i}")
    i += 1
    if i == 9:
        break

# ---------------------------
# 29강 함수(정의/호출)
def print_2_dan():
    dan = 2
    i = 1
    while i <= 9:
        print(f"{dan} x {i} = {dan * i}")
        i += 1

print_2_dan()

# ---------------------------
# 31강 매개변수(인자 받기)
def print_dan(dan, limit):
    while dan <= limit:
        num = 1
        while num <= 9:
            print(f"{dan} x {num} = {dan * num}")
            num += 1
        dan += 1

print_dan(3, 9)

# ---------------------------
# 35강 지역/전역/global
a = 20  # 전역변수

def add_one_global():
    global a     # 전역변수 수정 허용
    a += 1

# ---------------------------
# 36강 return (함수 결과값)
def func1():
    return 10

result = func1()   # result = 10

# -------------------------------------------------

# ✅ 리스트(List) 핵심 정리

# 1) 리스트는 "여러 값"을 한 번에 담는 자료형(객체)
ages = [10, 20, 30]

# 2) 리스트는 객체라서 "값"이 아니라 "주소(참조)"를 변수에 담는다.
a = []
b = []
# a와 b는 서로 다른 리스트(다른 객체)

b = a
# 이제 b는 a와 "같은 리스트"를 가리킨다(참조 공유)

a.append(10)
b.append(10)
print(a)  # [10, 10]  (같은 객체를 같이 수정했기 때문)

# -------------------------------------------------

# ✅ 리스트 기본 기능: 추가 / 삭제 / 수정
lst = [1, 2, 3, 4]

lst.append(5)        # 끝에 추가
lst.remove(4)        # 값 4 하나 삭제(앞에서부터 1개만)
del lst[0]           # 인덱스로 삭제
lst[0] = 100         # 인덱스로 수정

pos = lst.index(3)   # 값 3의 위치(인덱스) 찾기
size = len(lst)      # 길이(요소 개수)

# 정렬/뒤집기(원본 훼손)
lst.sort()           # 오름차순 정렬
lst.reverse()        # 순서 뒤집기

# 최솟값/최댓값
nums = [3, 1, 4, 1, 5, 9]
print(max(nums))     # 최댓값
print(min(nums))     # 최솟값

# -------------------------------------------------

# ✅ sorted(): 원본은 그대로, "정렬된 복사본" 반환
nums2 = [1, 2, 3, 4, 5]
rs = sorted(nums2, reverse=True)  # 내림차순 복사본
print(nums2)  # 원본 유지
print(rs)     # 정렬된 복사본

# -------------------------------------------------

# ✅ 슬라이싱(Slicing): "복사본"을 만들어 가져오기
a = [1,2,3,4,5,6,7,8,9,10]

a[1:3]    # 1번 인덱스부터 3번 전까지 -> [2,3]
a[:3]     # 처음부터 3번 전까지 -> [1,2,3]
a[1:5:2]  # 1~4까지, 2칸씩 -> [2,4]
a[2:]     # 2번부터 끝까지
a[:]      # 전체 복사
a[::-1]   # 전체 역순 복사





