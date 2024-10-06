MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}



#TODO: Ask user what does he want to drink: “What would you like? (espresso/latte/cappuccino): ”
#TODO: If coffe machine has resources matching the drink continue else print not enough resources.
#TODO: Ask the user to input money:  quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#TODO: Check if the user inputed enough money. IF yes calculate change and give back ELSE not enough money
#and refund inserted money
#TODO: If the transaction is successful make a coffe and deduct the ingredients
#TODO: Create print function that prints how many resources are left.


def check_for_ingredients():
    for ingredient in MENU[user_choice]["ingredients"]:
        if resources[ingredient] < MENU[user_choice]["ingredients"][ingredient]:
            print(ingredient)
            return False
    return True

def report():
    print(f'''
        water: {resources["water"]},
        milk: {resources["milk"]},
        coffe: {resources["coffee"]}
        money: {stored_money}
    ''')

def transaction():
    global stored_money

    print('Please insert coins.')
    quarters = int(input('How many quarters?: ')) * 0.25
    dimes = int(input('How many dimes?: ')) * 0.1
    nickles = int(input('How many nickles?: ')) * 0.05
    pennies = int(input('How many pennies?: ')) * 0.01

    total_money = quarters + dimes + nickles + pennies
    if total_money >= MENU[user_choice]["cost"]:
        for ingredient in MENU[user_choice]["ingredients"]:
            resources[ingredient] -= MENU[user_choice]["ingredients"][ingredient]
        if total_money > MENU[user_choice]["cost"]:
            change = total_money - MENU[user_choice]["cost"]
            stored_money += MENU[user_choice]["cost"]
            print(f'Here is your change {round(change, 2)}')
            print(f'Here is you {user_choice}. Enjoy!')
    else:
        print('Not enough money.')


stored_money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while True:
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')

    if user_choice == "report":
        report()
    elif user_choice == 'off':
        print('Good by!')
        break
    elif user_choice not in MENU:
        print('provide valid input')
    elif check_for_ingredients():
        print('Sorry not enough resources')
    else:
        transaction()

