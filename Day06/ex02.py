
score = input("성적 : ")
score = int(score)

# 다중 조건문
# if 조건에 만족하지 않았을때
# elif 조건에 만족하는지 확인
# 그게 아니면 else로 

if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 70:
    print("C학점입니다.")
elif score >= 60:
    print("D학점입니다.")
else :
    print("F학점입니다.")