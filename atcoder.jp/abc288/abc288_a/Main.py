n = int(input())

ab = [list(map(int, input().split())) for _ in range(n)]

for a_i, b_i in ab:
    print(a_i + b_i)
