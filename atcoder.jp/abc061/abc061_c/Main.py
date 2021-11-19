n, k = map(int, input().split())

dict_ = {}

for _ in range(n):
    a, b = map(int, input().split())
    if a in dict_:
        dict_[a] = dict_[a]+b
    else:
        dict_[a] = b

sorted_dict = sorted(dict_.items())

index_ = 0

for tuple_ in sorted_dict:
    index_ += tuple_[1]
    if index_ >= k:
        print(tuple_[0])
        exit()
