n = int(input())
a = list(map(int, input().split()))
a.sort()


def runlength(a):
    before = a[0]
    cnt = 0
    l = [0] * (a[-1] + 1)
    for a_i in a:
        if a_i == before:
            cnt += 1
        else:
            l[before] = cnt
            before = a_i
            cnt = 1

    l[before] = cnt
    return l


l = runlength(a)
ans = 0
for i in range(len(l)):
    temp = l[i]
    if 0 < i:
        temp += l[i - 1]
    if i + 1 < len(l):
        temp += l[i + 1]

    ans = max(temp, ans)

print(ans)
