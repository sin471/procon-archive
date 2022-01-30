h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

b = [i for i in zip(*a)]

for i in b:
    print(*i)
