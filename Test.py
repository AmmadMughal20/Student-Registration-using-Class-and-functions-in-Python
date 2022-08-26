class Student(object):
    # Student Object Initialization
    def __init__(self):
        self.students = []
    
    # print the dictionary of a single student by providing rollnumber with list of students
    def get_student(self, roll_number):
        for student in self.students:
            for key,value in student.items():
                if key == "roll number" and value == roll_number:
                    print(f"The student details with roll number: {roll_number}")
                    for key,value in student.items():
                        print(key + ": " + str(value))
        return            

     # printing the list of all students
    def print_students(self):
        print("*** List of all students ***")
        counter = 1
        for student in self.students:
            print(f"\nThe details of student no.: {counter}")
            for key, value in student.items():
                print(key + ": " + str(value))
            counter+=1

    # insert student dictionary in students list
    def insert_student(self):
        courses = ["Artificial Intelligence", "Blockchain", "Cloud Computing", "Internet of Things"]

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
            
        self.students.append({"roll number" : roll_number, "Name" : name, "email": email, "courses" : std_courses})

# main function to execute script
def main():
    ft, tt = 40, 3 # stars

    #creating object
    std = Student()    
    
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
            std.insert_student()
            print("Student Registered!!!")

        elif user_input == "2": # to get a student by entering its roll number
            roll_number_to_find = input("Enter Roll Number to find: ")
            std.get_student(roll_number_to_find)

        elif user_input == "3": # to print list of all students
            std.print_students()

        else: # all other wrong input cases
            ("Wrong Input!!!\n")

main() # execution