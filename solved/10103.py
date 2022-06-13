times = int(input())
chang = 100
shang = 100
for i in range(times):
    a, b = map(int, input().split())
    if a > b:
        shang -= a
    elif a < b:
        chang -= b

#print(chang)
#print(shang)
print(chang, shang, sep = "\n")