from itertools import permutations

n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]

dists = dict()
for a, b, c in abc:
    dists[(a, b)] = c
    dists[(b, a)] = c


ans = 0
temp = 0

for perm in permutations(range(1, n+1)):
    temp = 0
    for i in range(1, n):
        
        c = dists.get((perm[i - 1], perm[i]))
        if c is None:
            break
        temp += c
    ans = max(ans, temp)

print(ans)
