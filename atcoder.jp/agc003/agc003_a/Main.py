s=input()
N,W,S,E=0,0,0,0

if "N" in s:
  N=1
if "W" in s:
  W=1
if "S" in s:
  S=1
if "E" in s:
  E=1  

if not (N^S or W^E):
    print("Yes")
else:
    print("No")