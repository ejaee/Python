def print_3_times():
    print("hi")
    print("hi")
    print("hi")

print_3_times()
print()

def print_count(n, value):
    for idx in range(n):
        print(value)

print_count(3, "hello")
print()

# 가변 매개변수

def print_n_times(n, *values):
    for idx in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "hello", "ejae", "choi")

# 기본 매개변수

def print_n_times(value, n=3):
    for i in range(n):
        print(value)

print_n_times("hello")
print()
print()
print_n_times("hello", 4) # n값을 주면 3이 들어가지 않는다