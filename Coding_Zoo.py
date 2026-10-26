# Project Goal: Create a Zoo Coding Project with different animal classes each with unique attributes/methods

# Begin creating Animal class

class Animal:
    def __init__(self, name, weight, species):
        self.name = name
        self.weight = float(weight)
        self.species = species

    def sound(self):
        return "Animal sound"

    def info(self):
        animal_type = self.__class__.__name__
        return f"{self.name} is a {animal_type} of the {self.species} species, weighing {self.weight} kg. {self.name} makes a {self.sound()} sound"


# Begin Animal Subclasses here

class Bear(Animal):
    def __init__(self, name, weight, species, fur_color):
        super().__init__(name, weight, species)
        self.fur_color = fur_color
    
    def sound(self):
        return "high roar"
    
    def info(self):
        return super().info() + f" and has {self.fur_color} fur."

class Tiger(Animal):
    def __init__(self, name, weight, species, gender):
        super().__init__(name, weight, species)
        self.gender = gender
    
    def sound(self):
        return "deep roar"
    
    def info(self):
        return super().info() + f", and is a {self.gender} tiger."

# Elephant Age must be an integer
class Elephant(Animal):
    def __init__(self, name, weight, species, age):
        super().__init__(name, weight, species)
        self.age = int(age)
    
    def sound(self):
        return "trumpet"
    
    def info(self):
        return super().info() + f" and is {self.age} years old."
    
    
# Wolf extinction risk must be boolean
class Wolf(Animal):
    def __init__(self, name, weight, species, extinction_risk):
        super().__init__(name, weight, species)
        self.extinction_risk = extinction_risk
    
    def sound(self):
        return "howl"
    
    def info(self):
        risk = "is endangered" if self.extinction_risk else "is not endangered"
        return super().info() + f" and {risk}"
    

class Penguin(Animal):
    def __init__(self, name, weight, species, height):
        super().__init__(name, weight, species)
        self.height = float(height)
    
    def sound(self):
        return "squawk"
    
    def info(self):
        return super().info() + f" and stands at a height of {self.height} feet tall."
    

# Functions to help make sure valid inputs are present

def get_choice_from_list(prompt, valid_options):
    valid_list = [opt.lower() for opt in valid_options]

    while True:
        value = input(prompt).strip().lower()

        if value in valid_list:
            return valid_options[valid_list.index(value)]
        else:
            print(f"Invalid input. Valid options are: {', '.join(valid_options)}")


def get_float(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_bool(prompt):
    while True:
        value = input(prompt)
        if value == "True":
            return True
        elif value == "False":
            return False
        else:
            print("Invalid input. Please enter True or False")



# Begin Menu Functions

def add_animal(zoo):
    print("\nChoose an animal to add:")
    print("1. Bear")
    print("2. Tiger")
    print("3. Elephant")
    print("4. Wolf")
    print("5. Penguin")

    choice = input("Enter choice: ").strip()

    name = input("Name: ")
    weight = get_float("Weight in kg: ")
    species = input("Species: ")

    if choice == "1":
        fur = get_choice_from_list("Fur Color (Brown, Grey, Black, or White): ", ["Brown", "Grey", "Black", "White"])
        
        zoo.append(Bear(name, weight, species, fur))
    
    elif choice == "2":
        gender = get_choice_from_list("Gender (Male/Female): ", ["Male", "Female"])
        zoo.append(Tiger(name, weight, species, gender))
    
    elif choice == "3":
        age = get_int("Age in years: ")
        zoo.append(Elephant(name, weight, species, age))

    elif choice == "4":
        risk = get_bool("Extinction risk (True/False): ")
        zoo.append(Wolf(name, weight, species, risk))
    
    elif choice == "5":
        height = get_float("Height in ft: ")
        zoo.append(Penguin(name, weight, species, height))
    
    else:
        print("Invalid Choice.")

def show_all(zoo):
    print("\n--- All Animals ---")
    if not zoo:
        print("No animals yet.")
    else:
        for animal in zoo:
            print(animal.info())

def show_by_type(zoo):
    animal_type = input("\nEnter type (Bear/Tiger/Elephant/Wolf/Penguin): ")

    found = False
    for animal in zoo:
        if animal.__class__.__name__.lower() == animal_type.lower():
            print(animal.info())
            found = True
    
    if not found:
        print("No animals of that type.")


# Main program begins

def main():
    zoo = []

    while True:
        print("\n--- Zoo Menu ---")
        print("1. Add Animal")
        print("2. Show all Animals")
        print("3. Show Animals by type")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_animal(zoo)
        
        elif choice == "2":
            show_all(zoo)
        
        elif choice =="3":
            show_by_type(zoo)
        
        elif choice == "4":
            print("Exiting")
            break
        
        else:
            print("Invalid choice")

main()
