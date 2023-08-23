n,m=map(int,input().split())
pcf=[]
for i in range(n):
	p,c,*f=list(map(int,input().split()))
	pcf.append([p,c,set(f)])


def solve():
	for i in range(n):
		for j in range(n):
			p_i,_,f_i=pcf[i]
			p_j,_,f_j=pcf[j]
			if (p_i<p_j and f_i>=f_j) or (p_i<=p_j and f_i>f_j):
				return True
	return False
				
		

print("Yes" if solve() else "No")