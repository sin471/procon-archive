n, k, x = map(int, input().split())
a = list(map(int, input().split()))


for i in range(n):
    if k*x < a[i]:
        a[i] -= k*x
        k = 0
        continue
    k -= a[i]//x
    a[i] %= x

a.sort(reverse=True)
for i in range(min(k, n)):
    a[i] = 0

print(sum(a))
