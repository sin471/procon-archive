h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

remove_rows = set()
for i, grid_i in enumerate(grid):
    if all(map(lambda x: True if x == "." else False, grid_i)):
        remove_rows.add(i)


remove_columns = set()
grid2 = zip(*grid)
for i, grid2_i in enumerate(grid2):
    if all(map(lambda x: True if x == "." else False, grid2_i)):
        remove_columns.add(i)

flag = False
for i, grid_i in enumerate(grid):
    for j, grid_ij in enumerate(grid_i):
        if i in remove_rows:
            break
        if j in remove_columns:
            continue
        print(grid_ij, end="")
        
    else:
        print()
