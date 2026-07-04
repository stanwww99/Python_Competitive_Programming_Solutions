# Read a line of input, expected format: "<start_on> <num_days>"
info = input()

# Find the index of the first space to split the two numbers
i_space = info.find(' ')

# Extract starting weekday index and number of days in the month
start_on = int(info[:i_space])          # 1 = Sun, 2 = Mon, ..., 7 = Sat
num_days = int(info[i_space + 1:])

# Tuple of weekday labels
days = ('Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat')

# Print weekday headers on one line
for d in days:
    if d == 'Sat':
        print(d, end='')               # No trailing space after Saturday
    else:
        print(d, end=' ')

# Compute how many spaces to print before the first day
# Each column is 4 characters wide, so shift by (start_on * 4)
preceding_space = start_on * 4 - 5

# Print the initial indentation before day 1
if start_on == 1:
    # If the month starts on Sunday, print slightly different spacing
    print('\n' + preceding_space * ' ', end=2 * ' ')
else:
    print('\n' + preceding_space * ' ', end=3 * ' ')

# Number of days remaining in the first week
day_at_end = 8 - start_on

# Tracks which row (week) we are printing
row_num = 0

# Loop through all days of the month
for d in range(1, num_days + 1):

    # If it's the last day, print without trailing spaces
    if d == num_days:
        print(d, end='')

    else:
        # Check if we reached the end of a week
        if d % (day_at_end + 7 * row_num) == 0:
            print(d)                   # Print day and move to next line

            # Print indentation for next line depending on digit width
            if d < 9:
                print(2 * ' ', end='')
            else:
                print(' ', end='')

            row_num += 1               # Move to next week

        else:
            # Print day with spacing depending on digit width
            if d < 9:
                print(d, end=3 * ' ')
            else:
                print(d, end=2 * ' ')

# Final newline after printing the calendar
print()
