import string
s = input()

alphabets = string.ascii_lowercase
flags_dict = {i: 0 for i in alphabets}

for si in s:
    if not flags_dict[si]:
        flags_dict[si] = 1

for i in alphabets:
    if not flags_dict[i]:
        print(i)
        exit()
print("None")
