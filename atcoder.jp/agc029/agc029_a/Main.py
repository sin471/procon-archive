s=input()

left=0
cnt=0

for i,s_i in enumerate(s):
    if s_i=="W":
        cnt+=i-left
        left+=1

print(cnt)
