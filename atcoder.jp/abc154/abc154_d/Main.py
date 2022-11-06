from itertools import accumulate

n, k = map(int, input().split())
p = list(map(int, input().split()))


def expectation(p):
    sum_1_to_p = p * (p + 1) // 2
    return sum_1_to_p / p


expectations = [expectation(p_i) for p_i in p]

accumulated = [0] + list(accumulate(expectations))

ans = float("-INF")
for i in range(n - k + 1):
    tmp = accumulated[i + k] - accumulated[i]
    ans = max(ans, tmp)

print(ans)
