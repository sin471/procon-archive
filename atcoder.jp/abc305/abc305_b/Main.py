p, q = input().split()
if p > q:
    p, q = q, p

l = [3, 1, 4, 1, 5, 9]

ans = 0
for i in range(ord(p) - 65, ord(q) - 65):
    ans+=l[i]
    
print(ans)
