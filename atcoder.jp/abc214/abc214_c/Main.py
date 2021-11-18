n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# sunuke[i]=i番目のsunukeが宝石を受け取る時刻の最小値
sunuke = [-1]*n

# sunuke[0]が最適解を持っている前提で、min((sunuke[i-1]+S[i-1]),T[i])を比較(1<=i=<n)
# 時刻sunuke[i-1]にi-1番目の人が"渡される"
# 時刻sunuke[i-1]+S(i-1)もしくはT[i]にsunuke[i]が"受け取る"(sunuke[i-1]もしくは高橋が渡す)

sunuke_0 = []

sum_si_to_sn = sum(s)

for i in range(n):
    sunuke_0.append(t[i]+sum_si_to_sn)
    sum_si_to_sn -= s[i]
else:
    sunuke_0[0] = t[0]

sunuke[0] = min(sunuke_0)

for i in range(1, n):
    sunuke[i] = min(sunuke[i-1]+s[i-1], t[i])

print(*sunuke, sep="\n")
