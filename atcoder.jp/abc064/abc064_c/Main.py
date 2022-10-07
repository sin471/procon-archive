n = int(input())
a = list(map(int, input().split()))

colors_lessthan_3200 = {i // 400 for i in a if i < 3200}
if all(map(lambda x:x>=3200,a)):
    print(1,len(a))
    exit()

min_ = len(colors_lessthan_3200)
max_ = min_ + len(list(filter(lambda x: x >= 3200, a)))
print(min_, max_)
