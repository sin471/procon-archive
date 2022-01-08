n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]


def find_dist(d, xi, xj):
    tmp = 0
    for i in range(d):
        tmp += (xi[i]-xj[i])**2
    return tmp**0.5

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        dist = find_dist(d,x[i], x[j])
        if dist.is_integer():
            cnt += 1

print(cnt)