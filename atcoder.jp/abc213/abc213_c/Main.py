H, W, N = map(int, input().split())


X, Y = [], []

for i in range(N):
    ai, bi = map(int, input().split())
    X.append(ai)
    Y.append(bi)

X2 = list(set(X))
Y2 = list(set(Y))

Xdict = {v: i+1 for i, v in enumerate(sorted(X2))}
Ydict = {v: i+1 for i, v in enumerate(sorted(Y2))}

for i in range(N):
    print(Xdict[X[i]], Ydict[Y[i]])
