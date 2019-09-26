number=int(input("Enter any decimal number:"))

if number<0:
    print("Number is negative")

    quit()

else:
    print("Equivalent binary number",bin(number))
    binary=bin(number)

    decimal=int(binary,2)
    print(binary,"in Decimal is",number)