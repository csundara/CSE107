sum = 0
avg = 0

for i in range(1, 10):
    num = input('Please enter an integer: ')
    num = float(num)

	sum = sum + num
    avg = sum/i

    print(avg)
