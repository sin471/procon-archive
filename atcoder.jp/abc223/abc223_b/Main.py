s = list(input())
i = s.index(max(s))
j = s.index(min(s))
l = []
for i in range(len(s)):
    s.insert(0, s.pop(-1))
    l.append("".join(s))

print(min(l))
print(max(l))
