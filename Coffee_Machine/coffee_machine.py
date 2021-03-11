class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"""\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money\n"""

    def take(self):
        print(f"\nI gave you ${self.money}\n")
        self.money = 0

    def fill(self):
        print()
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        print()

    def buy_menu(self):
        print()
        order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if order == "1":
            coffee_machine.make_coffee(espresso)
        elif order == "2":
            coffee_machine.make_coffee(latte)
        elif order == "3":
            coffee_machine.make_coffee(cappuccino)
        elif order == "back":
            print()
            pass

    def make_coffee(self, menu):
        if self.water < menu.water:
            print("Sorry, not enough water!")
        elif self.milk < menu.milk:
            print("Sorry, not enough milk!")
        elif self.beans < menu.beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups < menu.cups:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= menu.water
            self.milk -= menu.milk
            self.beans -= menu.beans
            self.cups -= menu.cups
            self.money += menu.money
        print()

    def main_menu(self):
        while True:
            user_choice = input("Write action (buy, fill, take, remaining, exit):")
            if user_choice == "buy":
                coffee_machine.buy_menu()
            elif user_choice == "fill":
                coffee_machine.fill()
            elif user_choice == "take":
                coffee_machine.take()
            elif user_choice == "remaining":
                print(coffee_machine)
            elif user_choice == "exit":
                break


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
espresso = CoffeeMachine(250, 0, 16, 1, 4)
latte = CoffeeMachine(350, 75, 20, 1, 7)
cappuccino = CoffeeMachine(200, 100, 12, 1, 6)
coffee_machine.main_menu()
