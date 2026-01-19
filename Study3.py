# =========================================================52강 딕셔너리

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

ages["나미리"] = (
    50  # 딕셔너리 데이터 추가., key 세팅한다고 말함. / 딕셔너리 = key, value
)
print(ages)
ages["나미리"] = 60  # 이건 값 수정
print(ages)

del ages["짱구"]  # 짱구 keys & values값 삭제

if "철수" in ages:  # 값확인
    print("있다")
else:
    print("없다")

# 콜렉션(객체)
# - 리스트  => 장점 : 데이터 넣을 떄 편함(a.append(10))
# - 딕셔너리 => 장점 : 데이터 가져올 떄 편함.

print("== 딕셔너리 반복 v1 ==")
for name in ages:  # name이 중요한게 아니라. 그냥 딕셔너리를 부르면 keys 값 호출.
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


# ===============================================================56강 클래스
class Person:  # 1. 설계도(클래스) 선언
    
    # 2. 생성자 메서드 (__init__)
    # 객체가 만들어질 때 '자동으로' 딱 한 번 실행됩니다.
    # 재료(name, age...)를 받아서 내 몸(self)에 저장하는 역할을 합니다.
    def __init__(self, name, age, home, hobby): 
        self.name = name    # 들어온 name을 내(self) 이름 공간에 저장
        self.age = age      # 들어온 age를 내(self) 나이 공간에 저장
        self.home = home
        self.hobby = hobby  
    
    
    # __str__ : 객체를 까보는 행위
    # 고객의 편의가 아닌 개발자의 편의를 위해 존재하는 함수
    # 디버깅할 때 해당 객체의 어떤 데이터가 들어있는지 확인 가능하게 한다.
    def __str__(self): 
        return f"name : {self.name}, age : {self.age}, home : {self.home}, hobby : {self.hobby}"
    
        
    # 3. 메서드 (함수)
    # 이 클래스가 할 수 있는 행동을 정의합니다.
    def introduce(self):
        print(f"저는 {self.home}사는 {self.age}살, 취미는 {self.hobby}인 {self.name}입니다.")
        
    

# ---------------------------------------------------------
# 4. 객체 생성 (사용하기)

# 틀린 부분 수정:
# p1 = Person() -> 에러 발생! (설계도에 재료 4개를 넣으라고 했는데 안 넣어서)
# p1 = person(...) -> 에러 발생! (대문자 P여야 함, 파이썬은 대소문자 구분)

# 올바른 생성 방법:
p1 = Person("홍길동", 23, "안산", "테니스") 
p2 = Person("김철수", 30, "서울", "축구")    # 하나 더 만들어봄

# 5. 사용
p1.introduce()  # 홍길동이 자기소개
p2.introduce()  # 김철수가 자기소개
print(p1) # 주소가 나온다. 
