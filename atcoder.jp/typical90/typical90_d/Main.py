import itertools

H, W = map(int, input().split())

rangeH,rangeW=list(range(H)),list(range(W))

hw = [list(map(int, input().split())) for _ in rangeH]

# 横一列
sum_row = [sum(i) for i in hw]
# 縦一列
sum_column = [sum(i) for i in zip(*hw)]

orthogonal_sum = [row+column
                    for row in sum_row for column in sum_column]

hw=itertools.chain.from_iterable(hw)

ans_list=map(lambda x,y:x-y,orthogonal_sum,hw)

for i, j in enumerate(ans_list, 1):
    if i % W == 0:
        print(j, end="\n")
    else:
        print(j, end=" ")
