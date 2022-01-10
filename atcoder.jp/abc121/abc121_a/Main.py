H,W=map(int,input().split())
h,w=map(int,input().split())

black=(h*W+H*w)-h*w

print(H*W-black)