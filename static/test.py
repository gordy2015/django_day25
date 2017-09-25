
def collatz(number):
    w = number % 2
    # print(w)
    if w == 0:
        number = number // 2
       # print(number)
        return number
    else:
        number = 3 * number + 1
        #print(number)
        return number

def game(a):
    print('start number--> %s' % a)
    while True:
        a = collatz(a)
        print('number: %s' %a)
        if a == 1:
            print('end number--> %s' %a)
            break
def play():
    while True:
        number = input('pls input which you want: ')
        if number == 'exit' or number == 'quit':
            break
        try:
            int(number)
            game(int(number))
        except Exception as e:
            print('you input is wrong, pls input a number type')

play()



