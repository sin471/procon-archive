number_of_mochi = int(input())
diameter_of_mochi_list = [input() for _ in range(number_of_mochi)]
deduped_diameter_of_mochi_list = list(set(diameter_of_mochi_list))
print(len(deduped_diameter_of_mochi_list))
