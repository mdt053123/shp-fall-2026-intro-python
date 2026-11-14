"""Solution - Exercise 5: Virtual Pet (one possible design)"""


def clamp(x):
    return max(0, min(10, x))


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 3
        self.happiness = 7
        self.energy = 8
        self.age = 0

    def feed(self):
        self.hunger = clamp(self.hunger - 3)
        print(f"{self.name} munches happily.")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
            return
        self.happiness = clamp(self.happiness + 3)
        self.energy = clamp(self.energy - 2)
        self.hunger = clamp(self.hunger + 1)
        print(f"{self.name} chases a ball!")

    def sleep(self):
        self.energy = 10
        self.hunger = clamp(self.hunger + 2)
        print(f"{self.name} takes a nap. Zzz...")

    def tick(self):
        self.age += 1
        self.hunger = clamp(self.hunger + 1)
        self.happiness = clamp(self.happiness - 1)

    def is_alive(self):
        return self.hunger < 10 and self.happiness > 0

    def mood(self):
        if self.hunger >= 8:
            return "😫"
        if self.happiness >= 7:
            return "😄"
        if self.happiness <= 3:
            return "😢"
        return "🙂"

    def __str__(self):
        return (f"{self.name} {self.mood()} (age {self.age})  hunger {self.hunger}/10  "
                f"happy {self.happiness}/10  energy {self.energy}/10")


pet = Pet(input("Name your pet: ").strip() or "Mochi")

while pet.is_alive():
    print("\n" + str(pet))
    choice = input("feed / play / sleep / quit? ").strip().lower()
    if choice == "feed":
        pet.feed()
    elif choice == "play":
        pet.play()
    elif choice == "sleep":
        pet.sleep()
    elif choice == "quit":
        break
    else:
        print("Unknown action.")
        continue
    pet.tick()

if not pet.is_alive():
    print(f"\nOh no! {pet.name} ran away after {pet.age} turns. Take better care next time!")
else:
    print(f"\nBye! {pet.name} made it {pet.age} turns.")
