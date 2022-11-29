from itertools import permutations

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = [list(map(int, input().split())) for _ in range(m)]

legs = permutations(range(n))

INF = float("INF")
ans = INF
for leg in legs:
    leg = list(leg)
    # i=runner_i,leg[i]=runner_i`s leg,
    for x, y in xy:
        if abs(leg[x - 1] - leg[y - 1]) == 1:
            break
    else:
        time = sum(a[runner_i][leg_i] for runner_i, leg_i in enumerate(leg))
        ans = min(time, ans)


print(-1 if ans == INF else ans)
