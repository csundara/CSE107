def collatz_len(n):
    len_count = 1
    while n != 1:
        len_count = len_count + 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
    return len_count

def main():
    num = int(input('Enter a starting number: '))
    if str(num).isdigit() == False:
        print("Invalid entry")
        exit()
    else:
        len = collatz_len(num)
        print("Length of Collatz sequence: {}".format(len))

if __name__ == "__main__":
    main()
