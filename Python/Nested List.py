#Hacker Rank -Nested List

# Given the names and grades for each student in a class of N students, store them in a
# nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names
# alphabetically and print each name on a new line.

# Example
# records = [["chi", 20.0], ["beta",50.0],["alpha",50.0]]
# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are
# two students with that score: ["beta", "alpha"]. Ordered alphabetically, the names are

# printed as:
# alpha
# beta

# Input Format

# The first line contains an integer, N, the number of students.
# The 2NV subsequent lines describe each student over 2 lines.

# - The first line contains a student's name.

# - The second line contains their grade.


s=[]
if __name__ == '__main__':
    for _ in range(int(input("Enter number of students : "))):
        name = input("Name : ")
        score = float(input("Score : "))
        s.append([name,score])
grades=sorted(set(score for name,score in s))
second_lowest=grades[1]

second_lowest_students = [name for name, score in s if score == second_lowest]

for name in sorted(second_lowest_students):
    print(name)
