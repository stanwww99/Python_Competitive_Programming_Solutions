# Open a file named "False" and read its entire contents into the string s
# (Note: normally you'd pass a filename as a string; open(False) is unusual.)
s = open(False).read()

# Create an empty list to store the counts for each letter
counts = []

# Loop through the 26 letters of the English alphabet
for i in range(26):
    # Count occurrences of the uppercase version of the current letter
    uppercase_count = s.count(chr(i + 65))   # 65 = 'A' in ASCII

    # Count occurrences of the lowercase version of the current letter
    lowercase_count = s.count(chr(i + 97))   # 97 = 'a' in ASCII

    # Total occurrences of this letter (upper + lower)
    count = uppercase_count + lowercase_count

    # Convert the number to a string and store it in the list
    counts.append(str(count))

# Print all 26 counts separated by spaces
print(' '.join(counts))
