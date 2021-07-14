def is_be_odd(a_list):
    mod_2_a_list = list(map(lambda a_list: a_list % 2, a_list))
    if 1 in mod_2_a_list:
        return True
    else:
        return False


n = int(input())
a_list = list(map(int, input().split()))
count = 0

while True:
    if is_be_odd(a_list):
        print(count)
        break
    a_list = list(map(lambda a_list:a_list/2, a_list))
    count += 1
