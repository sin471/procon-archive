s = input()
a, b, c = s[0], s[1], s[2]

abc = int(a+b+c)
bca = int(b+c+a)
cab = int(c+a+b)
print(abc+bca+cab)
