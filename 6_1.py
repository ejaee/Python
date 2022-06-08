# ----

import sre_parse


print("---- 예외처리 ----\n")

# 구문 오류 (syntax error) : 프로그램 실행 전에 발생하는 오류
# 예외 or 런타임 오류 : 프로그램 실행 중에 발생하는 오류

print("예외를 모두 해결하는 것을 예외처리(exception handling)\n")

# 조건문으로 예외 처리
user_input = input("정수입력1> ")

if user_input.isdigit():
    number_input = int(user_input)
    print(number_input)
else:
    print("is not digit! (else)")
    
print()

# try except 구문
# try:
#    예외 발생 가능성이 있는 코드 코드
# except:
#    예외 발생 시 실행할 코드

print("try except 구문\n")

try:
    user_input = int(input("정수입력2> "))
    print(user_input)

except:
    print("is not digit!! (used except)")
print()
