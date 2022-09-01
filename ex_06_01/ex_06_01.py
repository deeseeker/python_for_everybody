
#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything
# other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.


smallest = None
largest = None

while True:
    num = input('Enter a number: ')

    try:
        if num == 'done':
            break

        val = float(num)
        print(val)
        if smallest is None or largest is None:
            smallest = val
            largest = val
        if val > largest :
            largest = val

        if val < smallest:
            smallest = val



#
    except:
        print('Invalid number')

print('done')
print(largest,smallest)
