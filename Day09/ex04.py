
# 표준 모듈 

# 1. math : 수학 연산 관련 함수 제공 모듈 

import math
print(f"math.pi : {math.pi}")
print(f"math.ceil(1.1) : {math.ceil(1.1)}") # 올림
print(f"math.floor(1.9) : {math.floor(1.9)}") # 내림
print(f"round(2.5,1) : {round(2.5,1)}") # 반올림
print(f"math.trunc(1.9) : {math.trunc(1.9)}") # 절사
print(f"math.sqrt(9) : {math.sqrt(9)}") # 제곱근
print(f"math.pow(3,2) : {math.pow(3,2)}") # 제곱

# 2. random : 난수 제공 모듈

import random
print(f"random.random : {random.random()}") # 실수
print(f"random.randint : {random.randint(1,10)}") # (a,b) 사이의 정수
print(f"random.randrange : {random.randrange(1,10,2)}") 
# (a,b,c) a이상 b미만 c만큼 증가하는 정수
seasons = ['봄', '여름', '가을', '겨울']
print(f"favorite season : {random.choice(seasons)}") 
# choice(A) : 시퀀스 자료형 A의 요소 중 임의로 반환
lotto = range(1,46)
print(f"number is {random.sample(lotto,6)}")
# sample(A,n) : 시퀀스 자료형 A 중 n개 임의로 반환
li = [1,2,3,4,5]
random.shuffle(li)
print(f"random.shuffle(li) : {li}")
# print(f"random.shuffle(li) : {random.shuffle(li)}") == None
# : (결과를 반환하는 함수가 아닌) 리스트를 셔플하기만 하는 함수
# shuffle(A) : 시퀀스 자료형 A의 요소들의 순서 섞음

# 3. time : 시간 처리 관련 모듈

import time

print(f"time() : {time.time}")
t = time.time()
print(f"ctime() : {time.ctime(t)}")
s = time.strftime("%Y/%m/%d (%a) %H:%M:%S")
print(f"strftime() : {s}")
time.sleep(5) # 지정한 시간만큼 시스템을 일시 중지

# 4. datetime : 날짜/시간 데이터 처리 모듈

import datetime

nowtime = datetime.datetime.now() # [모듈].[객체].now()
print(f"현재 날짜와 시간 : {nowtime}")
today = datetime.date(2022,1,27)
print(f"현재 날짜와 시간 : {today}")
today = datetime.datetime.now()
print(f"{today.year}년 {today.month}월 {today.day}일 {today.hour}시 {today.minute}분 {today.second}초")
specialDay = datetime.date(2022,2,7)
print(f"종강일 : {specialDay}")
t1 = datetime.time(15,0,0)
print(f"현재 시간 : {t1}")
t2 = datetime.time(15,50,0)
print(f"수업 종료 : {t2}")