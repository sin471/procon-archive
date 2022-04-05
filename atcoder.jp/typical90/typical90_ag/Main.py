from math import ceil
h, w = map(int, input().split())


if h==1 or w==1:
    print(max(h,w))
else:
    print(ceil(h/2)*ceil(w/2))
