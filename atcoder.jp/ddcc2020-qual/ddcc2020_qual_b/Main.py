from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

s = accumulate(a)
ave = sum(a)/2
diff = float("INF")

for i in s:
    diff = min(abs(i-ave), diff)

print(int(diff*2))
