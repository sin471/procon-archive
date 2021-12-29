n = int(input())
d = list(map(int, input().split()))

d.sort()

k_min = d[n//2-1]
k_max = d[n//2]

print(k_max-k_min)
