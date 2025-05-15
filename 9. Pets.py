pets = []

def add_pet():
    name = input("Name: ")
    species = input("Species: ")
    try:
        age = int(input("Age: "))
        pets.append({'name': name, 'species': species, 'age': age})
    except:
        print("Invalid age.")

def find_by_species():
    species = input("Search species: ")
    for p in pets:
        if p['species'].lower() == species.lower():
            print(p)

def filter_by_age():
    try:
        max_age = int(input("Maximum age: "))
        for p in pets:
            if p['age'] <= max_age:
                print(p)
    except:
        print("Invalid age.")

def menu():
    while True:
        print("\n1. Add pet\n2. Search by species\n3. Filter by age\n4. Exit")
        op = input("Option: ")
        if op == '1': add_pet()
        elif op == '2': find_by_species()
        elif op == '3': filter_by_age()
        elif op == '4': break
        else:
            print("Invalid option.")

menu()
