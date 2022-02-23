x1, y1, x2, y2 = map(int, input().split())

# (x1-a)**2+(y1-b)**2==5
# (x2-a)**2+(y2-b)**2==5
# を同時に満たす円の中心、整数a,bは存在するか


def solve():
    for a in range(x1-5, x1+6):
        for b in range(y1-5, y1+6):
            if (x1-a)**2+(y1-b)**2 == 5:
                if (x2-a)**2+(y2-b)**2 == 5:
                    return True
    return False


print("Yes" if solve() else "No")
