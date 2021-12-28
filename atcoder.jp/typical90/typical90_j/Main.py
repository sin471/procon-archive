n = int(input())
cp = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

class1 = [0]
class2 = [0]
for cp_i in cp:
    if cp_i[0] == 1:
        class1.append(class1[-1]+cp_i[1])
        class2.append(class2[-1])
    elif cp_i[0] == 2:
        class1.append(class1[-1])
        class2.append(class2[-1]+cp_i[1])


for l, r in lr:
    class1_sum = class1[r]-class1[l-1]
    class2_sum = class2[r]-class2[l-1]
    print(class1_sum, class2_sum)
