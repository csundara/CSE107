def transkm2mile(mile):
    print(mile * 1.6)
    return mile * 1.6




mile = float(input("Please enter the mile/hr: "))
km = transkm2mile(mile)

if km > 110:
    print('Over Speed')
else:
    print('Safe')
print('End Program')
