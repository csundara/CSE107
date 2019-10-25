def main():
    mile = float(input("Please enter the mile/hr: "))
    km = transkm2mile(mile)

    if km > 110:
        print('Over Speed')
    else:
        print('Safe')

def transkm2mile(mile):
    print(mile * 1.6)
    return mile * 1.6

def avg(n1, n2, n3):
    print((n1 + n2 + n3)/3)




print('End Program')
