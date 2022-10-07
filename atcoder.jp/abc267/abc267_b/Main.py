s = input()

if s[0] == "1":
    print("No")
    exit()

column = [["7"], ["4"], ["2", "8"], ["1", "5"], ["3", "9"], ["6"], ["10"]]

is_column_stood = [""] * 7


for i in range(7):
    is_stood = False
    for j in column[i]:
        if s[int(j) - 1] == "1":
            is_stood = True
            break

    is_column_stood[i] = "1" if is_stood else "0"

for i in range(1, 6):
    if is_column_stood[i] == "0":
        if "1" in is_column_stood[:i] and "1" in is_column_stood[i + 1 :]:

            print("Yes")
            exit()
print("No")
