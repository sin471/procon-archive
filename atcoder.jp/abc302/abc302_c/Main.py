from itertools import permutations

n, m = map(int, input().split())
s = [input() for _ in range(n)]


def dist(a, b):
    cnt = 0
    for i in range(m):
        if a[i] != b[i]:
            cnt += 1
    return cnt


def almost_equal(s):
    for i in range(1, n):
        if dist(s[i - 1], s[i]) > 1:
            return False
    return True


for p in permutations(s):
    if almost_equal(p):
        print("Yes")
        exit()
print("No")
