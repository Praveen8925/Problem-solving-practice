import json
from json import JSONDecodeError
def load_students():
    try :
        with open('students.json' , 'r') as file :
            file_data = json.load(file)
    except JSONDecodeError :
        print("the JSON file is invalid/corrupted.")
        return {}
    except FileNotFoundError :
        return {}
    return file_data

student = load_students()

def get_student_name(): 
    while True :      
        name = input("Enter you name :").strip()
        name_without_spaces = name.replace(" ","")
        if not name_without_spaces.isalpha():
            print("Name should contain only letters.")
            continue
        
        return name

def get_student_id():
    while True:
        student_id = input("Enter your id :").upper().strip()
        if not student_id:
            print("ID cannot be empty")
            continue
        
        return student_id
        
def get_student_mark(subjects):
    while True :
        try : 
            subjects_mark = int(input(f"Enter your {subjects} Mark : "))
        except ValueError :
            print(f"Please enter an interger")
            continue
        if 0<= subjects_mark <=100:
            return subjects_mark
        else :
            print(f"the Mark range should be 0 to 100 ")
            continue


def get_student_data():
    student_data = {}
    
    student_data['name'] = get_student_name()
    
    while True:
        student_id = get_student_id()
        if student_id not in student:
            break
        else : 
            print("The id is already exist ,Please Enter your Valid Id")
        
    subjects = ('Tamil','English','Science','Maths','History')
    marks = {}
    for subject in subjects:
        marks[subject.upper()] = get_student_mark(subject.upper())
    student_data['mark'] = marks
    
    return student_id , student_data 


def calculate_average(marks):
    average = round(sum(marks.values()) / len(marks))
    return average

def calculate_grade(average):
    if average >= 90:
        Grade = 'A'
    elif average >=80:
        Grade = 'B'
    elif average >=70:
        Grade = 'C'
    elif average >=60:
        Grade = 'D'
    else :
        Grade = 'F'
        
    return Grade

def display_report(std_id , std_data):
    print(f"ID : {std_id}")
    print(f"Student name : {std_data['name']}")
    print()
    for sub , mark in std_data['mark'].items():
        print(f"{sub} : {mark}")
    print()
    averages = calculate_average(std_data['mark'])
    grade = calculate_grade(averages)
    print(f"Average : {averages}")
    print(f"Grade : {grade}")
    print()
    print("=" * 30)
    
def search_student():
    student_id = get_student_id()
    if student_id in student :
        display_report(student_id ,student[student_id])
    else :
        print(f"{student_id} Student ID not found.")
        
    
def save_data(student):
    try :
        with open('students.json' , 'w') as file :
            json.dump(student,file)
    except PermissionError :
        print("Permission denied. Unable to save student data.")
        
def choice_fun(max_choice):
    while True :
        try :
            choice = int(input("Enter Your Choice :"))
            if 1 <= choice <=max_choice :
                break
            else :
                print("Invalid choice , choose the valid choice")
        except ValueError :
            print("Please enter an integer")
            
    return choice
        
def update_student():
    while True :
        student_id = get_student_id()
        if student_id in student :
            display_report(student_id ,student[student_id])
            print("1. update Name")
            print("2. update marks")
            print("3. Cancel")
            max_choice = 3
            choice = choice_fun(max_choice)
                
            if choice == 1 :
                
                student[student_id]['name'] = get_student_name()
                save_data(student)
                display_report(student_id ,student[student_id])
                break
                    
        
            elif choice == 2:
                print(f'{"=" * 5} Updating Student Mark {"=" * 5}')
                
                Subject = input("Enter Subject").upper().strip()
                if Subject in student[student_id]['mark']:
                    
                    student[student_id]['mark'][Subject] = get_student_mark(Subject)
                    save_data(student)
                    display_report(student_id ,student[student_id])
                    break
                                                    
                else :
                    available_subjects = ", ".join(student[student_id]['mark'].keys())
                    print("Availabel Subjects" , available_subjects)    
            
                    
            elif choice == 3 :
                print("Cancel")
                break
                    
                        
                        
        else :
            print(f"{student_id} Student ID not found.")
            break
        
def delete_student():
    student_id = get_student_id()
    if student_id in student :
        display_report(student_id ,student[student_id])
        while True :
            print("Please enter YES or NO.")
            confirmation = input("Enter YES or NO :").strip().upper()
            if confirmation == "YES":
                del student[student_id]
                print(f"{student_id} Removed from the list")
                save_data(student)
                break

                
            elif confirmation == "NO" :
                print("Cancle")
                break
    else :
        print(f"{student_id} Student ID not found.")
        
        
        
        
while True:
    print("===== STUDENT REPORT SYSTEM =====")
    print("1. Add student")
    print("2. View reports")
    print("3. Search Report")
    print("4. Update Report")
    print("5. Delete Report")
    print("6. Exit")
    choice_no = 6
    choice = choice_fun(choice_no)
    if choice == 1 :
        print(f'{"=" * 5} Adding Student Report {"=" * 5}')
        student_id , student_data = get_student_data()
        student[student_id] = student_data
        save_data(student)
    elif choice == 2:
        print(f'{"=" * 5}All Student Report{"=" * 5}')
        for student_id, student_data in student.items():
            display_report(student_id,student_data)
    elif choice == 3:
        print(f'{"=" * 5}Search Student Report{"=" * 5}')
        search_student()
    elif choice == 4:
        print(f'{"=" * 5}Update Student Report{"=" * 5}')
        update_student()
    elif choice == 5:
        print(f'{"=" * 5}Delete Student Report{"=" * 5}')
        delete_student()
    elif choice == 6 :
        print(f'{"=" * 5}exit{"=" * 5}')
        break