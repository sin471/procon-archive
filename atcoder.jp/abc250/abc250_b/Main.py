n, a, b = map(int, input().split())

line1 = line2 = ""
for i in range(n):
    if i % 2 == 0:
        line1 += "." * b
        line2 += "#" * b
    else:
        line1 += "#" * b
        line2 += "." * b


for i in range(a * n):
    ans = line1 if (i // a) % 2 == 0 else line2
    print(ans)
