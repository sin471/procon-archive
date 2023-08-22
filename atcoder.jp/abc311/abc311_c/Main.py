from sys import setrecursionlimit

setrecursionlimit(10**6)
n = int(input())
a = list(map(int, input().split()))

is_seen = [0] * n


def dfs(i, lis):
    if is_seen[i - 1]:
        ans = lis[lis.index(i) :]
        return ans
    lis.append(i)
    is_seen[i - 1] = 1
    return dfs(a[i - 1], lis)


ans = dfs(1, [])
print(len(ans))
print(*ans)
