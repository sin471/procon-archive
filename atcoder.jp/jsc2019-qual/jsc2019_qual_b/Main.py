n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7

nums1 = [0] * n
nums2 = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            nums1[i] += 1

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            nums2[i] += 1

nums = [
    ((nums1[i] * k) % mod + (((k - 1) * k // 2) % mod) * nums2[i] % mod) % mod
    for i in range(n)
]

print(sum(nums) % mod)
