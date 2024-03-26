import os
class ExpenseBills:
    def __init__(self,expense_amount=10000):
        self.expense_amount=expense_amount
        self.items=[]
        self.Total_Price=0
        self.balance=expense_amount

    def add_expense(self,item,amount):
        with open('Expense.txt','a')as file:
            file.write(f'{item}:{amount}\n')
            if self.balance==0 or self.balance<amount:
                print('No balance\n')
            else:
                self.items.append((item,amount))
                print('Expense added successfully.')
                self.Total_Price+=amount
                self.balance=self.balance-self.Total_Price
            
    def view_items(self):
        if not self.items:
            print('No items added yet.')
        else:
            print('Items:')
            for item,amount in self.items:
                print(f'{item}: ${amount}')

    def Total_Amount(self):
        if not self.items:
            print('No items added yet.')
        else:
            print(f'Total Amount Spent: ${self.Total_Price}')
    def show_balance(self):
        if not self.items:
            print('No items added yet.')
        else:
            print(f'Balance: ${self.balance}')
        
    def save_to_file(self):
        with open('details.txt', 'w') as file:
            file.write('Expense Details:\n')
            file.write('Total Limit:10000\n')
            file.write('Items:\n')
            for item,amount in self.items:
                file.write(f'{item}: ${amount}\n')
            file.write(f'Total Spent: ${self.Total_Price}\n')
            file.write(f'Balance: ${self.balance}\n')
def main():
    e=ExpenseBills()
    while True:
        print('\nExpenses\n')
        print('1. Add Item')
        print('2. View Items')
        print('3. Calculate Total Amount')
        print('4. Show Balance')
        print('5.Expense Details')
        choice = input('Enter your choice: ')
        if choice == '1':
            item = input('Enter item name: ')
            price = int(input('Enter price: '))
            e.add_expense(item, price)
        elif choice == '2':
            e.view_items()
        elif choice == '3':
            e.Total_Amount()
        elif choice == '4':
            e.show_balance()
        elif choice == '5':
            e.save_to_file()
            print('\nCheck the Details File')
            break
main()

