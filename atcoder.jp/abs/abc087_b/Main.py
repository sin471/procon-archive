import itertools

number_of_500_yen_coins = int(input())
number_of_100_yen_coins = int(input())
number_of_50_yen_coins = int(input())
target_total_amount = int(input())

coins_list_of_500_yen = [i*500 for i in range(number_of_500_yen_coins+1)]
coins_list_of_100_yen = [i*100 for i in range(number_of_100_yen_coins+1)]
coins_list_of_50_yen = [i*50 for i in range(number_of_50_yen_coins+1)]

product_iter_of_coins = itertools.product(
    coins_list_of_500_yen, coins_list_of_100_yen, coins_list_of_50_yen)

count=0

for i in product_iter_of_coins:
    if sum(i)==target_total_amount:
        count+=1

print(count)