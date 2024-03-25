#!/usr/bin/env python3

class User:
    def __init__(self, name, first_name, address, nationality, phone, date_of_birth, father_name, father_first_name, father_date_of_birth, mother_name, mother_first_name, mother_date_of_birth):
        """
        Initializes a User object with additional parental information.
        """
        self.name = name
        self.first_name = first_name
        self.address = address
        self.nationality = nationality
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.father_name = father_name
        self.father_first_name = father_first_name
        self.father_date_of_birth = father_date_of_birth
        self.mother_name = mother_name
        self.mother_first_name = mother_first_name
        self.mother_date_of_birth = mother_date_of_birth

    def verify_parents(self):
        """
        Verifies parents' information in the database.
        """
        if (self.father_name == father_name and self.father_first_name == father_first_name and self.father_date_of_birth == father_date_of_birth) \
           and (self.mother_name == mother_name and self.mother_first_name == mother_first_name and self.mother_date_of_birth == mother_date_of_birth):
            return True
        else:
            return False



class FamilyTree:
    def __init__(self):
        """
        Initializes a FamilyTree object to manage a collection of Person objects.
        """
        self.people = []

    def add_person(self, person):
        """
        Adds a person to the family tree.
        """
        self.people.append(person)

    def remove_person(self, person):
        """
        Removes a person from the family tree.
        """
        self.people.remove(person)



class Platform:
    def __init__(self):
        """
        Initializes a Platform object to manage user registration and family trees.
        """
        self.users = []
        self.global_tree = FamilyTree()

    def register_user(self, name, first_name, address, nationality, phone, date_of_birth,
                      father_name, father_first_name, father_date_of_birth,
                      mother_name, mother_first_name, mother_date_of_birth):
        """
        Registers a user in the platform and adds them to the global family tree.
        """
        # Create a new user instance
        user = User(name, first_name, address, nationality, phone, date_of_birth,
                    father_name, father_first_name, father_date_of_birth,
                    mother_name, mother_first_name, mother_date_of_birth)
        
        # Add the user to the global family tree
        self.global_tree.add_person(user)
        

        # Add the user to the platform's user list
        self.users.append(user)

        return user



class Administrator:
    def __init__(self, last_name, first_name, address, nationality, phone, date_of_birth, username, password, admin_id):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.nationality = nationality
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.username = username
        self.password = password

    def remove_node(self, person):
        """
        Removes a node and its descendants from the family tree.
        """
        pass

    def track_tree_size(self, family_tree):
        """
        Tracks the evolution of the family tree's size.
        """
        pass

    def find_most_represented_family(self, family_tree):
        """
        Finds the most represented family in the global tree.
        """
        pass

    def other_functionalities(self):
        """
        Other functionalities to be defined.
        """
        pass


#____________________________________   INTERFACE ____________________________


existing_administrators_data = [
    ("AdminLastName1", "AdminFirstName1", "AdminAddress1", "AdminNationality1", "AdminPhone1", "AdminDOB1", "admin1", "password1"),
    ("AdminLastName2", "AdminFirstName2", "AdminAddress2", "AdminNationality2", "AdminPhone2", "AdminDOB2", "admin2", "password2"),
    # Add more administrators as needed
]

# Create an instance of the platform
platform = Platform()

# Register existing administrators
for admin in existing_administrators_data:
    platform.users.append(admin)


# Prompt the user to choose if they are an administrator or a regular user
print("Are you registering as an Administrator or a User?")
print("1. Administrator")
print("2. User")

# Get user input for the role choice
role_choice = input("Enter the number corresponding to your role choice: ")

if role_choice == "1":
    # Prompt the user to enter their credentials
    # Loop until the login is successful
    is_admin = False
    while not is_admin:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for admin in existing_administrators_data:
            if isinstance(admin, Administrator) and admin.username == username and admin.password == password:
                is_admin = True
                break

    if is_admin:
        print("Welcome, Administrator!")
    else:
        print("Invalid credentials or not an administrator.")

elif role_choice == "2":

    welcome_message = """
    Welcome to our Family Tree Platform!

    We're thrilled to have you join our community dedicated to creating and managing family trees. With our platform, you can easily trace your ancestry, connect with relatives, and explore your family history.

    Whether you're just getting started or you're a seasoned genealogist, our platform offers a wide range of features to help you build and explore your family tree with ease.

    Feel free to explore the various functionalities, add your family members, and embark on a journey of discovery through your family's rich heritage.

    Happy exploring!


    Pauline Francois and Alize Platform   


    """
    print(welcome_message)


    # Register a new user
    print("Please enter your information below:")

    name = input("Last Name: ")
    first_name = input("First Name: ")
    address = input("Address: ")
    nationality = input("Nationality: ")
    phone = input("Phone Number: ")
    date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
    father_name = input("Father's Last Name: ")
    father_first_name = input("Father's First Name: ")
    father_date_of_birth = input("Father's Date of Birth (YYYY-MM-DD): ")
    mother_name = input("Mother's Last Name: ")
    mother_first_name = input("Mother's First Name: ")
    mother_date_of_birth = input("Mother's Date of Birth (YYYY-MM-DD): ")

    # Register the user with the entered information
    new_user = platform.register_user(name, first_name, address, nationality, phone, date_of_birth, father_name, father_first_name, father_date_of_birth, mother_name, mother_first_name, mother_date_of_birth)

