# Read a single digit (0–9) to display using a 7‑segment style pattern
num = input()

# 7‑segment representation for digit 0
if num == '0':
    print(" * * *")     # top segment
    print("*     *")   # upper-left + upper-right
    print("*     *")
    print("*     *")
    print("")          # middle gap
    print("*     *")   # lower-left + lower-right
    print("*     *")
    print("*     *")
    print(" * * *")     # bottom segment

# 7‑segment representation for digit 1
if num == '1':
    print("")
    print("      *")   # right column only
    print("      *")
    print("      *")
    print("")
    print("      *")
    print("      *")
    print("      *")
    print("")

# 7‑segment representation for digit 2
if num == '2':
    print(" * * *")     # top
    print("      *")    # upper-right
    print("      *")
    print("      *")
    print(" * * *")     # middle
    print("*")          # lower-left
    print("*")
    print("*")
    print(" * * *")     # bottom

# 7‑segment representation for digit 3
if num == '3':
    print(" * * *")     # top
    print("      *")    # upper-right
    print("      *")
    print("      *")
    print(" * * *")     # middle
    print("      *")    # lower-right
    print("      *")
    print("      *")
    print(" * * *")     # bottom

# 7‑segment representation for digit 4
if num == '4':
    print("")
    print("*     *")   # upper-left + upper-right
    print("*     *")
    print("*     *")
    print(" * * *")    # middle bar
    print("      *")   # lower-right
    print("      *")
    print("      *")
    print("")

# 7‑segment representation for digit 5
if num == '5':
    print(" * * *")     # top
    print("*")          # upper-left
    print("*")
    print("*")
    print(" * * *")     # middle
    print("      *")    # lower-right
    print("      *")
    print("      *")
    print(" * * *")     # bottom

# 7‑segment representation for digit 6
if num == '6':
    print(" * * *")     # top
    print("*")          # upper-left
    print("*")
    print("*")
    print(" * * *")     # middle
    print("*     *")    # lower-left + lower-right
    print("*     *")
    print("*     *")
    print(" * * *")     # bottom

# 7‑segment representation for digit 7
if num == '7':
    print(" * * *")     # top
    print("      *")    # upper-right
    print("      *")
    print("      *")
    print("")
    print("      *")    # lower-right
    print("      *")
    print("      *")
    print("")

# 7‑segment representation for digit 8
if num == '8':
    print(" * * *")     # top
    print("*     *")    # upper-left + upper-right
    print("*     *")
    print("*     *")
    print(" * * *")     # middle
    print("*     *")    # lower-left + lower-right
    print("*     *")
    print("*     *")
    print(" * * *")     # bottom

# 7‑segment representation for digit 9
if num == '9':
    print(" * * *")     # top
    print("*     *")    # upper-left + upper-right
    print("*     *")
    print("*     *")
    print(" * * *")     # middle
    print("      *")    # lower-right
    print("      *")
    print("      *")
    print(" * * *")     # bottom
