s = input()

l = []
for i, s_i in enumerate(s):
    if s_i == "B":
        l.append(i % 2)

if sum(l) != 1:
    print("No")
    exit()

flag = False

for s_i in s:
    if s_i == "R" and not flag:
        flag = True
    elif s_i == "R" and flag:
        flag = False
        print("No")
        exit()
    elif flag and s_i == "K":
        print("Yes")
        exit()
