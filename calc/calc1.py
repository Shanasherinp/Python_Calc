def add(num1,num2):
    result = num1+num2
    print(result)
def sub(num1,num2):
    result = num1-num2
    print(result)
def mult(num1,num2):
    result = num1*num2
    print(result)
def div(num1,num2):
    result = num1/num2
    print(result)
    

choice = input("enter your operator: +,-,*,/")
firstnum = int(input("enter your first num"))
secondnum = int(input("enter your second num"))

if choice == "+":
    add(firstnum, secondnum)
if choice == "-":
    sub(firstnum, secondnum)
if choice == "*":
    mult(firstnum, secondnum)
if choice == "/":
    div(firstnum, secondnum)




