from itertools import groupby

s = input()
k = int(input())
if len(set(s)) == 1:
    print(len(s) * k // 2)
    exit()


def runlength(iter_):
    l = []
    for key, g in groupby(iter_):
        l.append([key, len(list(g))])
    return l


x = 0
l = runlength(s)
for i, cnt in l:
    if i != 1:
        x += cnt // 2

ans = x * k
if s[0] != s[-1]:
    print(ans)
else:
    head_cnt = l[0][1]
    tail_cnt = l[-1][1]

    tmp = (head_cnt // 2 + tail_cnt // 2 - (head_cnt + tail_cnt) // 2) * (k - 1)
    print(ans - tmp)
