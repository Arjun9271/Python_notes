# daily expense tracker

expenses = []

def add_expenses(description,amount):
     expenses.append({'description':description,'amount':amount})


def view_expenses():
    for expense in expenses:
        print(f'{expense['description']}:${expense['amount']}')
        
def reset_expenses():
    expenses.clear()
    print(f'expenses:{len(expenses)}')


def total_cost():
    print(f'sum :${sum(expense['amount'] for expense in expenses)}')



        
add_expenses('surfexel',218)
add_expenses('snickers',35)


view_expenses()
total_cost()

