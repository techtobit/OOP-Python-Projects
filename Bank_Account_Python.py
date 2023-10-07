#parent classs
class User:
    def __init__(self, name, age, gender, nid, balance, password):
        self.name = name
        self.age = age
        self.gender = gender
        self.nid = nid
        self.balance = balance
        self.password = password

    
    def show_details(self):
        print('Personal Details \n')
        print(f'Name : {self.name} \n')
        print(f'Age : {self.age} \n')
        print(f'Gender : {self.gender} \n')
        print(f'NID Number : {self.nid} \n')
        print(f'Balance : {self.balance} \n')

#Child Class
class Bank:

    # def __init__(self, name, age, gender, balance, password):
    #     super().__init__(name, age, gender, balance, password)
    #     self.accounts_list = []
    def __init__(self):
        self.accounts_list = []

    def createAccount(self, name, age, gender, nid, balance, password):
        user = User(name, age, gender, nid, balance, password)
        self.accounts_list.append(user)
        return user

    def deposit(self, balance):
        print(f'ammount is here {balance}')
        for user in Bank.accounts_list:
            print(f'{user.name}')
        # self.balance +=balance
        # deposit = User(balance)
        # print(f'deposit is here {deposit}')
        # self.accounts_list.append(deposit)
        print(f'Your account has been credit $ {self.balance} and total balance is $ {self.balance}\n')

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f'Insufficient Fund | Total avaliable balance is $ {self.balance}\n')
        else:
            self.balance -=amount
            # print(f'Your account has been debit $ {self.amount} and total balance is $ {self.balance}\n')
    
    def view_balance(self):
        self.show_details
        print(f'Account Balance : $ {self.balance} \n')

# def cont():
#     input('\n\nPress enter to continue\n\n')

# exit=0
# bank = Bank('Ashraf', 22, 'Male', 35, 1234)
bank = Bank()
newAc = bank.createAccount('Rifat', 23, 'Male', 1511, 90, 1234)



curentUser = 1511

while True:
    if curentUser == None:
        print('Please Login Frist\n')
        options = input('Login or Register (L\R) :')
        if options == 'L':
            nid = int(input('Type your nid number :'))
            password = int(input('Type your password :'))
            for user in bank.accounts_list:
                if user.nid == nid or user.password == password:
                    curentUser = user
                    match = True
                    print('Match\n')
                    break
                if match == False:
                    print('Unable to Login!\n Check Id, Pass and try agian \n Or create a new account \n')
        elif options == 'R':
            print('Create a new account!\n')
            name = input('Enter Full Name :')
            age  = int(input('Enter Age(Make sure DOB is same with NID) :'))
            gender = input('Enter your gender :')
            nid = int(input('Enter NID number :'))
            balance = int(input('Enter inital deposit to activate account :'))
            password = int(input('Enter you password :'))

            newUser = bank.createAccount(name, age, gender, nid, balance, password)
            print(f'Your account with name {newUser.name} created successfuly!\n')
            curentUser = newUser
    else:
        if curentUser == 1511:
        # name = Bank(input('Enter Name: '), int(input("Enter Age :")), input("Enter Gender"))
            print("\nWhat would you like to do( Enter a number)?")
            print(" 1 - Deposit")
            print(" 2 - Withdraw")
            print(" 3 - View Account Summary")
            print(" 4 - View Balance")
            print(" 5 - Logout")

            options = int(input("\nPlease Enter the option here : "))
            if options == 1:
                balance = int(input('Enter Deposit Ammount :'))
                bank.deposit(balance)
                # name.deposit(int(input('Enter Deposit Ammount :')))
            elif options == 2:
                name.withdraw(int(input('Enter Withdraw Ammount :')))
            elif options == 3:
                name.show_details()
            elif options == 4:
                name.view_balance()
            elif options == 5:
                curentUser = None