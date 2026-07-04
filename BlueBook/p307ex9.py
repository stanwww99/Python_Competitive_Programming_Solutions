# Read the number of test cases
T = int(input())

# Loop through all test cases
for i in range(T):
    # Read the year for this test case
    N = int(input())

    # Check if the year is a leap year:
    # Rule:
    # - divisible by 4 AND not divisible by 100
    #        OR
    # - divisible by 400
    if ((N % 4 == 0 and N % 100 != 0) or N % 400 == 0):
        print(1)   # Leap year
    else:
        print(0)   # Not a leap year
