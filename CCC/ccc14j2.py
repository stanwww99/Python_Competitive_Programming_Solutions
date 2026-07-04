#This program determines who has won the vote
V = int(input())
vote = input()
a = vote.count('A')
b = vote.count('B')
if a > b:
    print('A')
if a < b:
    print('B')
if a ==  b:
    print('Tie')