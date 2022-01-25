from collections import deque

n=int(input())
a=list(map(int,input().split()))

a.sort()
q=deque(a)
ans=0

for i in range(n):
    q.popleft()
    q.pop()
    
    ans+=q.pop()

print(ans)