import random
import sqlite3

BIN = 400000
ACCOUNT_NUMBER_LENGTH = 10


class SimpleBankingSystem:
    def __init__(self):
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS card (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    number TEXT,
                    pin TEXT,
                    balance INTEGER DEFAULT 0
                    )"""
        )
        conn.commit()
        conn.close()
        self.selected_account = 0

    def main_menu(self):
        while True:
            user_request_main_menu = input(
                f'1. Create an account\n'
                f'2. Log into account\n'
                f'0. Exit\n'
            )
            if user_request_main_menu == "1":
                self.create_account()
            elif user_request_main_menu == "2":
                if self.log_in_credentials():
                    log_in_output = self.log_into_account()
                    if log_in_output == "exit":
                        print("Bye!")
                        break
                    else:
                        pass
                else:
                    pass
            elif user_request_main_menu == "0":
                print("Bye!")
                break
            else:
                print("Invalid Input")

    def create_account(self):
        new_card = self.create_card_number()
        new_pin = self.create_pin_numb()
        self.save_new_account(new_card, new_pin)
        print(
            f"Your card has been created\n"
            f"Your card number:\n"
            f"{new_card}\n"
            f"Your card PIN:\n"
            f"{new_pin}\n"
        )

    def luhn_algorithm(self, number_as_string):
        control_value = 0
        control_list = [int(value) for value in number_as_string]
        if len(control_list) == 16:
            control_list.remove(control_list[15])
        for i in range(len(control_list)):
            if i % 2 == 0:
                control_list[i] *= 2
        for i in range(len(control_list)):
            if control_list[i] > 9:
                control_list[i] -= 9
        for i in range(len(control_list)):
            control_value += control_list[i]
        return control_value

    def create_card_number(self):
        card_number = str(BIN)
        while True:
            for i in range(ACCOUNT_NUMBER_LENGTH - 1):
                number = str(random.randint(0, 9))
                card_number += number
            checksum_value = 10 - self.luhn_algorithm(card_number) % 10
            card_number += str(checksum_value)
            if self.luhn_algorithm(card_number) % 10 == 0:
                break
        return card_number

    def create_pin_numb(self):
        pin = ""
        for i in range(0, 4):
            number = str(random.randint(0, 9))
            pin += number
        return pin

    def save_new_account(self, new_card, new_pin):
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        c.execute(f"INSERT INTO card (number, pin) VALUES ('{new_card}', '{new_pin}')")
        conn.commit()
        conn.close()

    def log_into_account(self):
        while True:
            user_request_login = input(
                f"1. Balance\n"
                f"2. Add income\n"
                f"3. Do transfer\n"
                f"4. Close account\n"
                f"5. Log out\n"
                f"0. Exit\n"
            )
            if user_request_login == "1":
                self.balance_request()
            elif user_request_login == "2":
                self.add_money_to_account()
            elif user_request_login == "3":
                self.transfer_out()
            elif user_request_login == "4":
                self.close_account()
            elif user_request_login == "5":
                system_command = "logout"
                return system_command
            else:
                system_command = "exit"
                return system_command

    def log_in_credentials(self):
        card_number = int(input("Enter your card number:\n"))
        if self.luhn_algorithm(str(card_number)) % 10 == 0:
            associated_pin = int(input("Enter your PIN:\n"))
            conn = sqlite3.connect('card.s3db')
            c = conn.cursor()
            accounts_in_database = c.execute('SELECT number FROM card')
            if card_number in accounts_in_database:
                pin_in_database = c.execute(f"SELECT pin FROM card WHERE number = {card_number}")
                if associated_pin == pin_in_database:
                    self.selected_account = card_number
                    print("You have successfully logged in!\n")
                    return True
                else:
                    return False
            else:
                return False
        else:
            print("Probably you made mistake in the card number. Please try again!\n")
            return False

    def balance_request(self):
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        account_balance = c.execute(f'SELECT balance FROM card WHERE number = {self.selected_account}')
        print(f"Balance: {account_balance}")

    def add_money_to_account(self):
        money_to_add = int(input("Enter income:\n"))
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        old_balance = c.execute(f'SELECT balance FROM card WHERE number = {self.selected_account}')
        new_balance = money_to_add + old_balance
        c.execute(f"UPDATE card SET balance = {new_balance} WHERE number = {self.selected_account}")
        conn.commit()
        conn.close()

    def transfer_out(self):
        account_to_transfer_to = int(input("Enter card number:\n"))
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        accounts_in_database = c.execute('SELECT number FROM card')
        user_account_balance = c.execute(f'SELECT balance FROM card WHERE number = {self.selected_account}')
        if account_to_transfer_to in accounts_in_database:
            amount_to_transfer = int(input("Enter how much money you want to transfer:\n"))
            if user_account_balance < amount_to_transfer:
                print("Not enough money!\n")
            else:
                print("Success!\n")
                c.execute(f"UPDATE card SET balance = {user_account_balance - amount_to_transfer}"
                          f"WHERE number = {self.selected_account}")
                conn.commit()
                conn.close()
        else:
            print("Such a card does not exist.\n")

    def close_account(self):
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        c.execute(f'DELETE FROM card WHERE number = {self.selected_account}')


run_bank_system = SimpleBankingSystem()
run_bank_system.main_menu()