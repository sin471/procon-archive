n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]

for num in range(10**n):
    string = str(num)
    if len(string)!=n:
        continue
    
    for s, c in sc:
        if string[s-1] != str(c):
            break
    else:
        print(num)
        exit()

print(-1)
