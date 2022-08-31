n = int(input())
a, b, c = map(int, input().split())

min_ = float("INF")
for i in range(10000):
    for j in range(10000):
        remains = n - (a * i + b * j)
        if 0 <= remains and (remains % c == 0):
            min_ = min((i + j + remains // c), min_)

        if a * i + b * j > n:
            break

print(min_)
