
# ----
print("---- 1. 텍스트 파일 처리 기본 ----\n")

# 파일은 텍스트 파일과 바이너리 파일로 나뉜다
# 텍스트 파일 : 텍스트 에디터(vscode)로 열 수 있다
# 바이너리 파일 : 없다 (이미지, 동영상, 워드, ...)

# 다루는 방법
# 1. 쓰기
# -     새로 쓰기 (write) w
# -     있는 파일 뒤에(append) a
# 2. 읽기 r

file = open("test.txt", "w") # w >> 파일을 새로 생성한다
file.write("파일 쓰기를 배워보기, ")
file.close()

# open과 CLOSE를 with를 통해 한방에 쓸 수 있다, 대표적인 케이스
with open("test2.txt", "w") as file:
    file.write("이렇게 open과 close를 함께 함축적으로 사용할 수 있다")
file = open("test2.txt", "r")
print(file.read)
print()

# ----

print("---- 2. generator ----\n")
# 제너레이터는 이터레이터를 직접 만들 때 사용하는 구문
# 함수 내부에 yield(산출하다, "양보하다") 키워드를 사용

def func():
    print("a")
    print("b")
    yield 100

제너레이터 = func()
print(제너레이터)
print()
res = next(제너레이터) # a, b 출력하고 100의 값을 res에 저장
print()
print(res) # 100
print("----\n")

def func2():
    print("A")
    yield 1 # stop
    print("B")
    yield 2 # stop
    print("C")
    yield 3 # stop
    print("D")
    yield 4 # stop

제너레이터2 = func2()
print(제너레이터2)
res2 = next(제너레이터2) # A 1
print(res2)
res2 = next(제너레이터2) # B 2
print(res2)
res2 = next(제너레이터2) # C 3
print(res2)
res2 = next(제너레이터2) # D 4
print(res2)

print("\n실제는 next 사용보다는 for문 사용\n")

제너레이터2 = func2()
for i in 제너레이터2:
    pass # yield가 끝날 때 까지 반복
print()

제너레이터2 = func2()
for i in 제너레이터2:   # i에는 값이 들어감
    print(i)    
for i in 제너레이터2:   # 한 번 끝났으므로 두번째는 아무것도 나오지 않음(일회성)
    print(i)

# 정리 : 제너레이터는 일회성. 메모리를 절약할 수 있음

# 심화
print()
def 반전(리스트):
    for i in range(len(리스트)):
        yield 리스트[-i - 1] # i = 0 > 리스트[-1], i = 1 > 리스트[-2] 이므로 뒤부터 선택 가능

제너레이터3 = 반전([1, 2, 3, 4, 5])
for i in 제너레이터3:
    print(i)
print()

# ----
print("---- 확인문제 1 ----")
