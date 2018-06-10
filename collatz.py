def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    n = int(input('Type a number: '))
except ValueError:
    print('You must type a number!')
else:
    print('=' * 45)
    print('The Collatz conjecture for the number ' + str(n) + ' is: ')
    aux = 0
    new = n

    while True:
        aux = collatz(new)
        new = collatz(aux)
        if aux == 1:
            new = ' '
        print(aux, new, end=' ')
        if aux == 1 or new == 1:
            break
