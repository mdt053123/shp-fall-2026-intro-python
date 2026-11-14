"""Solution - Exercise 4: Contact Book (with the multiple-numbers bonus)"""

# Bonus version: each name maps to a LIST of numbers
contacts = {"Ada": ["212-555-0101"], "Alan": ["917-555-0199"]}


def clean_name(name):
    return name.strip().capitalize()


def add_contact(contacts):
    name = clean_name(input("Name: "))
    number = input("Number: ").strip()
    if name not in contacts:
        contacts[name] = []
    contacts[name].append(number)
    print(f"Saved {number} for {name}.")


def look_up(contacts):
    name = clean_name(input("Name to look up: "))
    if name in contacts:
        print(f"{name}: {', '.join(contacts[name])}")
    else:
        print("Not found.")


def delete_contact(contacts):
    name = clean_name(input("Name to delete: "))
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}.")
    else:
        print("Not found.")


def list_contacts(contacts):
    if not contacts:
        print("(no contacts)")
    for name in sorted(contacts):
        print(f"  {name:<10} {', '.join(contacts[name])}")


def search(contacts):
    text = input("Search for: ").strip().lower()
    found = False
    for name in sorted(contacts):
        if text in name.lower():
            print(f"  {name:<10} {', '.join(contacts[name])}")
            found = True
    if not found:
        print("No matches.")


while True:
    print("\n1) Add  2) Look up  3) Delete  4) List  5) Search  6) Quit")
    choice = input("> ").strip()
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        look_up(contacts)
    elif choice == "3":
        delete_contact(contacts)
    elif choice == "4":
        list_contacts(contacts)
    elif choice == "5":
        search(contacts)
    elif choice == "6":
        print("Bye!")
        break
    else:
        print("Please choose 1-6.")
