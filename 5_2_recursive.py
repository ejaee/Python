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
print(fibo(30))
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
