# Read the first integer from input
x = int(input())

# Read the second integer from input
y = int(input())

# Compute the raw product of the two integers
product = x * y

# Apply 32‑bit signed integer wrapping:
#   1. Add 2**31 to shift into a non-negative range
#   2. Take modulo 2**32 to simulate 32‑bit overflow behavior
#   3. Subtract 2**31 to shift back into signed integer range (-2^31 to 2^31-1)
result = (product + 2**31) % (2**32) - 2**31

# Output the wrapped result
print(result)
