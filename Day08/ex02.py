# 가변 매개변수
# 디폴트 매개변수

# 다중 반환
'''
def 함수명(매개변수):
    실행문
    실행문
    return (값1), (값2), (값3), ... 
'''

def cal(*args):
    result1 = sum(args)
    result2 = sum(args) / len(args)
    result3 = max(args)
    result4 = min(args)
    return result1, result2, result3, result4
# 반환값들을 튜플로 생성하여 반환

a, b, c, d = cal(1,2,3,4,5)
print(a)
print(c)

result = cal(1,2,3,4,5)
print(result)