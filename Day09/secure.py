
# 개인정보를 마스킹하는 함수를 정의

def secureName(name):
    return name[0] + "**"

def secureNo(no):
    return no[0:8] + "******"

def securePhone(phone):
    return phone.replace(phone[4:8], "****")