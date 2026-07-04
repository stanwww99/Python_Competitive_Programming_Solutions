print(str(-len(input())%8>3).lower())
# Compute the negative length modulo 8
# -len(s) % 8 yields one of {0, 3, 4, 7} for valid inputs
# The answer is True exactly when m > 3 (i.e., m in {4,7})
# Only submit line 1 for character count
