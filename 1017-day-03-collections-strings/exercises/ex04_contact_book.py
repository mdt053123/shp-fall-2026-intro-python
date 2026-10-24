"""
Exercise 4 - Contact Book
-------------------------
Build a menu-driven contact book. Store contacts in a dict:
    contacts = {"Ada": "212-555-0101", "Alan": "917-555-0199"}

Menu (loop until the user quits):
    1. Add / update a contact
    2. Look up a contact       (print "Not found" if missing; don't crash!)
    3. Delete a contact
    4. List all contacts       (sorted alphabetically)
    5. Search                  (show every contact whose name CONTAINS some text,
                                ignoring case, e.g. "a" matches Ada and Alan)
    6. Quit

Requirements:
  - Write a separate function for each menu option, e.g.
        def add_contact(contacts): ...
  - Names should be stored with a capital first letter no matter how the user
    types them (hint: .strip().capitalize()).

Bonus: let each person have MULTIPLE numbers (a dict of lists!).
"""

contacts = {"Ada": "212-555-0101", "Alan": "917-555-0199"}

# TODO: write your functions and menu loop
