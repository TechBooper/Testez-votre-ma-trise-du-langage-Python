class MyClass:
    def __init__(self, full_name):
        self.full_name = full_name

    def display_name(self):
        print("Le nom complet est :", self.full_name)


class OtherClass:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display_name(self):
        print(f"Nom complet : {self.first_name} {self.last_name}")


# Example usage
person1 = MyClass("Marwane")
person1.display_name()

person2 = OtherClass("John", "Doe")
person2.display_name()
