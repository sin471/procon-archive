n = int(input())
s = input()
i = 0
x = s[0]
cnt = 0
d = dict()

while i < n:
    if s[i] == x:
        i += 1
        cnt += 1
    else:
        d[x] = max(d.get(x, 0), cnt)
        x = s[i]
        cnt = 0
else:
    d[x] = max(d.get(x, 0), cnt)
    
print(sum(i for i in d.values()))
