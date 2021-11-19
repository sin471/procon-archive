s_l = input()
o_list = []
x_list = []
ques_list = []

cnt = 0

for i, char in enumerate(s_l):
    if char == "o":
        o_list.append(i)
    elif char == "x":
        x_list.append(i)
    else:
        ques_list.append(i)

set_o = set(o_list)
set_x = set(x_list)

range10 = range(10)
for i in range10:
    for j in range10:
        for k in range10:
            for l in range10:
                password = [i, j, k, l]
                set_password = set(password)
                if set_o <= set_password and set_x & set_password == set():
                    cnt += 1

print(cnt)
