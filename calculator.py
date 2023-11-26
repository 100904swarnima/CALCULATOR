a=int(input("enter the number \n"))
b=int(input("enter the number \n"))
ch=input("enter the choice\n")
if ch == '+':
    print(a+b)
elif ch == '-':
    print(a-b)
elif ch == '*':
    print(a*b)
elif ch == '%':
    print(a%b)
elif ch == '/':
    print(a/b)
else:
    print("Wrong choice")
