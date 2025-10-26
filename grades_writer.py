import csv

def main():
    # opens a file in write mode; keep it clean by using newline
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file) #creates a CSV writer object

        # header row
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # get input on number of students
        num_students = int(input("How many students do you want to enter? "))

        # loop to collect and write every student's data
        for i in range(num_students):
            print(f"\n--- Student {i + 1} ---")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # write the record to the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    # shown when done taking in data
    print("\nData successfully written to grades.csv")

main()
