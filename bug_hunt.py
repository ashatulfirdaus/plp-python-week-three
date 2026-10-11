
# This program demonstrates a while loop and a logic bug.

count = 1

while count <= 5:
    print(f"Count: {count}")
# BUG: count is not increased, so the loop never ends.


count = 1
total = 0

# BUG: Added the missing colon (:) after the while condition.
while count <= 5:
    # BUG: Changed < to <= so the loop includes number 5.
    total = total + count
    count = count + 1

# BUG: Converted total to a string so it can be joined with text.
print("Sum of 1 to 5 is: " + str(total))
