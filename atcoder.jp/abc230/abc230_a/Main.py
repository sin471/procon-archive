n = int(input())
ans= str(n+1).zfill(3) if n>=42 else str(n).zfill(3)

print("AGC"+ans)