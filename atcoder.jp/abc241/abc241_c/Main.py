n = int(input())
s = [input() for _ in range(n)]


def solve():
    for i in range(n):
        for j in range(n-5):
            cnt = 0
            for k in range(6):
                if s[i][j+k] == "#":
                    cnt += 1
            if cnt >= 4:
                return True

    for i in range(n-5):
        for j in range(n):
            cnt = 0
            for k in range(6):
                if s[i+k][j] == "#":
                    cnt += 1
            if cnt >= 4:
                return True

    for i in range(n-5):
        for j in range(n-5):
            cnt = 0
            for k in range(6):
                if s[i+k][j+k] == "#":
                    cnt += 1
            if cnt >= 4:
                return True

    for i in range(n-5):
        for j in range(5, n):
            cnt = 0
            for k in range(6):
                if s[i+k][j-k] == "#":
                    cnt += 1
            if cnt >= 4:
                return True
    return False


print("Yes" if solve() else "No")
