h, w = map(int, input().split())
print(["Imp","P"][sum(input().count("#") for _ in range(h))== h + w - 1]+"ossible")