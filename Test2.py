"""
# ----------------- 리스트에 순서대로 2,1,5,6,7을 한번에 담아주세요.
TestList = []
# TestList.append(2,1,5,6,7), 한번에 안됨.

TestList = [2, 1, 5, 6, 7]  # 그냥 이거네 ㅋㅋㅋ
print(TestList)

# ------------------ 평일을 한번에 & 토,일을 순서대로 추가
week = ["월", "화", "수", "목", "금"]  # ""을 꼭 써줘야 하네.
week.append("토")
week.append("일")

print(week)


# ------------------두 개의 리스트 합치기

week = ["월", "화", "수", "목", "금"]
weekend = ["토", "일"]
print(week + weekend)  # 그냥 더하기가 된다., 순서대로 추가해야함.

# ------------------가장 처음 요소를 출력하기
print(week[0])


# ------------------가장 마지막 요소 출력하기
print(week[4])
print(week[-1])  # 이것도 됨.

# -----리스트에 순서대로 월화수목금 한번에 담아주세요.
# -----그리고 while문을 이용해서 요소 전부 출력

week = ["월", "화", "수", "목", "금"]

i = 0
while len(week) > i:
    print(week[i])
    i += 1


# ------역순 출력

i = len(week) - 1  # -1을 해야지 정확
while i >= 0:
    print(week[i])
    i -= 1

# ------ 리스트에 순서대로 21오67을 한번에 담아라
# 그리고 리스트 안에 있는 오를 정수 5로 변경하라

a = [2, 1, "오", 6, 7]

a[a.index("오")] = 5
print(a)

# 리스트안에 있는 5를 삭제하라
a.remove(5)
print(a)


# -------------------------AI문제 특정값 전부 삭제하기
# target값을 리스트에서 전부 삭제 후 출력하라.
a = [1, 3, 2, 5, 8, 2, 3, 8, 7, 2, 3, 8, 7, 66, 3, 9, 47, 5, 1, 5, 2, 3, 2]
target = 3

# while a.index(3) is not None: #null대신 is None /
#   a.remove(3)
# 이건 불가능, 값이 없으면 None을 주는 게 아니라 Error로 터짐

while target in a:  # 이런식으로 쓴다.
    a.remove(target)

a.sort()
print(a)


# ------------------------AI 문제, 리스트 요약 통게
# 리스트의 모든 원소의 합, 숫자 2의 개수, 최댓값 출력

a = [1, 3, 2, 5, 8, 2, 3, 8, 7, 2, 3, 8, 7, 66, 3, 9, 47, 5, 1, 5, 2, 3, 2]
num = len(a) - 1
i = 0
count2 = 0
total = 0
list_num = 0
max_value_prev = a[0]
max_value = a[0]

while num >= i:
    list_num = a[i]
    total += list_num

    if list_num == 2:
        count2 += 1

    if a[i] > max_value_prev:
        max_value = a[i]
        max_value_prev = max_value
    # max_value=max(a) #가장 높은 요소값 출력

    i += 1

print(f"{total}  {count2}  {max_value}")

# ---------------리스트 순서대로 월화수목금 을 한번에 담고, 화가 리스트 안에 몇번째인지 알려달라.

week = ["월", "화", "수", "목", "금"]

if "화" in week:
    i = week.index("화")
    print(f"'화'의 위치는 {i}번 째 입니다.")
else:
    print("찾는 요소가 없다.")

# -------------------------------화가 리스트 안에 있는지 if문으로 체크 후 , 있다면 삭제

week = ["월", "화", "수", "목", "금"]

if "토" in week:
    week.remove("토")
else:
    print("없습니다.")

print(week)


# -----------------1~10까지 리스트로 묶어달라.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 1
while 10 >= i:
    numbers.append(i)
    i += 1

# -----------리스트 왼쪽 회전
# 리스트 a를 왼쪽으로 k칸 회전시켜라.


a = [10, 20, 30, 40, 50]
k = 3
i = 1

while k >= i:
    b = a[0]
    del a[0]
    a.append(b)
    i += 1

print(a)

# -----------원본 보존 + 중복 제거 정렬함수
# 원본 nums는 절대 훼손하면 안 됨
# nums의 값을 중복 제거해서 정렬된 새 리스트를 리턴
# descending=True면 내림차순, 아니면 오름차순


def make_unique_sorted(nums, descending):
    nums_2 = sorted(nums, reverse=descending)

    i = 1

    while len(nums_2) > i:
        if nums_2[i - 1] == nums_2[i]:
            del nums_2[i]
        else:
            i += 1

    return nums_2


nums = [3, 1, 4, 1, 5, 9, 1, 6, 5, 3, 5]
descending = False
print(make_unique_sorted(nums, descending))
print(nums)

# -------------------조건에 맞는 첫 값 찾기
#  nums의 복사본을 내림차순 정렬(원본 훼손 금지)
# 7의 배수는 맞는데
# 14의 배수는 아닌 값 (즉, 7로 나누어 떨어지지만 14로는 안 나누어 떨어짐)
# 조건에 맞는 값이 없으면 "NONE" 출력


def func(nums):
    nums_2 = sorted(nums, reverse=True)
    i = 0
    while len(nums_2) > i:
        if nums_2[i] % 7 == 0 and nums_2[i] % 14 != 0:
            return nums_2[i]
        else:
            i += 1

    return None


nums = [13, 21, 4, 7, 28, 5, 14, 70, 49]
print(func(nums))

# -------------------------------- 45강 문제 모음
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 1. 기본 슬라이싱 => 요소야. 요소
rs = numbers[1:4]
rs = numbers[:3]
print(rs)
# 2.음수인덱스 사용
rs_2 = numbers[-3:]  # [-3 : 0]은 실행안됨.
print(rs_2)

# 3. 스텝 이용 슬라이싱
rs_3 = numbers[0::2]
rs_3 = numbers[::2]  # 더 정답
print(rs_3)

# 4. 역순 슬라이싱
rs_4 = numbers[::-1]
print(rs_4)

# 5. 복잡한 슬라이싱
rs_5 = numbers[1::2]
rs_5 = numbers[1:-1:2]  # 이렇게도 쓸 수 있다.
print(rs_5)

# ----------------------------AI 문제
# 슬라이싱만 이용해서 a를 3등분해라
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

i = len(a)

if i % 3 == 0:
    p1 = a[0 : i // 3 ]           #슬라이스 인덱스는 정수여야 해서 /가 아닌 // 사용 필수
    p2 = a[i // 3 : i * 2 // 3 ]
    p3 = a[i * 2 // 3 :]


#----------------------------사용자에게 문장 1개를 입력받아서, 출력하라.

print(input("문장을 입력하세요 : "))

#---------------------사용자에게 문장 1개를 입력받아서, ,를 기준으로 나눠주세요
user_input = input("문장을 입력하세요 : ")
print(user_input.strip().split(","))


#---------------------------사용자에게 숫자 2개를 입력받아서, 더한 결과를 출력하라
print("문장 하나를 입력하세요 : ", end ='')
user_input=input().strip().split()
print(f"입력된 내용 : {user_input}")

#---------------------------숫자를 입력받아서 형변환을 시켜줘
print("숫자를 입력하세요 : ", end ='')
print(list(map(int, input().strip().split())))

#---------------------------숫자를 입력받아, 더해라
print("숫자를 입력하세요 : ", end ='')
nums = list(map(int,input().strip().split(",")))
i=0
sum = 0
while len(nums) > i:
    sum += nums[i]
    i+=1

print(sum)


#-----------------------------------------for문으로 구구단 출력

for dan in range(1,10):
    print(f"======{dan}단======")
    for nums in range(1,10):
        print(f"{dan} x {nums} = {dan * nums}")


#----------------------------------------for문으로 1부터 n까지 존재하는 소수의 합
print("넣을 숫자릅 입력하세요 :", end=' ')
n = int(input())

def Sum_Prime(n):
    sum = 0
    if n <=1:
        print("1보다 큰 정수를 입력하세요")
        return


    for i in range(2,n+1):
        is_Prime =True

        for k in range(2, i):
            if i % k == 0:
                is_Prime =False
                break

        if is_Prime:
            sum += i

    print(f"소수의 합은 {sum}입니다.")
"""

# ----------------------------------------for문으로 1부터 n까지 존재하는 소수의 합 다시


def is_Prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def Sum_Prime(n):
    sum = 0
    for i in range(1, n + 1):
        if is_Prime(i):
            sum += i

    return sum


n = int(input())
print(Sum_Prime(n))
