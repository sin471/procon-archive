n, q = map(int, input().split())
x = [int(input()) for _ in range(q)]

d = {value: index for index, value in enumerate(range(1, n + 1))}
l = list(range(1, n + 1))
for x_i in x:
    index = d[x_i]
    if index == n - 1:
        index -= 1
    d[l[index]] += 1
    d[l[index + 1]] -= 1
    l[index], l[index + 1] = l[index + 1], l[index]


print(*l)