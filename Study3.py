# 딕셔너리

ages = [10, 20, 30]
print(ages[0])  # 철수
print(ages[1])  # 짱구
print(ages[2])  # 유리

ages.append(40)  # index 3
print(ages[3])  # 장미

ages.remove(10)  # 철수 나이 삭제
# => 결국 이러면 짱구 나이 인덱스를 외워야 부를 수 있음.

# 딕셔너리
ages = {
    "철수": 10,
    "유리": 20,
    "짱구": 30,
    "맹구": 40,
}

print(ages["철수"])
print(ages["유리"])
print(ages["짱구"])
print(ages["맹구"])
print(ages)

ages["나미리"] = (50) # 딕셔너리 데이터 추가., key 세팅한다고 말함. / 딕셔너리 = key, value
print(ages)
ages["나미리"] = 60  # 이건 값 수정
print(ages)

del ages["짱구"] # 짱구 keys & values값 삭제

if "철수" in ages: #값확인
  print("있다")
else:
  print("없다")

# 콜렉션(객체)
# - 리스트  => 장점 : 데이터 넣을 떄 편함(a.append(10))
# - 딕셔너리 => 장점 : 데이터 가져올 떄 편함.

print("== 딕셔너리 반복 v1 ==")
for name in ages:
    age = ages[name]
    print(f"{name} 나이 : {age}살")

print("== 딕셔너리 반복 v2, keys() ==")
# print(ages.keys()) # 키 반복

for name in ages.keys():
    age = ages[name]
    print(f"{name} 나이 : {age}살")


print("== 딕셔너리 반복 v3, values() ==")

for age in ages.values():  # values에서는 keys를 가지고 못옴.
    print(f"나이 : {age}살")


print("== 딕셔너리 반복 v4, items() ==")  # 동시에 둘 다 가져올 수 있음
for name, age in ages.items():
    print(f"{name} 나이 : {age}살")
