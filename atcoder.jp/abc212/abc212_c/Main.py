import bisect
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = float("Inf")
x, y = float("Inf"), float("Inf")
a.sort()
b.sort()

for ai in a:
    ind = bisect.bisect(b, ai)
    if ind < m:
        x = abs(ai-b[ind])
    if ind-1 >= 0:
        y = abs(ai-b[ind-1])
    ans_i = min(x, y)
    if ans_i < ans:
        ans = ans_i

print(ans)
