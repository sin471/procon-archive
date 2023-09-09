n, m = map(int, input().split())
l = list(map(int, input().split()))


def calc_row(w):
    cnt = 0
    row = 1
    for l_i in l:
        if cnt + l_i > w:
            cnt = l_i + 1
            row += 1

        elif cnt + l_i <= w:
            cnt += l_i + 1
    return row


ok = 10**16
ng = max(l) - 1

while abs(ok - ng) > 1:
    w = (ok + ng) // 2
    if m >= calc_row(w):
        ok = w
    else:
        ng = w

print(ok)
