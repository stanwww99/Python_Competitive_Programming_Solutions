def is_prime(n):
    # 1 is not a prime number
    if n == 1:
        return False

    # 2 and 3 are prime numbers
    elif n == 2 or n == 3:
        return True

    # Any even number greater than 2 is not prime
    elif n % 2 == 0:
        return False

    # Check odd divisors from 3 up to sqrt(n)
    # If any divisor divides n evenly, it's not prime
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    # If no divisors were found, n is prime
    return True


def find_next_prime(my_num):
    # Handle small edge cases directly
    if my_num == 1 or my_num == 2:
        return 2
    if my_num == 3:
        return 3
    if my_num == 4 or my_num == 5:
        return 5

    # If the number is even, move to the next odd number
    if my_num % 2 == 0:
        my_num += 1

    # Keep checking odd numbers until a prime is found
    while not is_prime(my_num):
        my_num += 2  # skip even numbers

    return my_num


# Read input from the user
my_input = int(input().strip())

# Compute the next prime number
result = find_next_prime(my_input)

# Output the result
print(result)
