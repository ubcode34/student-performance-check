

# Name: ulises alberto 
# Period: pm

# Comment 1: Program setup and kind of like an introduction to what the app is about.
print("==================================")
print("STUDENT PERFORMANCE OVERVIEW")
print("==================================")
print("Enter the student's information below.")
print()

# Comment 2: 
"""
Asking questions to the student to get information to know what kind of student they are
"""
student_name = input("What is the student's name? ")
grade_level = int(input("What grade level is the student in? "))
assignment_avg = float(input("What is the student's assignment average? "))
quiz_avg = float(input("What is the student's quiz average? "))
test_avg = float(input("What is the student's test average? "))
attendance_pct = float(input("What is the student's attendance percentage? "))
missing_assignments = int(input("How many missing assignments does the student have? "))

# Comment 3: Calculate the student's overall grade
def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 0.30
    quiz_portion = quiz_average * 0.30
    test_portion = test_average * 0.40
    
    overall_grade = assignment_portion + quiz_portion + test_portion
    
    print("Overall Grade:", overall_grade)
    return overall_grade

overall_grade = calculate_grade(assignment_avg, quiz_avg, test_avg)

# Comment 4: Assign a letter grade based on overall grade number 
def letter_grade(overall_grade):
    if overall_grade >= 90:
        letter = "A"
    elif overall_grade >= 80:
        letter = "B"
    elif overall_grade >= 70:
        letter = "C"
    elif overall_grade >= 60:
        letter = "D"
    else:
        letter = "F"
    
    print("Letter Grade:", letter)
    return letter

student_letter_grade = letter_grade(overall_grade)

# Comment 5: Determine attendance status based on percentage
def attendance_status(attendance):
    if attendance >= 95:
        status = "Excellent Attendance"
    elif attendance >= 90:
        status = "Good Attendance"
    elif attendance >= 80:
        status = "Attendance Warning"
    else:
        status = "COOKED"
    
    print("Attendance Status:", status)
    return status

student_attendance_status = attendance_status(attendance_pct)


# Comment 6: missing assignment status and message 
def assignment_status(missing_assignments):
    if missing_assignments == 0:
        status = "Excellent"
    elif missing_assignments <= 2:
        status = "Good"
    elif missing_assignments <= 4:
        status = "Warning"
    else:
        status = "COOKED"
    
    print("Missing Assignment Status:", status)
    return status

student_assignment_status = assignment_status(missing_assignments)


# Comment 7: Determine the student's academic eligibility
def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic Eligibility: ELIGIBLE")
                print("Student passed all three requirements.")
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")
        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low.")
    else:
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")

check_eligibility(overall_grade, attendance_pct, missing_assignments)


# Comment 8: Check if student qualifies for High Honors or not
def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
            print("High Honors: NO")
            print("Reason: Attendance requirement not met.")
    else:
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")

check_high_honors(overall_grade, attendance_pct, missing_assignments)


# Comment 9: Check if student is in Good Standing using 'and'
def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        print("Good Standing: YES")
    else:
        print("Good Standing: NO")

check_good_standing(overall_grade, attendance_pct)


# Comment 10: Check if student needs academic support using 'or'
def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        print("Additional Support: RECOMMENDED")
    else:
        print("Additional Support: NOT NEEDED")

check_support(overall_grade, attendance_pct)


# Comment 11: Simulate nested conditional student login
print()
print("=== STUDENT LOGIN SIMULATION ===")
input_username = input("Enter username: ")
input_pin = input("Enter PIN: ")

if input_username == "student":
    if input_pin == "1234":
        print("Login Successful!")
    else:
        print("Login Failed: Incorrect PIN.")
else:
    print("Login Failed: Incorrect username.")

# Comment 12: Display customized message for grade level
def grade_level_message(grade_level):
    if grade_level == 9:
        print("Welcome to your freshman year!")
    elif grade_level == 10:
        print("Keep building your skills!")
    elif grade_level == 11:
        print("Junior year - keep pushing!")
    elif grade_level == 12:
        print("Senior year - finish strong!")
    else:
        print("Invalid grade level.")

grade_level_message(grade_level)

# Comment 13: Find the student's strongest academic category
def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average >= quiz_average and assignment_average >= test_average:
        print("Strongest Category: Assignments")
    elif quiz_average >= assignment_average and quiz_average >= test_average:
        print("Strongest Category: Quizzes")
    else:
        print("Strongest Category: Tests")

strongest_category(assignment_avg, quiz_avg, test_avg)


# Comment 14: Display final student summary report
print()
print("==================================")
print("STUDENT OVERVIEW")
print("==================================")
print("Student Name:", student_name)
print("Grade Level:", grade_level)
print()
print("Assignment Average:", assignment_avg)
print("Quiz Average:", quiz_avg)
print("Test Average:", test_avg)
print()
print("Overall Grade:", overall_grade)
print("Attendance:", attendance_pct)
print("Missing Assignments:", missing_assignments)
print("==================================")

