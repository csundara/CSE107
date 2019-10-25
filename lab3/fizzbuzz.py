

def main():
    num = int(input("Enter a number: "))
    if num < 0:
        print('Not a positive number!')
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('{} FizzBuzz'.format(i))
        elif i % 5 == 0:
            print('{} Buzz'.format(i))
        elif i % 3 == 0:
            print('{} Fizz'.format(i))
        else:
            print('{}'.format(i))

if __name__ == "__main__":
    main()
