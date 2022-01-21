'''
    제어문(조건문, 반복문)을 이용하여 아래와 같이 * 문자와 같은 프로그램을 완성 (1단계)
n = 5
    *
    **
    ***
    ****
    *****

(2단계)
    *
   ***
  *****
 *******
*********
'''

# 1. 입력 받은 수 n만큼 줄 반복   2. n번째 줄의 크기만큼 별의 개 반복

# 1단계

n = input("숫자를 입력하세요 : ")
n = int(n)
for i in range(0,n+1):
    for j in range(1,(i+1)):
        print("*",end=" ")
    print()

# 2단계

for i in range(1,n+1): # i : 1,2,3,4,5
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i*2): # j : 0,..., (i*2)-1
        print("*",end=" ")
    print()