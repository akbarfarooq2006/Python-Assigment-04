# MadLibs Project (Improved)



print("Welcome to MadLibs! Let's create a fun story.")

# Input lena aur validate karna
while True:
    noun = input("Enter a noun (person, place, or thing): ").strip()
    if noun:
        break
    print("Please enter something!")

while True:
    verb = input("Enter a verb (action word): ").strip()
    if verb:
        break
    print("Please enter something!")

while True:
    adjective = input("Enter an adjective (describing word): ").strip()
    if adjective:
        break
    print("Please enter something!")

while True:
    place = input("Enter a place: ").strip()
    if place:
        break
    print("Please enter something!")

# Lambi story template
story = f"In a faraway land, there was a {adjective} {noun} who loved to {verb}. " \
        f"One sunny day, they went to {place} to explore. " \
        f"Everyone in {place} was amazed by the {adjective} {noun} and joined in to {verb} together!"

# Output
print("\nHere's your MadLibs story:")
print(story ,"\n")