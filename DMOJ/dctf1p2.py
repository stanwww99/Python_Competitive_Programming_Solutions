data = input().strip().split()
n = int(data[0])
a = int(data[1])
b = int(data[2])
m = int(data[3])

x = 0
result = 0

for i in range(n):
    x = (x * a + b) % m
    result ^= x

print(result)

#simulate the pseudocode given