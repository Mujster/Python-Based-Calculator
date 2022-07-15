print("\tWelcome To Python Based Calculator\n")
num=input("\tEnter Your 1st Number\n")
num2=input("\tEnter Your 2nd Number\n")
operand=input("\tEnter Your Operand(+,*,-,/,=,%):\n")
if operand=='+':
    print("The Addition of",num,"+",num2,":",int(num)+int(num2))
elif operand=='*':
    print("The Product of", num, "*", num2, ":", int(num) * int(num2))
elif operand=='-':
    print("The Subtraction of", num, "-", num2, ":", int(num) - int(num2))
elif operand=='/':
    print("The Division of", num, "/", num2, ":", int(num) / int(num2))
elif operand=='%':
    print("The Modulus of", num, "%", num2, ":", int(num) % int(num2))
elif operand=='=':
    if num==num2:
        print("Both Numbers Are Equal\n")
    else:
        print("Both Numbers Are Not Equal\n")
else:
    print("No Such Operand Exists\n")
