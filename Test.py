#----------------------------------------17강 조건문 기초 문제풀이
age = 40
if age >= 10 and age < 20:
  print("10대")
elif age >= 20 and age < 30:
  print("20대")
elif age >= 30 and age < 40:
  print("30대")
elif age >= 40 and age < 50:
  print("40대")
else :
  print("50대 이상")


#-----------------Al 문제
#아래 조건을 만족하는 파이썬 코드를 작성해봐. (입력은 없음)
#변수 a = "7", b = "3" 를 만든다. (둘 다 문자열)
#a와 b를 숫자로 형변환해서 더한 결과를 sum_value에 저장한다.
#7+3 =10 형식으로 출력한다. (f-string 사용)

a="7"
b="3"
a = int(a)
b = int(b)
sum_value = a + b
print(f"{a} + {b} = {sum_value}")

#변수 age = 19 가 있을 때, 아래 규칙대로 출력하는 if/elif/else 코드를 작성해봐.
#age가 20 이상이면: 성인입니다
#age가 17 이상 19 이하이면: 고등학생 나이입니다
#그 외에는: 미성년입니다
age = 19
if age >= 20:
  print("성인입니다.")
elif age >= 17 and age <= 19:
  print("고등학생 나이입니다.")
else:
  print("미성년입니다.")