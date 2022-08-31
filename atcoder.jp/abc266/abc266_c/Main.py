a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))


def is_above_diagonal(p1,q1,q2):
    p1_x,p1_y=p1
    (q1_x,q1_y),(q2_x,q2_y)=q1,q2

    if (q1_x - q2_x) != 0:
        m = (q1_y - q2_y) / (q1_x - q2_x)

        return p1_y >= m * (p1_x - q1_x) + q1_y
    else:
        # 左にあるか
        return p1_x >= q1_x


def solve():
    is_separated_by_diagonal_bd=is_above_diagonal(a,b,d) != is_above_diagonal(c,b,d)
    is_separated_by_diagonal_ac=is_above_diagonal(b,a,c)!=is_above_diagonal(d,a,c)
    return is_separated_by_diagonal_bd and is_separated_by_diagonal_ac


print("Yes" if solve() else "No")
