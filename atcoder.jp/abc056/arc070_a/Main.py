x = int(input())
for n in range(10**6):
    if x <= n * (n + 1) // 2:
        print(n)
        break
