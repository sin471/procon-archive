n = int(input())

for i in range(100, 920):
    a = i // 100

    b = (i % 100) // 10
    c = i % 10

    if a * b == c and i >= n:
        print(a * 100 + b * 10 + c)
        break
