



"""
The program will display information about student grades on a final exam based off of a input text file
containing the grades.
To create the program, a main() function will be used to initialize the application.
A calculate_percent_above_average will also be used to calculate
the percentage of grades that are above the average grade.
Then, all the grades in the input text file will be read using the open() method.
From there, the grades will be assigned to a list of integers.
After the program runs, the information that will be printed to the user include the number of grades,
the average grade, and the percentage of grades that are above the average grade.
"""

"""
main
  infile = open("Final.txt")
  copy individual grades
  close infile

calculate_percent_above_average
  average = sum of grades / total number of grades
  num = 0
  For grade in grades
    if the grade is > average
      num += 1
  print("Number of grades: ", total number of grades)
  print("Average grade: ", average)
  print("Percentage of grades above average: {0:.2f}%)
    format 100 * num / total number of grades

main
"""
## Analyze grades on a final exam

def main():
  infile = open("Final.txt", 'r')
  grades = [line.rstrip() for line in infile]
  infile.close()
  for i in range(len(grades)):
    grades[i] = int(grades[i])

def calculate_percent_above_average():
  average = sum(grades) / len(grades)
  num = 0
  for grade in grades:
    if grade > average:
      num += 1
  print("Number of grades:", len(grades))
  print("Average grade:", average)
  print("Percentage of grades above average: {0:.2f}%".format(100 * num / len(grades)))

main()

