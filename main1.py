def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

def calc():
    while True:
        num1=float(input("Enter the First Number:"))
        num2=float(input("Enter the Second Number:"))
        select=input("Select (+,-,*,/):")

        if select=="+":
            print("Result:",add(num1,num2))
        elif select=="-":
            print("Result:",sub(num1,num2))
        
        elif select=="*":
            print("Result:",multi(num1,num2))
        elif select=="/":
            print("Result:",div(num1,num2))
        else:
            print("Error Occured")
calc()
