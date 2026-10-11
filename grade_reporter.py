
# This program reports grades for a list of students' marks.

marks = [85, 72, 56, 43, 90]
total = 0

for mark in marks:
    total += mark

    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Mark: {mark}, Grade: {grade}")

average = total / len(marks)

print(f"Total marks: {total}")
print(f"Average mark: {average:.2f}")



scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score}, Grade: {grade}")

    if score >= 50:
        passed += 1
    else:
        failed += 1

    total += score

average = total / len(scores)

print(f"Number passed: {passed}")
print(f"Number failed: {failed}")
print(f"Average score: {round(average, 1)}")
