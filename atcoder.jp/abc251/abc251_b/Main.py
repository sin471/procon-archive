n, w = map(int, input().split())
a = list(map(int, input().split()))

good = set()


def f(set_, x):
    if x <= w:
        set_.add(x)
    return set_


for i in range(n):
    a_i = a[i]
    for j in range(i + 1, n):
        a_j = a[j]
        for k in range(j + 1, n):
            a_k = a[k]
            good = f(good, a_i + a_j + a_k)

for i in range(n):
    a_i = a[i]
    for j in range(i + 1, n):
        a_j = a[j]
        good = f(good, a_i + a_j)

for i in range(n):
    a_i = a[i]
    good = f(good, a_i)

print(len(good))
