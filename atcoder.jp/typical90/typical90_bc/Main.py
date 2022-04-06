n, p, q = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                for m in range(l+1, n):

                    result = 1
                    for x in [a[i], a[j], a[k], a[l], a[m]]:
                        result *= x
                        result %= p
                    if result == q:
                        cnt += 1

print(cnt)
