from math import ceil


a, b, c = map(int, input().split())
abc = [a, b, c]

abc.sort(reverse=True)

max_second_diff = abc[0]-abc[1]

abc[1] += max_second_diff
abc[2] += max_second_diff
cnt = max_second_diff

max_min_diff = abc[0]-abc[2]

if max_min_diff % 2 == 0:
    cnt += (max_min_diff)//2
else:
    cnt += ceil(max_min_diff/2)
    cnt += 1

print(cnt)
