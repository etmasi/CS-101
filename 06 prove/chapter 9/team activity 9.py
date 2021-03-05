print("enter a list of  numbers and type 0 when finished")
number = []
number = -1

while num != 0:
    num = int (input (F'enter number'))
    if num != 0 :
        number.append(num)
        total = 0
    for num in numbers:
            total = 0 

        for num in numbers:
            total += num

    average = total/len (numbers)
    sorted_list = sorted (numbers)


    print(f'The Total is: {total}')
    print(f'the everage is:{average:.2f}')
    print(f'max value in list:', max(numbers))
    print(sorted_list)
    