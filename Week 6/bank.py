bank = {'Chad': [1000, 1000],
        'Grant': [1001,2000],
        'Jake': [1002, 500],
        }

def examine(name):
    '''this function takes a name and returns the corresponding in the bank list'''
    return print(bank[name])

def insert():
    '''this function insets a name, member number, and amount into the bank list'''
    name = input("Enter the member name: ")
    number = input("Enter the member number: ")
    amount = input("Enter the amount: ")
    bank[name].append(number)
    bank[name].append(amount)
    return

def delete():
    '''this function deletes a name, member number, and amount from the bank list'''
    name = input("Enter the member name: ")
    number = input("Enter the member number: ")
    amount = input("Enter the amount: ")
    bank[name].remove(number)
    bank[name].remove(amount)
    return

def withdraw():
    '''this function withdraws an amount from a member'''
    number = input("Enter the member number: ")
    amount = input("Enter the amount: ")
    withdraw(number, amount)
    return

def deposit():
    '''this function deposit an amount into a member'''
    number = input("Enter the member number: ")
    amount = input("Enter the amount: ")
    deposit(number, amount)
    return

#intialise the bank
print("what do you want to do? ")
function = input("Check, Withdraw, Deposit, Admin :")

if function == "Check":
    name = input("Enter the member name: ")
    examine(name)

elif function == "Withdraw":
    number = input("Enter the member number: ")
    amount = input("Enter the amount: ")
    withdraw(number, amount)
    

elif function == "Deposit":
    number = input("Enter the member number: ")
    amount = input("Enter the amount: ")
    deposit(number, amount)

elif function == "Admin":
    choice = input("Insert or Delete? : ")
    if choice == "Insert":
        insert()
    elif choice == "Delete":
        delete()

    else:
        print("invalid choice")
else:
    print("invalid choice")




    