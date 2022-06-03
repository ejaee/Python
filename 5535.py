t = int(input())
for i in range(t):
    mars = list(map(str, input().split()))
    n = 0
    for j in range(len(mars)):
        if mars[j] == "@":
            n *= 3
        elif mars[j] == "%":
            n += 5
        elif mars[j] == "#":
            n -= 7
        else:
            n = float(mars[j])
    print("%.2f" %n)