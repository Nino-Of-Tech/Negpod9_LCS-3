#!/usr/bin/python3
Months1 = ['January', 'March', 'May', 'July', 'August', 'October', 'November']
Months2 = ['February']
Months3 = ['April', 'June',  'September', 'December']
Month = ""
while(Month == "" ):
    Month = input("Enter the month: ")
    if Month in Months1:
        print(f"The month of {Month} has 31 days.")
        break
    if Month in Months3:
        print(f"The month of {Month} has 30 days.")
        break
    if Month in Months2:
        print(f"The month of {Month} has 28 days.")
        break
    print("Input incorrect")
    Month = ""
