
import time

#path = "/Users/kim_yoonkwon/PycharmProjects/pythonProject/Day10/"

today = time.strftime("%Y %m %d")

file = open("할 일(" + today + ")" + ".txt", "wt")

no = 1
while True :
    todo = input("오늘 할 일 : ")
    
    if not todo:
        break
    
    file.write(no + ". " + todo + '\n')
    no = no + 1
    
file.close