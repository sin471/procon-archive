n = int(input())
a = list(map(int, input().split()))

ans = float("INF")
for x in range(-100, 101):
    ans = min(sum(map(lambda a_i: (a_i - x) ** 2, a)), ans)

print(ans)
