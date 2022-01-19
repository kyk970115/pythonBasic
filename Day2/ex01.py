print("안녕하세요")
print("파이썬 프로그래밍")
print("\'바나나우유\'가 주문완료")

print("이름\t\t: 김윤권")
print("성별\t\t: 남")
print("키\t\t: 170")
print("생년월일\t: 970115")

print("""
      아령하세여~잇
      딴따라랄라ㅏ딴라라라
      즐거운 주말 개꿀딱""")

#문자열 연산자
a = "python"
b = "programming"
print(a + " " + b)

num = 10
print("number : " + str(num))

#문자열 반복 연산자
print("여러번 반복하여 출력" *3)

str1 = "안녕하세요"

# 문자열 선택 연산자 : [index]
#인덱싱
# index는 0부터 시작하는 순서번호
print(str1[0])
print(str1[1])
print(str1[4])

#슬라이싱
#[시작index : 끝index+1]
print(str1[0:2])
print(str1[2:])
print(str1[:2])

# 문자열의 길이 - ㅣ두
print("문자열의 길이 " + str(len(str1)))

# 변수 선언
a = 2
b = 3.0
c = "안녕하세요"

print(type(a))
print(type(b))
print(type(c))

x = 10
y = 20

print("x + y = ", x + y)
print("x - y = ", x - y)
print("x * y = ", x * y)
print("x / y = ", x / y)

i = 2
j = 3
print("2의 3제곱 : ", i**j)

print("(1+2) * 3 = ", (1+2 * 3))
print("1 + (2 * 3) = ", 1 + (2 * 3))

# 복합 대입 연산자
A = 10
A += 1
print("A += 1 ; ", A)

A -= 1
print("A -= 1 : ", A)

A *= 2
print("A *= 2 : ", A)

A /= 2
print("A /= 2 : ", A)

p = input("p : ")
q = input("q : ")

p = input(p)
q = input(q)

print("p + q = ", p + q)