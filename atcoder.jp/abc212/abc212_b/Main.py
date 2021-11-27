x = input()

if len(set(x)) == 1:
    print("Weak")
    exit()

for i in range(1, len(x)):
    if (int(x[i-1])+1) % 10 == int(x[i]):
        continue
    else:
        print("Strong")
        exit()
else:
    print("Weak")


