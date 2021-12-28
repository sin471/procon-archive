k, n = map(int, input().split())
a = list(map(int, input().split()))

a.append(a[0]+k)
dist = float("-Inf")

for i in range(n):
    dist=max(dist,a[i+1]-a[i])

print(k-dist)