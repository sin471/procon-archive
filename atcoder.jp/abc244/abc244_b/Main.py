n = int(input())
t = input()
direction = ((1, 0), (0, -1), (-1, 0), (0, 1))

positon = [0, 0]
cnt = 0
for i in t:
    d = direction[cnt % 4]
    if i == "S":
        positon[0] += d[0]
        positon[1] += d[1]
    elif i == "R":
        cnt += 1

print(*positon)