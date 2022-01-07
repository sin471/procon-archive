a = input()
b = input()

if len(a) > len(b):
    print("GREATER")
    exit()
elif len(a) < len(b):
    print("LESS")
    exit()

for i, j in zip(a, b):
    i, j = int(i), int(j)
    if i > j:
        print("GREATER")
        break
    elif i < j:
        print("LESS")
        break
    else:
        continue
else:
    print("EQUAL")
