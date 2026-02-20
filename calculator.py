#my approach
a = input("Enter first number: ")
s= input(
"""
Input one of the following :
(+)-addition
(-)-subtraction
(*)-multiplication
(/)-division
(**)-power
(//)-truncate

"""
)
b = input("Enter second number: ")
a = int(a)
b = int(b)
if s == "+":
    print (a+b)
elif s == "-":
    print (a-b)
elif s == "*":
    print (a*b)
elif s == "/":
    print (a/b)
elif s == "**":
    print (a**b)
elif  s == "//":
    print (a//b)
else :
    print("syntax error")


#teacher's approach

"""
-Input value 1
-select operator (+,-,*,/,//,**)
-input value 2
-perform calculation
-print result
"""
valueOne = input("Enter the first operand: ")
valueTwo = input("Enter the second operand: ")
operatorChoice = input(
"""
Kindly input the operation you want:
1. addition (+)
2. subtraction(-)
3. multiplication(*)
4. division (/)
5.power(**)
6. floor division(division without decimals //)
:
"""
)

output ="" 
operatorChoice = int(operatorChoice)
valueOne = int(valueOne)
valueTwo = int(valueTwo)
if(operatorChoice == 1):
    output = valueOne + valueTwo
elif(operatorChoice == 2):
    output = valueOne - valueTwo
elif(operatorChoice == 3):
    output = valueOne * valueTwo
elif(operatorChoice == 4):
    output = valueOne / valueTwo
elif(operatorChoice == 5):
    output = valueOne ** valueTwo
elif(operatorChoice == 6):
    output = valueOne // valueTwo
else:
    output = "wrong selection"


match(operatorChoice)
    case 1:
        output = valueOne + valueTwo
    case 2:
        output = valueOne - valueTwo
    case 3:
        output = valueOne * valueTwo
    case 4:
        output = valueOne / valueTwo
    case 5:
        output = valueOne ** valueTwo
    case 6:
        output = valueOne // valueTwo
    case_:
        output = "wrong selection"



print("***************************")
print(output)
print("***************************")
print("========================================================")