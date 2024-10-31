class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        
        self.menu()
    def menu(self):
        user_input = input("""
                           1.Enter 1 to create the pin
                           2.Enter 2 to deposit the amount
                           3.Enter 3 to with drawl
                           4.Enter 4 to check the balance
                           5.Enter 5 to Exit
                        """)
        if user_input == '1':
            self.create_pin()
        if user_input == '2':
            self.deposit()
        if user_input == '3':
            self.with_drawl()
        if user_input == '4':
            self.check_balance()
        if user_input == '5':
            print('Exited From menu')
    def create_pin(self):
        self.pin += input('Enter the pin:')
        print('Pin succesfully created ✌️')
        self.menu()
    def deposit(self):
        temp = input('Enter the Pin: ')
        if temp == self.pin:
            self.balance += int(input("Enter the amount:"))
            print('Deposit succesfull 😎')
        else:
            print("Invalid Pin")
        self.menu()
    def check_balance(self):
        temp = input('Enter the Pin:')
        if temp == self.pin:
            print(f'the balance amount is {self.balance}')
        else:
            print('Invlaid Pin')
        self.menu()
    def with_drawl(self):
        temp = input('Enter the pin:')
        if temp == self.pin:
            amount = int(input("Enter the Amount:"))
            if amount <= self.balance:
                self.balance -= amount
                print('with_drawl successfull 🤑')
            else:
                print('Insufficient_funds')
        else:
            print("Invalid Input")
        
        
        self.menu()
    

obj = Atm()