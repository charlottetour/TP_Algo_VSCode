def addition(a, b):
    return a + b

def afficher_menu():
    print("=== Programme de test Git et VS Code ===")
    print("1. Addition")
    print("2. Quitter")

while True:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        a = float(input("Entrez un nombre : "))
        b = float(input("Entrez un deuxième nombre : "))
        print("Résultat =", addition(a, b))
        print()
    elif choix == "2":
        print("Au revoir !")
        break
    else:
        print("Choix invalide.\n")

def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def afficher_menu():
    print("=== Programme de test Git et VS Code ===")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Quitter")

while True:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        a = float(input("Entrez un nombre : "))
        b = float(input("Entrez un deuxième nombre : "))
        print("Résultat =", addition(a, b))
        print()

    elif choix == "2":
        a = float(input("Entrez un nombre : "))
        b = float(input("Entrez un deuxième nombre : "))
        print("Résultat =", multiplication(a, b))
        print()

    elif choix == "3":
        print("Au revoir !")
        break

