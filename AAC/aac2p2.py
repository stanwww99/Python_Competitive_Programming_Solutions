import sys

# Read number of elements
N = int(input())

# Read list of integers
l = list(map(int, input().split()))

# Convert list to a set for O(1) average lookup time
k = set(l)

# Default answer is 2 (minimum number of bowls needed)
count = 2

# Special case: if there are exactly 2 numbers
if N == 2:
    # If their average is an integer (sum is even), both endpoints + midpoint exist → answer is 2
    if (l[0] + l[1]) % 2 == 0:
        print(2)
        sys.exit()
    else:
        # Otherwise only 1 bowl  can be chosen
        print(1)
        sys.exit()

# For N ≥ 3, check if any pair has an integer bowl  present in the set
for i in range(0, N - 1):
    for j in range(i + 1, N):
        # Check if midpoint exists in the set
        # Note: (l[i] + l[j]) / 2 may be float; set contains ints, so if integer bowl could be 3
        if k.__contains__((l[i] + l[j]) / 2):
            count = 3

# Output the result
print(count)
