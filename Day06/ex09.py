
# 대한민국의 수도를 맞추는 퀴즈
# 무한반복 --> 종료를 필요로 함(break)

while True:
    city = input("대한민국의 수도는? ")
    if city == "서울" or city == "seoul":
        print("정답입니다.")
        break
    else:
        print("틀렸습니다.")