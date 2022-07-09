n,x=map(int,input().split())

cnt=0
for i in range(26):
    for _ in range(n):
        cnt+=1
        if cnt==x:
            print(chr(65+i))

