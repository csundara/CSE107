def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

#num = int(input('Please enter an integer '))
num = input('Please enter an integer ')

while int(num) != 0:
    if num.isdigit() == False:
        num = input('Please enter an integer ')
    else:
        if is_even(int(num)) == True:
            print(num + " is an even number")
        else:
            print(num + " is an odd number")
        num = input('Please enter an integer ')
