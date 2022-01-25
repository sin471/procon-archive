n, m = map(int, input().split())

ps = []
for i in range(m):
    p, s = input().split()
    p = int(p)
    ps.append([p, s])

penalty = 0
ac_flags = [0]*n
wa_list = [0]*n

for p, s in ps:
    if s == "AC":
        ac_flags[p-1] = 1

    elif s == "WA":
        if not ac_flags[p-1]:
            wa_list[p-1] += 1

for i in range(n):
    if ac_flags[i]:
        penalty += wa_list[i]

ac = sum(ac_flags)
print(ac, penalty)
