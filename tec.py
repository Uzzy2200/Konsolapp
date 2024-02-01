from teacher import Teacher

class TEC:
    def __init__(self):
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def update_teacher(self, teacher_name):
        for teacher in self.teachers:
            if f"{teacher.first_name} {teacher.last_name}" == teacher_name:
                print(f"Updating teacher: {teacher.first_name} {teacher.last_name}")
                print("1. Add a subject")
                print("2. Remove a subject")

                choice = int(input("Choose an option: "))

                if choice == 1:
                    new_subject = input("Enter the new subject: ")
                    teacher.add_subject(new_subject)
                    print(f"Subject {new_subject} added to {teacher.first_name} {teacher.last_name}")
                elif choice == 2:
                    subject_to_remove = input("Enter the subject to remove: ")
                    teacher.remove_subject(subject_to_remove)
                    print(f"Subject {subject_to_remove} removed from {teacher.first_name} {teacher.last_name}")
                else:
                    print("Invalid choice. Returning to the main menu.")
                return

        print(f"Teacher with name '{teacher_name}' not found.")

    def show_teachers(self):
        for teacher in self.teachers:
            print(f"{teacher.first_name} {teacher.last_name} - Subjects: {''.join(teacher.subjects)}")
