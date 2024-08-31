a=input('Enter 1st number:')
o=input('Select an operator(+,-,*,/,%):')
b=input('Enter 2nd number:')
if o=="+":
    print(int(a) + int(b))
elif o=="-":
    print(int(a) - int(b))
elif o=="*":
    print(int(a) * int(b))
elif o=="/":
    print(int(a) / int(b))
elif o=="%":
    print(int(a) % int(b))
else:
    print("Operator not found")