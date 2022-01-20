
# 커피 1잔을 300원, 자판기에 금액을 입력하고 커피의 잔 수에 따라서

money = input("입력 금액 : ")

# 조건 : 남은 금액이 300원보다 클 때
i = 0
money = int(money)
while money >= 300:
    money = money - 300
    i = i + 1
    print(f"커피 {i}잔, 잔돈 {money}원")