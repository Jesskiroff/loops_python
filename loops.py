# fruits = ["Apple", "Peach", "Pineapple", "Orange", "Pear"]
# for f in fruits:
#     print (f)
#     print(f + "salad")


height = input("Please list student heights \n")
student_heights = height.split(",")
print(student_heights)
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
total_height = 0
for h in student_heights:
    total_height += h
print(f"The total height is {total_height}")

# number_of_students = 0
# for s in student_heights:
#     number_of_students += 1
number_of_students = len(student_heights)
print(f"The number of students is: {number_of_students}")

average_height = round(total_height/ number_of_students)

print(f"The average height of the students is {average_height}")
    
    
