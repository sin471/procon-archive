from itertools import permutations

s, k = input().split()
k = int(k)

s_per = permutations(s)
ans_set = {"".join(i) for i in s_per}
ans_list = sorted(list(ans_set))
print(ans_list[k-1])
