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

#---------------리스트 순서대로 월화수목금 을 한번에 담고, 화가 리스트 안에 몇번째인지 알려달라.

week = ["월", "화", "수", "목", "금"]

if "화" in week:
  i = week.index("화")
  print(f"'화'의 위치는 {i}번 째 입니다.")
else:
  print("찾는 요소가 없다.")

#-------------------------------화가 리스트 안에 있는지