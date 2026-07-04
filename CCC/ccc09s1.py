import math

a = int(input())
b = int(input())
count = 0
square = int(math.sqrt(b))
cube = int(math.cbrt(b))
for i in range(int(math.sqrt(a)), square + 1):
    for j in range(int(math.cbrt(a)), cube + 1):
        if i**2 == j**3: #both square and cube number is cool
            count += 1
print(count)