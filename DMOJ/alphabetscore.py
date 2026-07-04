from collections import Counter
count = Counter(input())
score = 0
for char in count:
    score += count[char]*(ord(char) - ord('a') + 1) #score for one letter is frequency a = 1, ... z = 26
print(score)