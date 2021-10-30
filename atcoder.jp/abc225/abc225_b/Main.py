n=int(input())
ab=[list(map(int,input().split())) for _ in range(n-1)]

x=set(ab[0])&set(ab[1])
for item in ab:
    y=set(item)&x
    if not y:
        print("No")
        exit()

print("Yes")