# format() 메소드
# {}괄호 기호로 변수나 값이 표시될 위치(형식)을 지정하여 출력

print(" 내 이름은 {}".format('홍길동'))

a = 10
b = 20
print("a : {}, b : {}".format(a,b))
print("b : {1}, a : {0}".format(a,b)) # 인덱스로 인식

print("{0}하세요, 저는 ---{1}, 과목은 파이썬{1}, 다음에 봐요{0}".format('안녕','하세요'))

tel1, tel2, tel3 = "02", "992", "3497"
print('address : {0}-{1}-{2}'.format(tel1,tel2,tel3))

academy = 'SBS'
print('name : {name}'.format(name=academy))