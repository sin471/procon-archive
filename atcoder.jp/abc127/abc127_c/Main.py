n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

can_through = [float("-INF"), float("INF")]
cnt = 0

for l, r in lr:
    can_through[0] = max(can_through[0], l)
    can_through[1] = min(can_through[1], r)

if can_through[0]<=can_through[1]:
    print(can_through[1]-can_through[0]+1)
else:
    print(0)

