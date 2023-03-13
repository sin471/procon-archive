s = input()
n = len(s) + 1

s2 = ">" + s + "<"

a = [-1] * n
for i in range(n):
    if s2[i] == ">" and s2[i + 1] == "<":
        a[i] = 0

for i in range(n):
    if a[i] == 0:
        j = i
        while j <= n - 2 and s[j] == "<":
            a[j + 1] = max(a[j] + 1, a[j + 1])
            j += 1
        j = i
        while 1 <= j and s[j - 1] == ">":
            a[j - 1] = max(a[j] + 1, a[j - 1])
            j -= 1

print(sum(a))
