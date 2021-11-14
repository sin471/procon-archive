x,y=map(int,input().split("."))
sign=""
if 0<=y<=2:
  sign="-"
elif 7<=y<=9:
  sign="+"
print(f"{x}{sign}")
  