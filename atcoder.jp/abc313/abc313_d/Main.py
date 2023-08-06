n, k = map(int, input().split())


def ask(x):
    print("?", *[i + 1 for i in x], flush=True)
    return int(input())


ans = [-1] * n
seq = list(range(k + 1))

old = 0
ans[0] = 0

for i in range(k, -1, -1):
    res = ask(seq[:i] + seq[i + 1 :])
    if res == old:
        ans[i] = ans[(i + 1) % (k + 1)]
    else:
        ans[i] = (ans[(i + 1) % (k + 1)] + 1) % 2
    old = res

seq2 = list(range(n))
for i in range(k + 1, n):
    res = ask(seq2[i - k + 1 : i + 1])
    if res == old:
        ans[i] = ans[i - k]
    else:
        ans[i] = (ans[i - k] + 1) % 2
    old = res

if sum(ans[n - k :]) % 2 == old:
    print("!", *ans)
else:
    print("!", *[(i + 1) % 2 for i in ans])
