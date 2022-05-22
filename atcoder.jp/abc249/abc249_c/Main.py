from string import ascii_lowercase

n, k = map(int, input().split())
s = [input() for _ in range(n)]

outer_list = []
for i in range(2**n):
    inner_list = []
    for j in range(n):
        if i & (1 << j):
            inner_list.append(s[j])
    outer_list.append(inner_list)

ans = 0

for lis in outer_list:
    cnt = 0
    string = "".join(lis)
    for char in ascii_lowercase:
        if string.count(char) == k:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
