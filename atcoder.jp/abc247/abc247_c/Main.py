s_lis=[0]*17

def s(n):
  global s_lis
  if n==1:
    return [1]
  
  if s_lis[n-1]:
    s_n_1=s_lis[n-1]
  else:
    s_n_1=s(n-1)
    s_lis[n-1]=s_n_1

  return s_n_1+[n]+s_n_1

n=int(input())
print(*s(n))