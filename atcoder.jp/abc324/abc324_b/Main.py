n = int(input())

while n != 1:
    if n % 2 == 0:
        n //= 2
    elif n % 3 == 0:
        n //= 3
    else:
        print("No")
        exit()

print("Yes")
