# 파일 입출력
# 텍스트 파일 생성

path = "/Users/kim_yoonkwon/PycharmProjects/pythonProject/Day10/"

file = open("hello.txt","wt",encoding = "UTF-8")

file.write("안녕하세요")
file.write("\n")
file.write("파일 입출력 내용을 학습합니다.")

print("파일이 생성되었습니다.")

file.close