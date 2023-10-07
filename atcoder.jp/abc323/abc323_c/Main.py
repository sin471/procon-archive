from operator import itemgetter

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [list(input()) for _ in range(n)]

# 現時点でのスコアを計算
scores = []
for i in range(n):
    s_i = s[i]
    x = 0
    for j in range(m):
        if s_i[j] == "o":
            x += a[j]

    x += i + 1
    scores.append(x)


# aを特典が高い順にソート．このときソート前のインデックスも保持
# [1000 500 700 2000]->[[2000,3],[1000,0],[700,2],[500,1]]
sorted_indexes_temp = sorted([[a_i, i] for i, a_i in enumerate(a)], reverse=True)
sorted_indexes = list(map(itemgetter(1), sorted_indexes_temp))

for i in range(n):
    ans = 0
    j = 0

    # 自分以外の中の最大値を求める
    score = scores[i]
    score2 = score
    scores[i] = 0
    max_ = max(scores)

    # xのうち得点が高いものから解いていく
    while max_ >= score2:
        should_solve = sorted_indexes[j]
        if s[i][should_solve] == "x":
            score2 += a[should_solve]
            ans += 1
        j += 1
    scores[i] = score

    print(ans)
