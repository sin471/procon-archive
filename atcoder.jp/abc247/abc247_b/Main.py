n=int(input())
st=[input().split() for _ in range(n)]

def solve():
  for i in range(n):
    s_flag=False
    t_flag=False
    for j in range(n):
      if i==j:
        continue
      
      st_i,st_j=st[i],st[j]
      if st_i[0] in st_j:
        s_flag=True
      if st_i[1] in st_j:
        t_flag=True
        
    if s_flag and t_flag:
      return False
    
  return True

print("Yes" if solve() else "No")
    