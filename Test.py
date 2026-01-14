# ----------------------------------------17강 조건문 기초 문제풀이
age = 40
if age >= 10 and age < 20:
    print("10대")
elif age >= 20 and age < 30:
    print("20대")
elif age >= 30 and age < 40:
    print("30대")
elif age >= 40 and age < 50:
    print("40대")
else:
    print("50대 이상")


# -----------------Al 문제
# 아래 조건을 만족하는 파이썬 코드를 작성해봐. (입력은 없음)
# 변수 a = "7", b = "3" 를 만든다. (둘 다 문자열)
# a와 b를 숫자로 형변환해서 더한 결과를 sum_value에 저장한다.
# 7+3 =10 형식으로 출력한다. (f-string 사용)

a = "7"
b = "3"
a = int(a)
b = int(b)
sum_value = a + b
print(f"{a} + {b} = {sum_value}")

# 변수 age = 19 가 있을 때, 아래 규칙대로 출력하는 if/elif/else 코드를 작성해봐.
# age가 20 이상이면: 성인입니다
# age가 17 이상 19 이하이면: 고등학생 나이입니다
# 그 외에는: 미성년입니다
age = 19
if age >= 20:
    print("성인입니다.")
elif age >= 17 and age <= 19:
    print("고등학생 나이입니다.")
else:
    print("미성년입니다.")

# ---------------------AI 문제
# 요금 계산기
"""
age_str, minutes_str는 문자열이니까 정수로 변환해서 사용한다.
기본요금은 1,000원.
통화요금은 분당 15원.
할인 규칙 (나이 기준)
나이 19세 이하: 총액에서 20% 할인
나이 65세 이상: 총액에서 30% 할인
그 외: 할인 없음
최종 요금은 정수로 출력한다. (소수점 나오면 int()로 버림)
"""

age_str = "20"
minutes_str = "70"
age_str = int(age_str)
minutes_str = int(minutes_str)

totalPrice = 1000 + 15 * minutes_str

if age_str <= 19:
    totalPrice = 0.8 * totalPrice
elif age_str >= 65:
    totalPrice = 0.7 * totalPrice
else:
    totalPrice = totalPrice

print(f"최종 요금은 {int(totalPrice)}원입니다.")

# -------------숫자 뒤집기 & 합 비교  ========================> 못풀음
"""
n_str을 정수 n으로 변환한다.
while문만 사용해서 아래를 구한다:
: n을 뒤집은 숫자 (예: 1230 → 321, 50760 → 06705 → 6705)
digit_sum: n의 각 자리수 합
마지막에 아래 규칙으로 출력:
만약 rev > digit_sum이면 "REV WIN"
아니면 "SUM WIN"
"""

n_str = "50760"
n = int(n_str)

rev = 0
digit_sum = 0
while n > 0:
    last = n % 10
    digit_sum += last
    rev = rev * 10 + last

    n = n // 10
    # 여기는 어럽네..

if rev > digit_sum:
    print("REV WIN")

else:
    print("SUM Win")


# --------------------------------구구단 만들기.

dan = 1

while 9 >= dan:
    num = 1
    print(f"===={dan}====")
    while 9 >= num:
        print(f"{dan} x {num} = {dan * num}")
        num += 1

    dan += 1

# -----------------------------1부터 100까지 짝수만 출력
i = 1
while 100 >= i:
    if i % 2 == 0:
        print(i)

    i += 1


# -------------------------------------구구구단 만들기
dan_First = 1
dan_Second = 1
num = 1

while 9 >= dan_First:
    print(f"----{dan_First}단----")
    dan_Second = 1

    while 9 >= dan_Second:
        num = 1

        while 9 >= num:
            print(
                f"{dan_First} x {dan_Second} X {num} = {dan_First * dan_Second * num}"
            )
            num += 1
        dan_Second += 1

    dan_First += 1

# ---------- 구구단은 n단 m단 중 홀수단만 1~limit까지 곱 중 짝수곱만 출력해주세요.
n = 4
m = 19
limit = 11

i = n
k = 1
while m >= i:
    k = 1
    while limit >= k:
        if i % 2 == 1 and k % 2 == 0:
            print(f"{i} x {k} = {i * k}")
        k += 1
    i += 1


# ------------------------다국어 인사 만들기
def hello(language: str, count: int):  # 이런식으로 만든다. 또한 다른 타입도 가능하다ㅏ.
    i = 1
    match language:
        case "Korea":
            while count >= i:
                print("안녕하세요")
                i += 1

        case "Japan":
            while count >= i:
                print("곤니찌와")
                i += 1

        case _:
            while count >= i:
                print("다른 언어입니다.")
                i += 1


def hello(language: str, count: int):  # 수정 버전
    match language:
        case "Korea":
            msg = print("안녕하세요")
        case "Japan":
            msg = print("곤니찌와")
        case _:
            msg = print("다른 언어입니다.")

    i = 1
    while count >= i:
        print(msg)
        i += 1


hello("Korea", 3)


# --------------입력받은 정수의 모든 약수를 출력하는 함수 구현
def print_divisor(num):
    i = 1
    while num >= i:
        if num % i == 0:
            print(f"{i}는 {num}의 약수입니다.")
        i += 1


print_divisor(1000)

# -------------- 36강 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요. + 약수의 합


def get_divisors_sum(num):
    sum = 0
    i = 1
    while num >= i:
        if num % i == 0:
            sum += i
        i += 1
    return sum


def isPrimeNumber(num):
    if num < 2:
        return False

    i = 2
    while num >= i:
        if num % i == 0:
            return False  # 이 리턴은 함수에 대한 return이다.
        i += 1
    return True  # 이렇게 하면 while문이 끝나고 온다.


# 약수의 합을 이용한 소수 판별
def isPrimeNumber2(num):
    if num < 2:
        return False

    return get_divisors_sum(num) == num + 1


# 지렸다...


a = int(input("정수를 입력하세요: "))
b = int(input("약수의 합을 알고 싶은 정수를 입력하세요 : "))

if isPrimeNumber(a) == True:
    print(f"{a}는 소수가 맞습니다.")
else:
    print(f"{a}는 소수가 아닙니다.")

print(get_divisors_sum(b))


# ----------36강 1부터 1000사이에 존재하는 소수들의 개수를 출력해주세요
def getDivisorsSum(num):
    s = 0
    i = 1
    while num >= i:
        if num % i == 0:
            s += i
        i += 1
    return s


def isPrimeNumber3(num):
    if num <= 1:
        return False

    return getDivisorsSum(num) == num + 1


def countPrimeNumber(num):
    i = 1
    count = 0
    while num >= i:
        if isPrimeNumber3(i) == True:
            count += 1
        i += 1
    return count


a = int(input("소수들의 개수를 알고 싶은 숫자를 작성하세요 : "))
print(countPrimeNumber(a))

