# 정수 하나를 입력받아 1부터 입력받은 수까지의 합을 구하는 프로그램

n = input("원하는 숫자를 입력해주세요 : ")
n = int(n)
a = 1
sum = 0

for a in range(a,(n+1)):
    sum = sum + a

print(f"{sum}")