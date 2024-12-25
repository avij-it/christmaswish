import random

# Predefined list of Christmas wish templates
wishes = [
    "Merry Christmas, [Name]! Wishing you joy and peace this holiday season.",
    "Happy Holidays, [Name]! May your Christmas be filled with love and happiness.",
    "Season's Greetings, [Name]! Hope your holiday season is magical and bright.",
    "Merry Christmas, [Name]! May your days be merry and bright.",
    "Wishing you a joyful Christmas, [Name]! Stay blessed."
]

def generate_wish(name):
    """Generate a Christmas wish for the given name."""
    wish_template = random.choice(wishes)
    return wish_template.replace("[Name]", name)

def save_wish_to_file(wish, file_name="christmas_wishes.txt"):
    """Save the wish to a text file."""
    with open(file_name, "a") as file:
        file.write(wish + "\n")
    print(f"Wishing saved to {file_name}.")

def main():
    print("🎄 Welcome to the Christmas Wish Generator! 🎄")
    
    while True:
        # Get the user's name for customization
        name = input("Enter the name to customize the wish (or type 'exit' to quit): ").strip()
        if name.lower() == 'exit':
            print("Thank you for using the Christmas Wish Generator! 🎅")
            break

        # Generate and display the wish
        wish = generate_wish(name)
        print(f"\nGenerated Wish: {wish}\n")

        # Ask if the user wants to save the wish
        save = input("Would you like to save this wish to a file? (yes/no): ").strip().lower()
        if save == 'yes':
            save_wish_to_file(wish)
        print()

if __name__ == "__main__":
    main()
