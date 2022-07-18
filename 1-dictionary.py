#!/usr/bin/python3
def roman_int(roman_number):
	roman_numbers = { "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000 }
	int_number = 0
	i = 0
	while i < len(roman_number):
		if roman_number[i:i+2] in roman_numbers:
			int_number+=roman_numbers[roman_number[i:i+2]]
			i+=2
		else:
			int_number+=roman_numbers[roman_number[i]]
			i+=1
	return int_number
print(f"roman III equals {roman_int('III')}")
print(f"roman LVIII equals {roman_int('LVIII')}")
print(f"roman MCMXCIV equals {roman_int('MCMXCIV')}")
print(f"roman XCIX equals {roman_int('XCIX')}")
print(f"roman MMDCCCL equals {roman_int('MMDCCCL')}")
