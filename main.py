#Coffe machine code



machine_is_on = True


#Stock available in the machine
stock_status = {
    "Water": 100,
    "Milk": 50,
    "Coffee": 76,
    "Money": 2.5
}


#Menu with resource requirements
menu = {
    "espresso": {
        "ingredients": {"Water": 50, "Milk": 0, "Coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"Water": 200, "Milk": 150, "Coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"Water": 250, "Milk": 100, "Coffee": 24},
        "cost": 3.0
    }
}

#Function to check resources
def check_resources(drink):
    """Check if resources are sufficient for the chosen drink"""
    ingredients = menu[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > stock_status[item]:
            print(f"Sorry there is not enough {item}. Ask Admin to refill")
            return False
    return True


#function for adding to refill stock
def admin_refill():
    print("\n--- Admin Stock Refill ---")
    for item in stock_status:
        if item != "Money":
            add_amount = int(input(f"Add how much {item}? Current = {stock_status[item]}: "))
            stock_status[item] += add_amount

    print("Stock updated Successfully")



while machine_is_on:
    choice = input("What would you like? (espresso/latte/ cappuccino): ").lower()

    if check_resources(choice):
        print(f"Thanks fpr choosing {choice}! making your drink...")
        #Deduct the used resources
        for item in menu[choice]["ingredients"]:
            stock_status[item] -= menu[choice]["ingredients"][item]
    #If not enough won't make the drink


    elif choice == "report":
        print(stock_status)

    elif choice == "admin":
        password = input("Enter PW: ")
        if password == '1234':
            admin_refill()

        else:
            print("Wrong password!. Access Denied..")


    elif choice == "off":
        print("Coffee Machine Successfully Turned OFF!!!")
        machine_is_on = False

    else:
        print("Invalid Choice. Please try again")









