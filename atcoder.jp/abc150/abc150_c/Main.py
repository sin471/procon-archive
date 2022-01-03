from itertools import permutations
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

p_list = sorted(list(permutations(p)))
q_list = sorted(list(permutations(q)))

for i, p_i in enumerate(p_list, 1):
    if p_i == p:
        break

for j, q_i in enumerate(q_list, 1):
    if q_i == q:
        break

print(abs(i-j))
