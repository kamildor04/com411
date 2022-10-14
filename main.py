# Activity 1
book = input("What type of book is this?")

if book == "Adventure":
    print("I like adventure books")
print("Finished reading book.")

# Activity 2

activity = input("Please enter the activity to be performed.")

if activity == "calculate":
    print("Performing calculations...")
print("Activity completed!")

# Activity 3

paint = input("Towards which direction should I paint (up, down, left or right)? ")

if paint == "up":
    print("I am painting in the upward direction!")
elif paint == "down":
    print("I am painting in the down direction!")
elif paint == "left":
    print("I am painting in the left direction!")
elif paint == "right":
    print("I am painting in the right direction!")
else:
    print("Your input is incorrect")

# Activity 4

number = int(input("Please enter a whole number"))
if (number % 2) == 0:
    print(f"The number {number} is an even number.")
else:
    print(f"The number {number} is an odd number.")