else:
    print("Invalid choice.")


# Sample data for 10 users
users_data = [
    ("Dupont", "Jean", "123 Rue de la République", "France", "01-23-45-67-89", "1980-05-15",
     "Dupont", "Pierre", "1950-02-10", "Durand", "Marie", "1955-08-20"),
    ("Dubois", "Marie", "456 Avenue Victor Hugo", "France", "02-34-56-78-90", "1975-07-20",
     "Dubois", "Jacques", "1955-11-25", "Martin", "Isabelle", "1960-04-15"),
    ("Moreau", "François", "789 Boulevard Saint-Germain", "France", "03-45-67-89-01", "1990-09-10",
     "Moreau", "Philippe", "1965-06-30", "Lefebvre", "Catherine", "1970-12-05"),
    ("Lefevre", "Sophie", "234 Rue du Faubourg", "France", "04-56-78-90-12", "1982-03-25",
     "Lefevre", "Michel", "1958-09-15", "Garcia", "Nathalie", "1963-11-20"),
    ("Roux", "Antoine", "567 Rue de la Paix", "France", "05-67-89-01-23", "1995-11-05",
     "Roux", "Bernard", "1970-04-20", "Blanc", "Sylvie", "1975-08-10"),
    ("Girard", "Elodie", "890 Boulevard des Capucines", "France", "06-78-90-12-34", "1988-12-30",
     "Girard", "David", "1960-11-12", "Robin", "Christine", "1965-02-25"),
    ("Bonnet", "Julien", "123 Rue de Rivoli", "France", "07-90-12-34-56", "1984-06-18",
     "Bonnet", "Vincent", "1963-07-22", "Chevalier", "Sophie", "1968-10-15"),
    ("Thomas", "Cécile", "456 Avenue de la Grande Armée", "France", "08-01-23-45-67", "1992-10-08",
     "Thomas", "Alain", "1975-01-05", "Rousseau", "Sandrine", "1980-03-30"),
    ("Robert", "Lucas", "789 Rue de la Madeleine", "France", "09-34-56-78-90", "1987-04-02",
     "Robert", "Franck", "1967-12-12", "Petit", "Caroline", "1972-09-25"),
    ("Richard", "Manon", "234 Avenue des Champs-Élysées", "France", "10-45-67-89-01", "1998-08-20",
     "Richard", "Olivier", "1980-05-18", "Leroy", "Elise", "1985-11-15"),
    ("Trepos", "Stephane", "234 Avenue des Champs-Élysées", "France", "10-45-67-89-01", "1998-08-20",
     "Trepos", "Bertand", "1980-05-18", "Leroy", "Elise", "1985-11-15"),
    ("Poulichet", "Patricia", "234 Avenue des Champs-Élysées", "France", "10-45-67-89-01", "1998-08-20",
     "Poulichet", "Joseph", "1980-05-18", "Poulichet", "Irène", "1985-11-15"),
]

# Register 10 users
for data in users_data:
    platform.register_user(*data)
  
# Display potential parents
print("Potential Parents for", new_user.first_name, new_user.name, ":")
for user in platform.users:
    if (user.name == new_user.father_name and user.first_name == new_user.father_first_name and user.date_of_birth == new_user.father_date_of_birth) or \
       (user.name == new_user.mother_name and user.first_name == new_user.mother_first_name and user.date_of_birth == new_user.mother_date_of_birth):
        print("    ", user.first_name, user.name, user.date_of_birth)


# After registering, prompt the user to choose an action
print(" ")
print("You are now registered. What would you like to do? ")
print(" ")
print("1. Add a direct parent")
print("2. Add a child")

choice = input("Enter the number corresponding to your choice: ")


if choice == "1":
    # Prompt the user to enter parent information
    parent_name = input("Enter the parent's last name: ")
    parent_first_name = input("Enter the parent's first name: ")
    parent_date_of_birth = input("Enter the parent's date of birth (YYYY-MM-DD): ")

    # Create the parent user
    parent_user = platform.register_user(parent_name, parent_first_name, "", "", "", parent_date_of_birth, "", "", "", "", "", "")
    
    # Add the parent to the user's record
    new_user.add_parent(parent_user)
    print("Parent added successfully!")
    
elif choice == "2":
    # Prompt the user to enter child information
    child_name = input("Enter the child's last name: ")
    child_first_name = input("Enter the child's first name: ")
    child_date_of_birth = input("Enter the child's date of birth (YYYY-MM-DD): ")
    
    # Create the child user
    child_user = platform.register_user(child_name, child_first_name, "", "", "", child_date_of_birth, "", "", "", "", "", "")
    
    # Add the child to the user's record
    new_user.add_child(child_user)
    print("Child added successfully!")
    
else:
    print("Invalid choice.") 


"""
# Example Usage:
# Creating an instance of an administrator
admin = Administrator("Trepos", "Pauline", "1 avenue champs elysée 75001 Paris", "Française", "0612233445", "17/02/2003")

# Creating an instance of a family tree
family_tree = FamilyTree()

# Creating an instance of a user
user = User("Moutarde", "Ketchup", "Mcdo de Cergy", "Américain", "+600020305", "01/01/1970",
            "Gog", "Hot", "01/01/1850", "Nini", "Pa", "02/01/1850")

# Authenticating the user
#Authentication.authenticate_user(user)

# Adding the user to the family tree
family_tree.add_person(user)
"""



