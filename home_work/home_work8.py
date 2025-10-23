class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")


class Trainer(Employee):
    def __init__(self, name, role, specialization):
        Employee.__init__(self, name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        Employee.__init__(self, name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Yoga Style: {self.yoga_style}")


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print(f"Yoga Style: {self.yoga_style}")



emp = Employee("Alice", "Receptionist")
trainer = Trainer("Bob", "Fitness Trainer", "Weight Training")
yoga_instructor = YogaInstructor("Clara", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer("David", "Multi-Trainer", "Cardio & Strength", "Ashtanga Yoga")

print("Employee Details:")
emp.display()
print("\nTrainer Details:")
trainer.display()
print("\nYoga Instructor Details:")
yoga_instructor.display()
print("\nMulti-Trainer Details:")
multi_trainer.display()
