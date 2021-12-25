import math
x, y = map(int, input().split())
ans = 0
if x < y:
    ans = math.ceil((y-x)/10)

print(ans)
