n = int(input())
l = list(map(int, input().split()))
max_l = max(l)
print("Yes" if max_l < (sum(l)-max_l) else "No")
