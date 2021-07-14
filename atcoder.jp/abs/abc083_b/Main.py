n, a, b = map(int, input().split())

within_range_of_AtoB_list = []
for i in range(n+1):
    # 各位の和を求めるため一桁ごとに分割
    split_i_into_digit_list = list(map(int, list(str(i))))
    # 各位の和を求める
    digit_sum_of_i = sum(split_i_into_digit_list)
    # 該当範囲a以上b以下
    if a <= digit_sum_of_i <= b:
        # 該当する数をリストに入れる
        within_range_of_AtoB_list.append(i)

print(sum(within_range_of_AtoB_list))
