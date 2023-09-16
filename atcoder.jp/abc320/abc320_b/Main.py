s = input()


def is_kaibun(s):
    s = list(s)
    return s == s[::-1]


ans = 0
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        s2 = s[i:j]
        if is_kaibun(s2):
            ans = max(ans, len(s2))

print(ans)
