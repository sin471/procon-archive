n, w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

taste = 0

ab.sort(key=lambda x: x[0], reverse=True)

for ai, bi in ab:
    if w-bi >= 0:
        taste += ai*bi
        w -= bi
    else:
        taste += w*ai
        break

print(taste)
