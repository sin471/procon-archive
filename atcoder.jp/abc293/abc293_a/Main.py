s = input()

l = []
for i in range(len(s) // 2):
    l.append(s[2 * i + 1])
    l.append(s[2 * i])

print("".join(l))
