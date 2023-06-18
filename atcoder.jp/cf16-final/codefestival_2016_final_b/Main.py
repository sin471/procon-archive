n = int(input())

# k(k+1)//2>=nを満たす最小のkを考える

for k in range(1, 10**7 + 1):
    e = k * (k + 1) // 2
    if e >= n:
        l = list(range(1, k + 1))
        if e - n != 0:
            del l[e - n - 1]
        print(*l)
        exit()
