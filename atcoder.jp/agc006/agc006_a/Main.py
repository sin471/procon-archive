n = int(input())
s = input()
t = input()

cnt = 0
min_st_length = min(len(s), len(t))
for i in range(min_st_length):
    if s[-i - 1 :] == t[: i + 1]:
        cnt = max(cnt, i + 1)


print(len(s) + len(t) - cnt)
