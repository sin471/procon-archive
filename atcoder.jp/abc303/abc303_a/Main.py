n = int(input())
s = input()
t = input()
d = {"0": "o", "o": "0", "1": "l", "l": "1"}

for i in range(n):
    if s[i] == t[i] or d.get(s[i], None) == t[i]:
        pass
    else:
        print("No")
        exit()
print("Yes")
