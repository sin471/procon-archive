from collections import Counter

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

l = []
for i in range(h):
    inner = []
    for j in range(w - 1):
        if s[i][j] == s[i][j + 1] == "T":
            s[i][j] = "P"
            s[i][j + 1] = "C"
        
        inner.append(s[i][j])
    
    inner.append(s[i][-1])
    l.append(inner)

for i in l:
    print("".join(i))
