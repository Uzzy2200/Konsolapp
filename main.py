from tec import TEC
from teacher import Teacher
tec_instance = TEC()

def create_teacher():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    subject = input("Enter subject: ")
    
    new_teacher = Teacher(first_name, last_name, subject)
    tec_instance.add_teacher(new_teacher)
    print(f"Teacher {new_teacher.first_name} {new_teacher.last_name} created with subject {new_teacher.subjects}")

def update_teacher():
    tec_instance.show_teachers()
    choice = input("Choose a teacher by entering their full name: ")
    tec_instance.update_teacher(choice)

def show_all_teachers():
    tec_instance.show_teachers()

if __name__ == "__main__":
    while True:
        print("\nMENU:")
        print("1. Create teacher")
        print("2. Update teacher")
        print("3. Show list of all teachers")
        print("4. EXIT")

        choice = input("Choose an option by entering a number: ")

        if choice == "1":
            create_teacher()
        elif choice == "2":
            update_teacher()
        elif choice == "3":
            show_all_teachers()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
