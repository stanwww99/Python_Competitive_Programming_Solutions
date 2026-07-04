import random

# Function to perform the Miller-Rabin test
def is_prime(n, k=5):  # Number of trials
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Find r and d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test n with k trials
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Function to find the next prime number
def next_prime(n):
    while not is_prime(n):
        n += 1
    return n

current_number = int(input())
next_prime_number = next_prime(current_number)
print(next_prime_number)
