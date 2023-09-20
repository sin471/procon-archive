n = int(input())
a = list(map(int, input().split()))

ans = 1
INF = 10**18

if 0 in a:
    print(0)
    exit()

for i in range(n):
    if ans > INF // a[i]:
        print(-1)
        exit()
    ans *= a[i]

print(ans)
