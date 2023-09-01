from data import MENU, resources

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/Cappuccino)"
is_on = True
money_of_machine = 0

while is_on:
    user_choice = input("What would you like? (espresso/latte/Cappuccino): ")

    # TODO: 2. Turn off the machine by entering "off" to the prompt.
    if user_choice == "off":
        is_on = False
    # TODO: 3. Print Report
    elif user_choice == "report":
        print(f"Money: ${money_of_machine}")
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
    else:
        # TODO: 4. Check resources sufficient?
        user_selection = MENU.get(user_choice)
        if user_selection is not None:
            for resource, quantity in user_selection["ingredients"].items():
                if resources[resource] < quantity:
                    print(f"Sorry, not enough {resource}.")
                    is_on = False
                    break
        else:
            print("Invalid choice. Please select a valid drink (espresso/latte/cappuccino), 'off', or 'report'.")

        if is_on:
            # TODO: 5. Process coins.
            print("Please Insert the coin.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickels = int(input("How many nickels?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01

            total_money = float(quarters + dimes + nickels + pennies)

            # TODO: 6. Check transaction successful?
            cost_of_drink = MENU[user_choice]["cost"]
            if total_money >= cost_of_drink:
                money_of_machine += cost_of_drink
                change = round(total_money - cost_of_drink, 2)
                print(f"Here is ${change} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")

            # TODO: 7. Make Coffee.
            print(f"Here is your {user_choice}. Enjoy!")

            for resource, quantity in user_selection["ingredients"].items():
                resources[resource] -= quantity
