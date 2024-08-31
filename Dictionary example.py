n=int(input("Enter the range : "))
d={}

for i in range(n):
    values=input("Enter key: ")
    keys=input("Enter values: ")
    d[values]=keys

print(d)
