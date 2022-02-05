def solve(n):
    if n==1:
        return True
    if n<=4:
        return False
    else:
        return True

print("Yes" if solve(int(input())) else "No")