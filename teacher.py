from person import Person

class Teacher(Person):
    def __init__(self, first_name, last_name, subject):
        super().__init__(first_name, last_name)
        self.subjects = [subject]

    def add_subject(self, new_subject):
        self.subjects.append(new_subject)

    def remove_subject(self, subject_to_remove):
        if subject_to_remove in self.subjects:
            self.subjects.remove(subject_to_remove)
        else:
            print(f"Subject {subject_to_remove} not found for {self.first_name} {self.last_name}")
