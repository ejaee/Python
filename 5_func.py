# ----
print("---- 함수 ----\n")
#함수를 선언
def 함수이름(매개변수1, 매개변수2):
    print("안녕하세요" + str(매개변수1))
    print("반갑습니다" + str(매개변수2))
    return 매개변수1 + 매개변수2

# 함수를 호출
print(함수이름(1, 2))

# 프로그램 종료

from re import A

# ----

def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)
print()

# ----
print("---- 가변 매개변수 ----\n")

print("이것은", "가변", "매개변수 입니다")

# ----
def 함수이름2(매개변수1, 매개변수2, *가변매개변수1):
    print(매개변수1)
    print(매개변수2)
    print(가변매개변수1)

함수이름2(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 한 함수에서 가변매개변수 하나만 사용가능하다 (*가변매개변수1, *가변매개변수2))
# 가변매개변수는 앞에 올 수 없다 (*가변매개변수1, 매개변수1)

# ----
print("---- 기본 매개변수 ----\n")

def print_set_times(value, n=5): # 기본매개변수를 5로
    for i in range(n):
        print(value)

print_set_times("기본매개변수 입니다")
print()
print()
print_set_times("hello", 2) # n값을 주면 적용된다

# 기본매개변수는 앞에 오지않고 마지막에 입력을 한다 (2, "hello")

# ----
print("---- 키워드 매개변수 ----\n")
# 가변과 기본을 같이쓰고 싶다면?
print() # 가변 + 기본 조합 시, 가변 먼저오고 기본

def function(일반매변1, 일반매변2, *가변매변, 기본매변a=10):
    print(일반매변1, 일반매변2)
    print(가변매변)
    print(기본매변a)
    print()

function(0, 1, 2, 3, 4, 5, 6, 7, 8)
# 0, 1은 일반매변으로 들어가고 나머지 모두 가변으로 들어갔다
# 기본매변은 10으로, 바뀌지 않았다
function(0, 1, 2, 3, 4, 5, 6, 7, 8, 기본매변a=5)
# 기본매변을 바꾸고 싶다면 이름을 적어줘야한다

# ----
print("---- 리턴 ----\n")
# 왔던 곳으로 돌아가라

def sum_all(start, end):
    변수 = 0
    for i in range(start, end + 1):
        변수 += i
    return 변수

print(sum_all(1, 100))
print(sum_all(50, 100))
print()

 # 기본 매변 활용하여 편하게 할 수 있다
def sum_all2(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        print(start, end, step, output)
        output += i

    return output

print("A", sum_all2()) # 5050
print("B", sum_all2(0, 100, 10)) # 1275
print("C", sum_all2(end=50)) # 5050
print("D", sum_all2(end=100, step=2)) # 2550
print()

# ----
# 확인문제

def mul(*value):
    변수 = 1
    for i in value:
        변수 *= i
    return 변수

print(mul(5, 7, 9, 10))

# ----
print("---- 함수의 활용 ----\n")

print("---- 재귀함수 ----\n")
# n! = 1 * 2 * 3 * ... * n
def iter_factorial(n):
    변수 = 1
    for i in range(1, n+1):
        변수 *= i
    return 변수

print(iter_factorial(10))
print()

# n! = n * (n-1)!
# 0! = 1
def recur_factorial(n):
    if (n == 0):
        return 1
    else:
        return (n * recur_factorial(n-1))

print(recur_factorial(10))
print()


print("---- 피보나치 수열 ----\n")
counter = 0
def fibo(n):
    global counter # 함수 외부의 변수를 사용할 때
    counter += 1 
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

#print(fibo(1))
#print(fibo(2))
#print(fibo(3))
#print(fibo(4))
#print(fibo(5))
#print(fibo(6))
print(fibo(36))
print(counter, "번 연산")
print()

# 위 속도 개션
print(">> 메모화(memoization)\n")

메모 = { 1: 1, 2: 1} # 레퍼런스를 나타내는 자료형은 글로벌을 사용하지 않아도 된다
def f(n):
    if n in 메모:
        return 메모[n]
    else:
        output = f(n-1) + f(n-2)
        메모[n] = output
        return output
print(f(36))
print()

print("---- 조기리턴 ----\n")

메모 = { 1: 1, 2: 1} # 레퍼런스를 나타내는 자료형은 글로벌을 사용하지 않아도 된다
def f(n):
    if n in 메모:   # else를 없애므로써 들여쓰기 단계를 줄여줌 >> 더 좋은 코드
        return 메모[n] # 조기리턴
    output = f(n-1) + f(n-2)
    메모[n] = output
    return output
print(f(36))
print()

# ---- 
print("---- 문제1 리스트 평탄화(list_flatten) ----\n")

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            # output.append(item)
            output += [item]
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("origin:", example)
print("change:", flatten(example))
print()

# ---- 
print("---- 튜플(tuple) ----\n")

# list와 다르게 소괄호로 선언
# 한 번 선언하면 값을 바꿀 수 없음

a = (1, 2, 3, 4)
print(type(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a)
print()

[a, b] = [10, 20]
(c, d) = (30, 40)
e, f = 50, 60
print(a, b, c, d, e, f)
print()

c, d = c, d # swap
print(a, b, c, d, e, f)
print()

# ----

A, B = 97, 40
몫, 나머지 = divmod(A, B)
print(몫)
print(나머지)
print(type(divmod(A, B)))
print()

# tuple은 소괄호를 생략할 수 있다

def test():
    return 1, 2

a, b = test()
print(a, b)
print()

# 헷갈릴 수 있는 것들

print([273])
print(type([273])) # >> list
print()


print((273))
print(type((273))) # >> int
print()


print((273, ))
print(type((273, ))) # >> tuple
print()

print()
print()
print()
print()