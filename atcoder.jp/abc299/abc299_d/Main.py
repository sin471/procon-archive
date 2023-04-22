n = int(input())

def ask(mid):
    print("? " + str(mid), flush=True)
    return int(input())


def bin_search():
    ok = n + 1
    ng = 0
    mid = (ok + ng) // 2

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        if ask(mid):
            ok = mid
        else:
            ng = mid

    return ng


print("! " + str(bin_search()), flush=True)
