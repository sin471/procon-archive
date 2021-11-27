a, b = input().split()

for ai, bi in zip(a[::-1], b[::-1]):
    ai = int(ai)
    bi = int(bi)
    if ai+bi >= 10:
        print("Hard")
        exit()

print("Easy")
