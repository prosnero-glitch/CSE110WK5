


print("Welcome to the Shopping Cart Program!")
product=input("Enter the product name to add to the shopping cart: ")
print(f"Added {product} to the shopping cart.")
# Display the contents of the shopping cart
print("Contents of the shopping cart:")
print(product)
# Add a new item
print("Add a new item:")
new_item=input("Enter the name of the new item: ")
print(f"Added {new_item} to the shopping cart.")
# Display the contents of the shopping cart
print("Contents of the shopping cart:")
print(product)
print(new_item)
# List of available items
print("Available items:")
print("1. Mat")
print("2. Bed")
print("3. Mop")
print("4. Vacuum")
print("5. Umbrella")
print("6. Quit")
# Have menu system that repeats until the user chooses quit.
while True:
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        print("You selected Mat.")
    elif choice == "2":
        print("You selected Bed.")
    elif choice == "3":
        print("You selected Mop.")
    elif choice == "4":
        print("You selected Vacuum.")
    elif choice == "5":
        print("You selected Umbrella.")
    elif choice == "6":
        print("Quitting...")
        break
    else:
        print("Invalid choice. Please try again.")