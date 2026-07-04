# Determine whether the second string is a wildcard anagram of the first string.
# A wildcard '*' in s2 can represent ANY character.

import sys
from collections import Counter

# Read the two input strings
s1 = input()
s2 = input()

# If lengths differ, s2 can never be an anagram of s1 (even with wildcards)
if len(s1) != len(s2):
    print('N')
    sys.exit()

# Count frequency of each character in both strings
s1 = Counter(s1)
s2 = Counter(s2)

# s3 will track how many characters from s1 still need to be matched
s3 = dict()

# Initialize s3 with counts from s1
for i in s1:
    s3[i] = s1[i]

# Subtract counts of actual characters in s2 (ignore wildcards '*')
for i in s2:
    if i != '*':
        # Reduce the needed count for this character
        s3[i] = s3.get(i, 0) - s2[i]

# If any count goes negative, s2 uses a character more times than s1 has
for i in s3:
    if s3[i] < 0:
        print('N')
        sys.exit()

# If no conflicts, wildcards can fill the remaining gaps → valid wildcard anagram
print('A')
