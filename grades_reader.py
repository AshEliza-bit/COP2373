import csv

def main():
    print("Student Grades\n") #prints title at the top of the table
    print(f"{'First Name':<15}{'Last Name':<15}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}") # column headers with neat spacing
    print("-" * 60) # prints a divider line made of 60 dashes

    # open CSV file
    with open('grades.csv', mode='r') as file: # in read mode
        reader = csv.reader(file) # creates a CSV reader object
        next(reader)  # skip the first row with the headers

        # print each student's record
        for row in reader:
            first_name, last_name, exam1, exam2, exam3 = row
            print(f"{first_name:<15}{last_name:<15}{exam1:<10}{exam2:<10}{exam3:<10}")

main()
