n = int(input())
p = list(map(int, input().split()))

x = p[0]
p.remove(x)
print(max(max(p, default=-100) - x + 1, 0))
