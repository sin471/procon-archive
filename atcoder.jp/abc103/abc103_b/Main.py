s=list(input())
t=list(input())

for i in range(len(s)):
  if s==t:
    print("Yes")
    break
  
  s.append(s.pop(0))
else:
  print("No")
