print("Welcome to the Shopping Cart Program!")
# Store prices as well as names.
names_list = ["mat", "bed", "mop", "vacuum", "umbrella"]
prices_list = [2.00, 200.00, 15.00, 150.00, 25.00]

item_name = input("What item would you like to add? ")
item_price = float(input("What is the price of the item? "))
names_list.append(item_name)
prices_list.append(item_price)
# Change the display functionality to also display the prices of the items.
# Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol (for example $, €,
for i in range(5):
    print(f"{i + 1}. {names_list[i]} - ${prices_list[i]:.2f}")

# Complete the option to display the total amount of the prices of all the items in the shopping cart.
total = sum(prices_list)
print(f"Total: ${total:.2f}")

# Complete the option to remove an item from the shopping cart.
remove_item = int(input("Which item would you like to remove? "))
if 1 <= remove_item <= len(names_list):
    names_list.pop(remove_item - 1)
    prices_list.pop(remove_item - 1)
    print("Item removed.")
else:
    print("Invalid item number.")

