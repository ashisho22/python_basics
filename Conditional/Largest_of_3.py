Num1 = int(input("Write first number = "))
Num2 = int(input("Write second number = "))
Num3 = int(input("Write third number = "))

if Num1 >= Num2 and Num1 >= Num3:
    print(f"{Num1} is the largest number")
elif Num2 >= Num1 and Num2 >= Num3:
    print(f"{Num2} is the largest number")
else:
    print(f"{Num3} is the largest number")
