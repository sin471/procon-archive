v, a, b, c = map(int, input().split())
v %= (a+b+c)
for i in [[a, "F"], [b, "M"], [c, "T"]]:
    v -= i[0]
    if v < 0:
        print(i[1])
        break
