from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu=Menu()

is_on = True


while is_on:
    options=menu.get_items()
    choice=input(f"What would you like to have ({options}): ")
    if choice == "off":
        is_on=False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        can_make=coffee_maker.is_resource_sufficient(drink)
        price=drink.cost
        print(f"price of {choice} is {price}")
        if can_make:
            # total_money=money_machine.process_coins()
            payment=money_machine.make_payment(price)
            if payment:
                coffee_maker.make_coffee(drink)

