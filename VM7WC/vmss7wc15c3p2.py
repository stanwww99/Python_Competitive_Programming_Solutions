N, K =  map(int, input().split())
l = list()
for i in range(N):
    l.append(int(input()))
l = sorted(l)
l.reverse()
sums = 0
for i in range(min(N, K)):
    sums += max(0, l[i])  #no add negative score
print(sums)