# for문과 range() 함수
# range() : 범위 생성 함수    구조 : range(초기값, 종료값, 증감값)
# range(1,10,2) : 1,3,5,7,9

for n in range(1,10):
    print(n)

# 구구단
dan = input("단 : ")
dan = int(dan)
for n in range(1,10):
    print(f"{dan} x {n} = {dan*n}")

# 이중반복문 / 중첩반복문  : 반복문 안에 또다른 반복문
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} x {j} = {i*j}")
    print()