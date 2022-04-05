def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        cnt += abs(a[i]-b[i])

    if cnt > k:
        return False

    if cnt == k:
        return True

    if cnt < k and (k-cnt) % 2 == 0:
        return True
    else:
        return False

print("Yes" if solve() else "No")