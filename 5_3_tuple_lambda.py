# ---- 
print("---- 1. 튜플(tuple) ----\n")

# list와 비슷하다
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

# a[0] = 100 값을 바꿀 수 없다

#그러면 왜 쓰는가
[a, b] = [10, 20]
(c, d) = (30, 40)
e, f = 50, 60 # 괄호를 제거해도 튜플 처리
print(a, b, c, d, e, f)
print()

c, d = d, c # swap
print(a, b, c, d, e, f)
print()

# 튜플 사용 이유

A, B = 97, 40
몫, 나머지 = divmod(A, B) # 튜플 리턴을 통해 한번에 가능
print(몫)
print(나머지)
print(type(divmod(A, B)))
print()

# 튜플 예
for i, value in enumerate([1, 2, 3, 4, 5, 6], start=1):
    print("{}번째 요소는 {}입니다".format(i,value))

# tuple은 소괄호를 생략할 수 있다
# 튜플 예

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

print((273, )) # 요소가 하나있는 튜플의 경우에 ','가 있어야 한다
print(type((273, ))) # >> tuple
print()

# 딕셔너리에서 튜퓰 예

#a = {
#     숫자: O
#     문자열: O
#     불: O
#     리스트: 는 키로 앞에 올 수 없다
#     튜플: O
#}

d_tuple = {
    (0, 0): 10,
    (0, 1): 20,
    (1, 0): 30,
    (1, 1): 40
}

print( d_tuple[(0, 0)], d_tuple[0, 1], d_tuple[1, 0], d_tuple[1, 1]) # 튜플은 괄호 생략 가능
print()

# ----
# 함수의 매개변수로 함수 전달하기
# 함수포인터와 비슷하네
print("---- 함수의 매개변수로 함수 전달하기 ----\n")
def call_10_times(func):
    for i in range(10):
        # 콜백함수(callback)
        func(i)

def print_hello(number):
    print("hello", number)

call_10_times(print_hello) # 함수를 하나 더 만들어서 보내는건 낭비다?! >> 그래서 람다를 쓴다
print()

call_10_times(lambda number: print("hello!!!!!", number)) # lambda를 통해 한줄완성
print()

print("---- 2. 람다를 활용한 filter 함수 만들기 ----\n")

a = list(range(100))

#def 짝수만(number):
#    return number % 2 == 0
#b = filter(짝수만, a)
b = filter(lambda number: number % 2 == 0, a)
print(list(b))
print()

print("---- 람다를 활용한 map 함수 만들기 ----\n")

# map >>> 어떠한 리스트를 기반으로 새로운 리스트를 만듦
a = list(range(100))

#def 제곱(number):
#    return number * number
#print(list(map(제곱, a)))
print(list(map(lambda number: number * number, a)))
print()

print("---- filter + map ----\n")

print([i * i for i in a if i % 2 == 0])
print()
print("- filter와 map을 사용하지 않은 위 식은 메모리를 사용하는 방식이다\n")
print("- filter와 map은 제너레이터 함수로, 메모리를 사용하지 않는다\n")
print("- 데이터에 자유로운 요즘 그냥 아무거나 써라\n")