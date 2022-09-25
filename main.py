
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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
        return True


def coins():
    """ returns the total money inserted"""
    print("please insert coins.")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes:  "))
    nickles = int(input("how many nickles:  "))
    pennies = int(input("how many pennies:  "))
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.0


def make_coffee(coffee_ingredients):
    """ deduct the coffee ingredients from resources"""
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    return resources


is_on = True

while is_on:
    user_input = input("What would you like (espresso,cappuccino,latte) : ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if is_resources_sufficient(drink['ingredients']):
            charge = coins()
            cost = drink['cost']
            if charge >= cost:
                profit += cost
                make_coffee(drink['ingredients'])
                print(f"your {user_input} is ready, enjoy! ")
                if charge > cost:
                    change = charge - cost
                    print(f"Here is ${change} dollars in change")
            if charge < cost:
                print("Sorry that's not enough money.Money refunded.")
















