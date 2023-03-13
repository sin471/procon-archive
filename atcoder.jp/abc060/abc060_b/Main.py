a, b, c = map(int, input().split())

k = 1
while True:
    if k * a % b == c:
        print("YES")
        exit()
    if k > b:
        print("NO")
        exit()
    k += 1
