#This program calculates the number of choices a student gets right
question = int(input())
ans = list()
student = list()
for i in range(question):
    ans.append(input())
for i in range(question):
   student.append(input())
count = 0
for i in range(question):
    if student[i]  == ans[i]:
        count += 1
print(count)