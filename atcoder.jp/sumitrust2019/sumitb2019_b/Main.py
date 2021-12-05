n = int(input())

for x in range(1, n+1):
    if x*1.08//1 == n:
        print(x)
        exit()
else:
    print(":(")
