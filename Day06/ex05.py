
# for 반복문
# for 변수 in (리스트, 튜플 등의 컬렉션)

li = [1,2,3,4,5]

for n in li:
    print(n, end='')

# 문자열을 입력 받아서 비밀번호를 확인하는 프로그램을 작성 (비밀번호 조건 : 숫자와 문자 포함)

pw = input("비밀번호 : ")

ch_count = 0    # 문자의 개수
num_count = 0   # 숫자의 개수

# pw라는 문자열을 한 글자씩 가져와서 반복

for ch in pw :
    if ch.isalpha():    # 해당 문자가 알파벳이면 true 아니면 false
        ch_count += 1
    if ch.isnumeric():     # 해당 문자가 숫자이면 true 아니면 false
        num_count += 1

if ch_count > 0 and num_count >0 :
        print("enable")
else :
        print("disable")