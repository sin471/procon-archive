n, k = map(int, input().split())

n %= k

while True:
    next_n = abs(n-k)
    if next_n < n:
        n = next_n
    else:
        break

print(n)
