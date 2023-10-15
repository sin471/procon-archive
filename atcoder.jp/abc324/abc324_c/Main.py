def check(s, t):
    if len(s) > len(t):
        s, t = t, s

    if len(s) + 1 < len(t):
        return False

    i = j = miss = 0

    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            miss += 1
            if miss > 1:
                return False
            j += 1
            if len(s) == len(t):
                i += 1
    return True


n, t = input().split()
n = int(n)
ans = []
for i in range(n):
    s = input()
    if check(s, t):
        ans.append(i + 1)

print(len(ans))
print(*ans)
