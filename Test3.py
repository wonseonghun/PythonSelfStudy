# == 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기 ==
month_end_days = {
    "1월": 31,
    "2월": 29,
    "3월": 31,
    "4월": 30,
    "5월": 31,
    "6월": 30,
    "7월": 31,
    "8월": 31,
    "9월": 30,
    "10월": 31,
    "11월": 30,
    "12월": 31,
}

#print(month_end_days["1월"])

#== 문제 : 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기

for i in range(1,13):
  month = str(i) +"월"
  if i ==2:
    end_day =29
  elif i in [1,3,5,7,8,10,12]:
    end_day = 31
  else:
    end_day = 30
    
  
for month in month_end_days:
  end_day=month_end_days[month]
  print(f"{month}의 마지막 날은 {end_day}")
 
# 다른 버전 ----------------------------- 
month_end_days_list_ver =[31,29,31,30,31,30,31,31,30,31,30,31]

for i in range(0,12):
  month_end_days[f"{i+1}월"] = month_end_days_list_ver[i]
  print(month_end_days)
  

#==문제 : keys()를 이용해 순회출력==
month_end_days = {
    "1월": 31,
    "2월": 29,
    "3월": 31,
    "4월": 30,
    "5월": 31,
    "6월": 30,
    "7월": 31,
    "8월": 31,
    "9월": 30,
    "10월": 31,
    "11월": 30,
    "12월": 31,
}

for month in month_end_days.keys():
  end_day =  month_end_days[month]
  print(f"{month}의 마지막 날은 {end_day}입니다.")
  
for month, end_day in month_end_days.items():
  print(f"{month}은 {end_day}일까지입니다.")
  

