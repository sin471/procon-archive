n = int(input())
s = [input() for _ in range(n)]

def solve_overlap(t_list):
    #重複があった場合、リールをn周(+10n)させる
    overlap_cnt_list = [0] * 10

    for i,ele in enumerate(t_list):

        overlap_cnt = overlap_cnt_list[ele]
        if overlap_cnt:
            t_list[i] += 10 * overlap_cnt

        overlap_cnt_list[ele] += 1
    return t_list

ans = float("INF")
for reel in range(10):
    # t_list[i]:=S_iの数字をreelに揃えるときの最短のt
    t_list = [-1] * n

    for i in range(n):
        t_list[i] = s[i].index(str(reel))

    t_list2 = solve_overlap(t_list)

    ans = min(max(t_list2), ans)

print(ans)
