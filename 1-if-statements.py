#!/usr/bin/python3
m = int(input().strip())

if m % 2 == 0:
    print("Weird")
else:
    if m >= 2 and m <= 5:
        print("Not Weird")
    elif m >= 6 and m <= 20:
        print("Weird")
    elif m > 20:
        print("Not Weird")
