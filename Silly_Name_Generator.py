# Silly Name Generator from Impractical Python Projects

# Pseudocode
# Load a list of first names
# Load a list of surnames
# Choose a first name at random
# Assign the name to a variable
# Choose a surname at random
# Assign the name to a variable

import random
from tokenize import group

print("Welcome to the Psych 'Sidekick Name Picker.'\n")
print("A name just like Sean would pick for Gus:\n\n")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill")
last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom')

group = []

for i in range(3):
    full_name=random.choice(first) + " " + random.choice(last)
    group.append(full_name)
print(group)
