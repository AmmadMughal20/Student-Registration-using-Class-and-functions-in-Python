class Student(object):
    # Student Object Initialization
    def __init__(self, name, roll_number, email, courses):
        self.name, self.roll_number, self.email, self.courses = name, roll_number, email, courses
    
# Student Object to Dictionary Conversion
def return_dictionary(obj_student):
    student, student["name"], student["roll_number"], student["email"], student["courses"] = {}, obj_student.name, obj_student.roll_number, obj_student.email, obj_student.courses
    return student

# print the dictionary of a single student by providing rollnumber with list of students
def get_student(roll_number, students):
    for student in students:
        for key,value in student.items():
            if key == "roll_number" and value == roll_number:
                print(f"The student details with roll number: {roll_number}")
                for key,value in student.items():
                    print(key + ": " + str(value))
        break            

 # printing the list of all students
def print_students(students):
    print("*** List of all students ***")
    counter = 1
    for student in students:
        print(f"\nThe details of student no.: {counter}")
        for key, value in student.items():
            print(key + ": " + str(value))
        counter+=1

# insert student dictionary in students list
def insert_student(student, students):
    return students.append(student)

# main function to execute script
def main():
    ft, tt = 40, 3 # stars
    students = []

    #  courses list
    courses = ["Artificial Intelligence", "Blockchain", "Cloud Computing", "Internet of Things"]
    
    print("\n" + "*"*ft + "\n" + "*"*tt + " Welcome to Students Registration " + "*"*tt + "\n" + "*"*ft + "\n")


    while True:
        print("*"*17+" Menu "+"*"*17+"\n")
        print("1: Register new student.\n2: Print a student details.\n3: Print complete students list.\n4. Exit")
        user_input = input("\nEnter your desired option: ")

        # flow of program according to user input
        if user_input == "4": # exits the program
            print("Thank You! Bye Bye!")
            exit()
        
        elif user_input == "1":    # to register a new student
            print("*"*9+" Enter student details "+"*"*8+"\n")

            # inputs details of potentially registering student 
            name, roll_number, email, std_courses = input("Name: "), input("Roll Number: "), input("Email: "), []
            print("Please select your desired courses from below option:\n")
            
            course_counter = 1
            # printing courses list to get input for courses 
            for course in courses:
                print(f"{course_counter}. for {course}")
                course_counter+=1

            # user input for registering student courses
            user_courses = input("e.g. 1, 2 or 1,2 for Artificial Intelligence and Blockchain\n")
            
            # creation of list for registering student's courses according to user input
            for courseid in user_courses:
                if courseid == "1" or courseid == "2" or courseid == "3" or courseid == "4":
                    std_courses.append(courses[int(courseid)-1])
            
            # student object creation, object to dictionary conversion and insertion of dictionary into registered students list
            insert_student(return_dictionary(Student(name, roll_number, email, std_courses)),students)
            print("Student Registered!!!")

        elif user_input == "2": # to get a student by entering its roll number
            roll_number_to_find = input("Enter Roll Number to find: ")
            get_student(roll_number_to_find, students)

        elif user_input == "3": # to print list of all students
            print_students(students)

        else: # all other wrong input cases
            ("Wrong Input!!!\n")

main() # execution