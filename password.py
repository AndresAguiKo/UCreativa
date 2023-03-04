# Analizar password 
# Recomendacion de uno mas seguro
# Almacenar passwords para que funcione como una plataforma llamada 1Password

# Lo primero es crear los menus, 

print("-------------------------------------------------")
print ("Welcome to UrPass") #nombre de la app/web
print("-------------------------------------------------")

# Change everything to english "IMPORTANT"


# Olvidé declarar random y string / Hacer double check 

import random
import string

def menu():
    while True:
        print("Please select an option:")
        print("A. Password Analyzer")
        print("B. Generate Password")
        print("C. Save Password")
        print("E. Exit")

        choice = input()

        if choice == "A":
            password = input("Enter the password you want to analyze: ")
            password_analyzer(password)
        elif choice == "B":
            password = generate_password()
            print("Generated password:", password)
        elif choice == "C":
            app_web = input("Enter the name of the wensite: ")
        elif choice == "D":
            break
        else:
            print("Invalid option. Please try again.")

            # ^ aca aariba me falta dos opciones que es la guardar el password/ sin emabrgo me falta info para completar este. 


def password_analyzer(password):
    length = len(password)
    lowercase = False
    uppercase = False
    digit = False
    special_char = False

    for char in password:
        if char.islower():
            lowercase = True
        elif char.isupper():
            uppercase = True
        elif char.isdigit():
            digit = True
        elif char in "!@#$%^&*()_+-=[]{}|;':\",./<>?":
            special_char = True

    if length < 8:
        print("The password is very short. It is recommended to use at least 8 characters.")
        return False
    elif not lowercase:
        print("Must contain an lowercase letter.")
        return False
    elif not uppercase:
        print("Must contain an uppercase letter.")
        return False
    elif not digit:
        print("Must contain at least one number.")
        return False
    elif not special_char:
        print("Must contain a special character .")
        return False
    else:
        print("Password is secure.")
        return True

def generate_password():
    while True:
        password = "".join([random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;':\",./<>?") for _ in range(12)])
        if password_analyzer(password):
            return password


password = input("Ingresa tu contraseña: ")
if not password_analyzer(password):
    print("Weak password, it is recommended to change it.")
    print("We provide a secure password:")
    print(generate_password())
