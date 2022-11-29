n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

abc = [a, b, c]
for i in range(3):
    abc[i] = list(map(lambda x: x % 46, abc[i]))

count_buckets = [[0] * 46 for _ in range(3)]

for i in range(3):
    for l_j in abc[i]:
        count_buckets[i][l_j] += 1


a_count_bucket = count_buckets[0]
b_count_bucket = count_buckets[1]
c_count_bucket = count_buckets[2]
ans = 0

for i, a_count in enumerate(a_count_bucket):
    for j, b_count in enumerate(b_count_bucket):

        c_count = c_count_bucket[-(i + j) % 46]
        ans += a_count * b_count * c_count

print(ans)
