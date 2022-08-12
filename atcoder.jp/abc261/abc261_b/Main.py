n=int(input())
a=[list(input()) for _ in range(n)]
def solve():
    d={"W":1,"D":2,"L":3}
    for i in range(n):
        for j in range(n):
            a_ij=a[i][j]
            a_ji=a[j][i]
            if i==j:
                continue
            
            if not d[a_ij]+d[a_ji]==4:
                return False
    return True

print("correct" if solve() else "incorrect")
