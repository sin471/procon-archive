N = int(input())
t_list = [0]
x_list = [0]
y_list = [0]
A = 'Yes'
for i in range(N):
    ti, xi, yi = map(int, input().split())
    t_list.append(ti)
    x_list.append(xi)
    y_list.append(yi)
    if ((abs(x_list[i+1] - x_list[i]) + abs(y_list[i+1] - y_list[i]) > (t_list[i+1] - t_list[i]))):
        A = 'No'
        break
    if (x_list[i+1] + y_list[i+1] - t_list[i+1])%2 != 0:
        A = 'No'
        break
print(A)