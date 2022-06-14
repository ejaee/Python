times = int(input())
flag = 1
res = 0
k = list(map(int, input().split()))

for i in range(times):

    if k[i] == 0:
        flag = 1
    else:
        res += flag
        flag += 1
print(res)