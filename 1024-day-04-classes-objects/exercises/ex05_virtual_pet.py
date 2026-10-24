"""
Exercise 5 - Virtual Pet (open-ended)
-------------------------------------
Design a Pet class and a game loop, Tamagotchi-style.

Pet should have (at least):
  attributes: name, hunger (0-10), happiness (0-10), energy (0-10), age
  methods:
    feed()    -> hunger goes down by 3 (never below 0)
    play()    -> happiness +3, energy -2, hunger +1 (can't play if energy < 2)
    sleep()   -> energy back to 10, hunger +2
    tick()    -> called after EVERY action: age +1, hunger +1, happiness -1
    is_alive()-> False if hunger reaches 10 or happiness reaches 0
    __str__   -> a status line, e.g.  "Mochi (age 4)  hunger 3/10  happy 7/10  energy 5/10"

Game loop:
  - Ask for the pet's name.
  - Each turn show the status and a menu: feed / play / sleep / quit.
  - Call tick() after each action. End the game if the pet is no longer alive,
    and report how many turns it survived.

Bonus ideas:
  - A mood() method that returns an emoji based on the stats.
  - Keep values in range with a helper: def clamp(x): return max(0, min(10, x))
  - Several pets at once (a list of Pet objects)!
"""

# TODO
