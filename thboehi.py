
print("----------")
print("Exercice 8")
# Générateur de mot de passe
import random
import string
import pyperclip


def password_generator(length):
    if length < 6:
        print("La longueur d'un mot de passe ne doit pas faire moins de 6 caractères pour des questions de sécurité")
        return
    
    lettres_maj = string.ascii_uppercase
    lettres_min = string.ascii_lowercase
    chiffres = string.digits
    special_chars = "!@#$%^&*()-_=+<>?"
    password_chars = lettres_maj + lettres_min + chiffres + special_chars

    minimum_required = [
        random.choice(lettres_maj),
        random.choice(lettres_min),
        random.choice(chiffres),
        random.choice(special_chars)
    ]

    password_full = random.choices(password_chars, k=length-4) + minimum_required

    random.shuffle(password_full)

    return "".join(password_full)

while True:
    try:
        print("Choisis la longeur du mot de passe (min. 6)\n0 pour quitter...")
        length_int = int(input(""))
        # length_int = int(length_input)

        #Quitter la boucle
        if length_int == 0:
            print("Ok bye, merci !")
            break

        if length_int < 6:
            print("!! Erreur : On avait dit 6 minimum.")
            continue
        password = password_generator(length_int)
        print("--------------------")
        print("Le mot de passe est ")
        print(password)
        print("Copié dans le clipboard")
        print("--------------------")
        pyperclip.copy(password_generator(length_int))

    except ValueError:
        
        print("!! Erreur : Merci de donner un nombre...")
        continue

print("Yo.")