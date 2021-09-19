S = [input() for _ in range(3)]
T = input()

ans_list = [S[int(i)-1] for i in T]
ans = "".join(ans_list)
print(ans)
