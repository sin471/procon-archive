n = int(input())

l = [[] for _ in range(37)]

for i in range(n):
    c_i = int(input())
    a_i = list(map(int, input().split()))

    for a_ij in a_i:
        l[a_ij].append((i, c_i))

x = int(input())

lis = sorted(l[x], key=lambda k: k[1])
if len(lis) == 0:
    print(0)
    exit()

m = lis[0][1]
ans_list = [i + 1 for i, c_i in lis if c_i == m]
print(len(ans_list))
print(*ans_list)
