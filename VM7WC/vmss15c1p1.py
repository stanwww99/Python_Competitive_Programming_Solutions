import math

# Read the area A from input (1 <= A <= 1_000_000).
A = int(input())

# Start from the integer square root of A.
# The optimal rectangle with integer sides will have one side <= sqrt(A).
start = int(math.sqrt(A))

# Decrease start until we find a divisor of A.
# The first divisor we find (closest to sqrt(A)) gives the pair (start, A//start)
# that minimizes the perimeter.
while True:
    if A % start == 0:
        # found an integer side length 'start' that divides A
        break
    else:
        # try the next smaller integer
        start -= 1

# Perimeter of rectangle with sides start and A//start is 2*(start + A//start)
print(start * 2 + (A // start) * 2)
