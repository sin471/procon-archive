n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def solve():
    dp = [0]*n
    ep = [0]*n
    dp[0] = 1
    ep[0] = 1

    for i in range(1, n):
        #X_i-1=A_i-1の場合
        if dp[i-1]:
            if abs(a[i-1]-a[i]) <= k:
                dp[i] = 1

            if abs(a[i-1]-b[i]) <= k:
                ep[i] = 1

        #X_i-1=B_i-1の場合
        if ep[i-1]:
            if abs(b[i-1]-b[i]) <= k:
                ep[i] = 1

            if abs(b[i-1]-a[i]) <= k:
                dp[i] = 1

    return dp[-1] or ep[-1]


print("Yes" if solve() else "No")
