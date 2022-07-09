n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

box = [0] * n
for a_i in a:
    box[a_i - 1] = 1

for l_i in l:
    flag_cnt = k + 1
    for j in range(n - 1, -1, -1):
        if not box[j]:
            continue
        
        flag_cnt -= 1

        if flag_cnt == l_i and j != n - 1 and (not box[j + 1]):
            box[j] = 0
            box[j + 1] = 1

for i in range(n):
    if box[i]:
        print(i + 1,end=" ")
