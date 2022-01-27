n = int(input())
a = list(map(int, input().split()))


def f(m):
    ans = 0
    for i in a:
        ans += m % i

    return ans


m = 1
for i in a:
    m *= i

print(f(m-1))
