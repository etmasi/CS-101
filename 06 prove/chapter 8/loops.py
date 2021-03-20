user = int(input(f'How many colums and row do you want in your multiplication table?'))
number = user + 1
for  val_1 in range(1,number):
    for val_2 in range(1,number):
        print('{:3}'.format(val_1 * val_2),end='')
        print()