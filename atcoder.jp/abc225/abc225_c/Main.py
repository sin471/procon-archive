n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

b00 = b[0][0]
for i in range(n):
    for j in range(m):
        if b00+i*7+j == b[i][j]:
            if b[i][j] % 7 == 0 and j != m-1:
                print("No")
                exit()
        else:
            print("No")
            exit()
print("Yes")
