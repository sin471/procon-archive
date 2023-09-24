def dfs(num):
    good_number.append(num)
    # 末尾の数よりも小さい数を新たに付け加える
    for i in range(0, num%10):
        nex = num*10 + i
        dfs(nex)


good_number = []
for i in range(1, 10):
    dfs(i)

good_number.sort()

K = int(input())
print(good_number[K - 1])
