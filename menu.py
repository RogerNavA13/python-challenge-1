# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"\nYou selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"\nWhat {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("\nType menu item number: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    # Store the item name as a variable
                    selected_item = menu_items[menu_selection]["Item name"]
                    selected_price = menu_items[menu_selection]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"\nHow many {selected_item} would you like? ")

                    # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        print("Invalid quantity. Defaulting to 1.")
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": selected_item,
                        "Price": selected_price,
                        "Quantity": quantity
                    })
                    print(f"\nAdded {quantity} {selected_item} to your order.")
                else:
                    print("\nThat menu item number doesn't exist.")
            else:
                print("\nYou didn't select a valid number.")
        else:
            print(f"\n{menu_category} was not a menu option.")
    else:
        print("\nYou didn't select a number.")

    while True:

        # Ask the customer if they would like to order anything else
        keep_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o: ")

        # 5. Check the customer's input
        if keep_ordering.lower() in ['y', 'yes']:
                # Keep ordering
                # Exit the keep ordering question loop

                break
        elif keep_ordering.lower() in ['n', 'no']:

                # Complete the order
                place_order = False
                print("\nThank you for your order!")
                break
        else:
            # Tell the customer to try again
            print("Invalid input. Please type 'Y' or 'N'.")
                

# Print out the customer's order
if order:  # Only print if there are items in the order
    print("\nThis is what we are preparing for you.\n")

    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")


# 6. Loop through the items in the customer's order
    for item in order:
    # 7. Store the dictionary items as variables
        name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
        name_spaces = " " * (24 - len(name))
        price_spaces = " " * (6 - len(str(price)))

    # Print the item name, price, and quantity
        print(f"{name}{name_spaces} | ${price}{price_spaces} | {quantity}")

# Calculate and print the total cost
    total_cost = sum(item["Price"] * item["Quantity"] for item in order)
    print("\nTotal cost: ${:.2f}".format(total_cost))
else:
    print("\nNo items were ordered.")