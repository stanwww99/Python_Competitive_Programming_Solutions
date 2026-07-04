# Read two space-separated values from standard input and unpack them into N and K as strings
N, K = input().split()

# Convert N from string to integer so it can be used in numeric operations
N = int(N)

# Convert K from string to integer so it can be printed as a number (or used numerically if needed)
K = int(K)

# Loop from 0 up to N-2 (inclusive) which runs exactly N-1 times
for i in range(N - 1):
    # Print a zero followed by a space without adding a newline after each print call
    # end=" " ensures the outputs stay on the same line separated by a single space
    print(0, end=" ")

# After printing N-1 zeros and spaces, print K and terminate the line with the default newline
# This places K as the final value on the same line after the zeros
print(K)
