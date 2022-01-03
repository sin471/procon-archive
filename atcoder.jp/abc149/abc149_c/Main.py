x = int(input())

while True:
    y = int(x**0.5//1)
    for i in range(2, y):
        if x % i == 0:
            break
    else:
        print(x)
        exit()
    x += 1
