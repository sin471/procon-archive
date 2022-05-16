D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]

t = [int(input()) for _ in range(D)]

last_days = [0] * 365
satisfaction = 0


def decreasing_satisfaction_per_day(day: int):
    result = 0
    for constest_type in range(1, 26 + 1):
        days_since_last_contest = day - last_days[constest_type - 1]
        result += c[constest_type - 1] * days_since_last_contest

    return result


for day, constest_type in enumerate(t, 1):
    last_days[constest_type - 1] = day
    satisfaction += s[day - 1][constest_type - 1]
    satisfaction -= decreasing_satisfaction_per_day(day)
    print(satisfaction)
