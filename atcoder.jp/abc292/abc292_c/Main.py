from math import ceil,floor, sqrt

n = int(input())

# AB=kとなる(A,B)の組の数を各k(1<=k<N)について求める
# A<Bとするとfloor(sqrt(A))まで調べれば十分

cnts_k = [0] * n
cnts_k[1] = 1

for k in range(2, n):
    # 必ずa<sqrt(k)を満たすので、a<b
    for a in range(1, ceil(sqrt(k))):
        if k % a != 0:
            continue

        # (A,B)と(B,A)の2組があるので2ずつ加算
        cnts_k[k] += 2

    # A=B,AB=kとなるとき、個別に1加算
    if sqrt(k).is_integer():
        cnts_k[k] += 1

ans = 0
for i in range(1, n):
    ans += cnts_k[i] * cnts_k[n - i]

print(ans)
