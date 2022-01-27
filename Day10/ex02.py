# 파일 입출력
# 텍스트 파일 생성

path = "/Users/kim_yoonkwon/PycharmProjects/pythonProject/Day10/"

file = open("hello.txt","at",encoding = "UTF-8")

file.write("\n")
file.write("이어서 내용을 추가합니다")
file.write("\n")
file.write("텍스트 파일 내용 추가 모드 : at.")

print("파일이 새로운 내용을 추가했습니다.")

file.close