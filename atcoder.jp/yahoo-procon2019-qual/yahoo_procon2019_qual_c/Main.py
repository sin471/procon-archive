k, a, b = map(int, input().split())

bisket = 1

bisket += a - 1
k -= a - 1

diff = b - a
if diff >= 2:
    bisket += (k // 2) * diff
    bisket += k % 2
else:
    bisket += k

print(bisket)
