import enum


numbers = [1, 34, 23, 13, 100 ,132, 1, 2, 32, 2]

for number in numbers:
    if number < 10:
        continue
    print(number)

print(min(numbers))

print(min(102, 302, 12, 324, 123))

print(numbers)
reversed_numbers = reversed(numbers)
print(reversed_numbers)
print(list(reversed_numbers))
print()

temp = [1, 2, 3, 4, 5, 6] # temp에 reversed를 사용하면 제너레이터에 해당한다

#idx를 먼저 정의하지 않고 바로 가능하다
for idx in reversed(temp):
    print("first: {}".format(idx))

for idx in reversed(temp):
    print("second: {}".format(idx))

for idx in temp:
    print("reset: {}".format(idx))

# ---- enumerate()

list_a = ["1st", "2nd", "3rd"]

# 단순 출력
print(list_a)
print()

print(enumerate(list_a))
print()

# enumerate 적용
print(list(enumerate(list_a)))
print()

# list()로 강제 변환
for idx, value in enumerate(list_a):
    print("{} = {}".format(idx, value))
print()

# ---- items()

dict_a = {
    "key_0" : "1",
    "key_1" : "2",
    "key_2" : "3"
}

print(dict_a)
print()

print("item():\n", dict_a.items())
print()

for key, element in dict_a.items():
    print("{} = {}".format(key, element))
print()

# ---- array_b == array_c
array_b = []

for i in range(0, 20, 2):
    array_b.append(i * i)
print(array_b)
print()

# list comprehensions // list name = [표현식 for 반복자 in 반복할 수 있는 것]
array_c = [i * i for i in range(0, 20, 2)]
print(array_c)
print()

# list name = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
array_d = ["one", "two", "three"]
output = [num for num in array_d if num != "one"]
print(output)
print()

# ---- 

num = {
    "choi "
    "ejae"
}
print(num)
print()

# 반복할 수 있는 것 == iterable
# 내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체를 의미
# list, dict, tupple...

num2 = [1, 2, 3, 4, 5]
r_num2 = reversed(num2)

print(r_num2) # reversed()함수의 리턴값이 바로 reverseiterator... 메모리의 효율성을 위해
# 1만개의 요소가 들어있는 리스트를 복제 -> 뒤집어 리턴하는 것 보다 기존의 리스트를 활용
print(next(r_num2))
print(next(r_num2))
print(next(r_num2))
print(next(r_num2))
print()

# notation

print("{:b}".format(10)) # 10 -> 2
print(int("1010", 2)) # 2 -> 10
print()

print("{:o}".format(10)) # 10 -> 8
print(int("12", 8)) # 8 -> 10
print()

print("{:x}".format(10)) # 10 -> 16
print(int("10", 16)) # 16 -> 10
print()