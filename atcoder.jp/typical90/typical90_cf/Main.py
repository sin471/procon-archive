n = int(input())
s = input()

rle = []
now = s[0]
cnt = 0
for s_i in s:
    if s_i == now:
        cnt += 1
    else:
        rle.append(cnt)
        cnt = 1
        now = s_i
rle.append(cnt)

sum_rle = [0]
for i in range(len(rle)):
    sum_rle.append(rle[i] + sum_rle[-1])

ans = 0
for i in range(len(rle)):
    ans += rle[i] * (sum_rle[-1] - sum_rle[i + 1])

print(ans)
