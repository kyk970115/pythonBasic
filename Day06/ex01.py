# if 조건문

age = input("당신은 몇 살입니까?")
age = int(age)

if age >= 20:
    print("성인입니다.")
    print(f"나이 : {age}")
else:
    print("청소년입니다.")
    print(f"나이 : {age}")