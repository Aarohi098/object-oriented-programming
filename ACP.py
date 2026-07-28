class Pet:
    # class attribute
    topic = "Animals"
    
    # instance attributes
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

# --- Interactive User Input ---
print("--- Welcome to the Pet Profile Builder ---")

# collect information from the user
user_name = input("Enter your pet's name: ")
user_species = input("Enter your pet's species ")
user_age = input("Enter your pet's age: ")


my_pet = Pet(user_name, user_species, user_age)


# Accessing the class attribute
print("Classification Topic: {}".format(my_pet.topic))

# Accessing the instance attributes provided by the user
print("Pet Name: {}".format(my_pet.name))
print("Pet Species: {}".format(my_pet.species))
print("Pet Age: {} years old".format(my_pet.age))
