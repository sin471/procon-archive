from collections import Counter

n = int(input())
a = Counter(map(int, input().split()))

ans = 0
for key, val in a.items():
    if key < val:
        ans += val - key
    elif key > val:
        ans += val

print(ans)
