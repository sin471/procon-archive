n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))


def solve():
    if n < m:
        return False

    dic = dict()
    for d_i in d:
        dic.setdefault(d_i, 0)
        dic[d_i] += 1

    for t_i in t:
        dic.setdefault(t_i, 0)
        dic[t_i] -= 1
        if dic[t_i] < 0:
            return False

    return True


print("YES" if solve() else "NO")
