n = int(input())
s = input()

char1 = s[0]
char2 = "F" if char1 == "M" else "M"

for i in range(n):
    if i % 2 == 0:
        if s[i] != char1:
            break
    elif i % 2 == 1:
        if s[i] != char2:
            break
else:
    print("Yes")
    exit()

print("No")
