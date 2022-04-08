n = int(input())

for bit in range(2**n-1, -1, -1):
    lis = []
    l, r = 0, 0
    for i in range(n-1, -1, -1):
        if bit & (2**i):
            lis.append("(")
            l += 1
        else:
            lis.append(")")
            r += 1

        if l < r:
            break
    else:
        if l == r:
            print("".join(lis))
