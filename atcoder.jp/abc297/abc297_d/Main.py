a, b = map(int, input().split())

cnt = 0
while b > 0:
    if a < b:
        a, b = b, a

    if a % b == 0:
        cnt += (a // b) - 1
        print(cnt)
        break

    cnt += a // b
    a %= b
