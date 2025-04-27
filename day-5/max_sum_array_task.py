import random

student_scores = [78, 92, 65, 88, 70, 55, 81, 90, 73, 67,
                  84, 76, 69, 93, 60, 82, 71, 87, 59, 66,
                  80, 75, 62, 85, 77]
print(max(student_scores))


max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

# list comprehension to create a list of 25 random numbers between 0 and 100.
student_scores = [random.randint(0,100) for _ in range(25)]
print(student_scores)
print(sum(student_scores))