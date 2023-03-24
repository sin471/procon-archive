n, m = map(int, input().split())
cnt = min(n, m // 2)
m -= cnt * 2
cnt += m // 4

print(cnt)
