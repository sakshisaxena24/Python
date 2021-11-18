student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0
min = 1000000
for score in student_scores:
    if score > max:
        max = score
    if score < min:
        if score < min:
            min = score
print(f"Highest score is: {max}")
print(f"Lowest score is : {min}")
