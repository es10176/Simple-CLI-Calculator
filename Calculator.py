def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print('\n\nWelcome to your calculator!')
    Operation1 = input('\n\nSelect Operation:\n\n[1] Add\n[2] Subtract\n[3] Multiply\n[4] Divide\n\n: ')

    if Operation1 in ('1', '2', '3', '4'):
        num1 = float(input('\nEnter first number: '))
        num2 = float(input('\nEnter second number: '))

    if Operation1 == '1':
        print(num1, '+', num2, '=', add(num1, num2))
        solution1 = input('\nPress Enter to continue...')

    elif Operation1 == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))
        solution2 = input('\nPress Enter to continue...')

    elif Operation1 == '3':
        print(num1, '*', num2, '=', multiply(num1, num2))
        solution3 = input('\nPress Enter to continue...')

    elif Operation1 == '4':
        print(num1, '/', num2, '=', divide(num1, num2))
        solution4 = input('\nPress Enter to continue...')