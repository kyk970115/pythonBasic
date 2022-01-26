
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
# print(f"random.shuffle(li) : {random.shuffle(li)}") == None : 
# shuffle(A) : 시퀀스 자료형 A의 요소들의 순서 섞음

# 3. time : 시간 처리 관련 모듈
# 4. datetime : 날짜/시간 데이터 처리 모듈