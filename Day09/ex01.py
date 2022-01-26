
# 모듈 : 변수나 함수 또는 클래스로 모아놓은 파이썬 파일 - 하나의 파이썬 파일(.py)
# 패키지 : 모듈들이 여러 개 모여있는 폴더
# 모듈 사용  : import 모듈

import converter
from converter import *

miles = kmToMiles(150)
print(f"150km = {miles} miles")

pound = gramToPound(1000)
print(f"1000g = {pound} pound")