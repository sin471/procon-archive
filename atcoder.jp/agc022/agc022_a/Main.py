from string import ascii_lowercase

s = input()
set_ = set(s)
if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()
elif len(s) != 26:
    for i in ascii_lowercase:
        if i not in set_:
            print(s + i)
            break
else:
    l = []
    for i in range(len(s) - 1, -1, -1):
        l.append(s[i])
        if s[i] < max(l):
            l.sort()
            for j in range(len(s)):
                if l[j] > s[i]:
                    print(s[:i] + l[j])
                    exit()
