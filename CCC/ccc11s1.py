#this program computes if a text is english or French given number of s and t
sCount = 0
tCount = 0
N = int(input())
for i in range(N):
    text = input()
    sCount += text.count('s')
    sCount += text.count('S')
    tCount += text.count('t')
    tCount += text.count('T')
if sCount >= tCount:
    print("French")
else:
    print("English")
