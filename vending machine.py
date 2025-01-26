class VendingMachine:
    def __init__(self):
        # Initialize the vending machine with items, their prices, and stock levels
        self.items = {
            'drinks': {
                'Coffee': {'price': 2.5, 'stock': 5},
                'Tea': {'price': 1.8, 'stock': 3},
                'Soda': {'price': 1.5, 'stock': 10},
                'Water': {'price': 1.0, 'stock': 8}
            },
            'snacks': {
                'Chips': {'price': 1.0, 'stock': 6},
                'Chocolate': {'price': 1.5, 'stock': 4},
                'Cookies': {'price': 1.2, 'stock': 7},
                'Biscuits': {'price': 1.3, 'stock': 3}
            }
        }

    def display_menu(self):
        # Display the available categories: Drinks or Snacks
        print("\n--- Vending Machine ---")
        print("Please choose a category:")
        print("1. Drinks")
        print("2. Snacks")
        print("3. Exit")

    def display_items(self, category):
        # Display the items in the selected category (drinks or snacks)
        print(f"\n--- {category} ---")
        items = self.items[category]
        for idx, item in enumerate(items.keys(), start=1):
            stock = items[item]['stock']
            print(f"{idx}. {item} - ${items[item]['price']} (Stock: {stock})")

    def process_purchase(self, selected_item, category, amount_inserted):
        # Process the user's purchase: check if they have enough money and stock
        item_info = self.items[category][selected_item]
        price = item_info['price']
        stock = item_info['stock']
        
        if stock == 0:
            print(f"Sorry, {selected_item} is out of stock.")
            return False
        
        if amount_inserted < price:
            print(f"Sorry, you need ${price - amount_inserted} more.")
            return False
        
        # Deduct stock and calculate change
        item_info['stock'] -= 1
        change = amount_inserted - price
        print(f"\nDispensing {selected_item}... Enjoy!")
        print(f"Your change: ${change:.2f}")
        return True

    def suggest_additional_purchase(self, selected_item, category):
        # Suggest an additional item based on user's selection
        if category == 'drinks' and selected_item == 'Coffee':
            print("\nSuggestion: How about some Biscuits with your coffee?")
        elif category == 'drinks' and selected_item == 'Tea':
            print("\nSuggestion: A nice snack would go well with your tea!")
        elif category == 'snacks' and selected_item == 'Chips':
            print("\nSuggestion: A refreshing Soda would be a great pairing with Chips.")
        else:
            print("\nEnjoy your purchase! Would you like to buy anything else?")

    def run(self):
        while True:
            self.display_menu()
            try:
                # Get user's menu choice
                choice = int(input("Enter your choice (1-3): "))
                if choice == 1:
                    self.display_items('drinks')
                    drink_choice = int(input("Select a drink by number: ")) - 1
                    selected_drink = list(self.items['drinks'].keys())[drink_choice]
                    amount_inserted = float(input(f"Insert money (Price: ${self.items['drinks'][selected_drink]['price']}): "))
                    if self.process_purchase(selected_drink, 'drinks', amount_inserted):
                        self.suggest_additional_purchase(selected_drink, 'drinks')
                elif choice == 2:
                    self.display_items('snacks')
                    snack_choice = int(input("Select a snack by number: ")) - 1
                    selected_snack = list(self.items['snacks'].keys())[snack_choice]
                    amount_inserted = float(input(f"Insert money (Price: ${self.items['snacks'][selected_snack]['price']}): "))
                    if self.process_purchase(selected_snack, 'snacks', amount_inserted):
                        self.suggest_additional_purchase(selected_snack, 'snacks')
                elif choice == 3:
                    print("Thank you for using the Vending Machine. Goodbye!")
                    break
                else:
                    print("Invalid choice, please select again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except IndexError:
                print("Invalid selection. Please choose a valid item number.")

            # Ask if the user wants to buy another item
            another_purchase = input("\nWould you like to buy another item? (yes/no): ").lower()
            if another_purchase != 'yes':
                print("Thank you for using the Vending Machine. Goodbye!")
                break


# Running the vending machine
vending_machine = VendingMachine()
vending_machine.run()
