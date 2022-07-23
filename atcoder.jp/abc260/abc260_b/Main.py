n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = [a_i + b_i for a_i, b_i in zip(a, b)]

lists = [a, b, ab]
lists_and_indexes = []

for list_ in lists:
    list_and_indexes = [[list_i, -i] for i, list_i in enumerate(list_)]
    lists_and_indexes.append(list_and_indexes)

for list_and_indexes in lists_and_indexes:
    list_and_indexes.sort(reverse=True)

indexes_lists=[]
for list_and_indexes in lists_and_indexes:
    indexes=[-i for _,i in list_and_indexes]
    indexes_lists.append(indexes)

flags = [0] * n

xyz=[x,y,z]
for xyz_i,indexes in zip(xyz,indexes_lists):
    cnt = 0
    for index in indexes:
        if cnt == xyz_i:
            break
        if not flags[index]:
            flags[index] = 1
            cnt += 1


for i in range(n):
    if flags[i]:
        print(i + 1)
