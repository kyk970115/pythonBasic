'''
    1부터 100까지 수를 반복하여 출력하면서 수가 3, 6, 9인 경우 그 개수만큼 *을 출력하는 프로그램을 완성
'''
" 십의 자리만 3,6,9 / 일의 자리만 3,6,9 / 둘다 3,6,9"

for i in range(1,101):
    
    ten = int(i / 10)
    one = int(i % 10)
    
    ten1 = (ten == 3 or ten == 6 or ten == 9)
    one1 = (one == 3 or one == 6 or one == 9)
    
    if ten1 and one1 :
        print("**")
    elif ten1 or one1 :
        print("*")
    else:
        print(i)