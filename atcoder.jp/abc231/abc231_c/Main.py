from bisect import bisect_left

n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]

a.sort()
for i in x:
    m = bisect_left(a, i)
    print(len(a)-m)
