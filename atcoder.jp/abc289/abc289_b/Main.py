n, m = map(int, input().split())
a = list(map(int, input().split()))

is_re = [1] + [0] * n

for a_i in a:
    is_re[a_i] = 1

is_seen = [1] + [0] * n

ans_list = []
for i in range(n + 1):
    if is_seen[i] == 1:
        continue

    j = i
    l = []
    is_seen[i] = 1
    l.append(i)
    while is_re[j]:
        j += 1
        is_seen[j] = 1
        l.append(j)

    ans_list.extend(l[::-1])

print(*ans_list)
