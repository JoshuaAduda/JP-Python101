# This is a singleline coment

# name = "Jonh Doe" #this is a variable
# firstName = input() #standard input
# secondName = input("Enter second name: ")

"""
Multi-line coment or string
"""
output=""
# print("===================")
# print(secondName) # standard output
# print("===================")





"""
DATA TYPE:
 -TEXT(strings) type: str
 -NUMBERS(integers,float, complex)
 -LISTS(list, tuple, dictionary, sets)
"""

#Numbers: INT > int()
number =10 #integer value or 10
output = number
output = type(number)
number=100000000000
output=number

# #Numbers: FLOAT ->float()
# amount =200.5
# output = root
# output = type(root)

#Text: STRINGS -> str()
name = "John Doe"
name = 'John Doe'
welcomeMessage = "It's a sunny morning"


#string is a list of characters 
name = "Peter Parker"
output = name [4] 

#slicing 
output  = name [1:12]
output  = name [1:6:2]
output  = name.upper()
output  = name.lower()
output  = name.startswith("b")
output  = name.split(" ")
output = name
output  = name.replace("e", "u")
output  = name.replace("u", "e")
output  = name.replace("Peter", "Jane")


#operators and operands

"""
-Arithmetic operators
addition (+)
Subtraction(-)
Multiplication(*)
power(**)
division(/)
floor division (//)
modulus (%)
-boolean operators(and. or, not)
-bitwise operator
-assignment operators
-comparison operators
-membership operator

"""
numberOne = 10
numberTwo = 20 
#addition (+)
output = numberOne + numberTwo
#Subtraction(-)
output = numberOne - numberTwo
#Multiplication(*)
output = numberOne * numberTwo
#division(/)
output = numberOne / numberTwo
#floor division (//)
output = numberOne // numberTwo #TRUNCATION
#modulus (%)
output = numberOne % numberTwo #remeinder

#operation = input("Enter math operation: ")
#output = eval(operation)

#Comparison operator(>, >=, <, <=, ==, !=)
x=10
y=20
output =(x<y) # less than(<)
output =(x>y) # greater than(>)
output =(x>=y) # greater than or equal to(>=)
output =(x<=y) # less than or equal to(<=)
output =(x==y) # equality(==)
output =(x!=y) # not equal to(!=)


#LOGIC OPERATORS (and, or, not)
age = 17
year = 2026

output = ((2027>= year) and (age<= 18))
output = ((2027> year) or (age == 18))

output = not ((2027>= year) and (age<= 18))
output = not ((2027>= year) or (age<= 18))

#Assignement operators
i=0
# x = x+y
x +=y
# i = i+1
i +=1
i -=1
i *=5
i /=3
i //=1
i %=20
output = i


"""
CONDITIONAL STATEMENTS
-if...else
-if...elif...else
-match
"""

age=18
if age > 18 :  
    output ="Able to vote"
else :
    output = "Oops! cannot vote!"    

clothing = "t-shirt"
color = "green"

if (clothing == "t-shirt") and (color) :
    output = "Buy the t-shirt"
else :
    output = "Do not buy"

clothing = "pants"
color ="black"
shoes ="white"
socks = "happy-socks"

if (clothing == "pants") and (color == "green") :
    output = "green is good but we will back for the cold!"
elif (clothing == "pants") and (shoes == "brown") :
    output = "The brown shoes are not part of the weddding theme"
elif (clothing == "pants") and socks.startswith("official") :
    output = "This is a good start"
elif (clothing == "pants") and socks.startswith("happy") and (color == "black") :
    output = "you nailed it!!"
else :
    output = "Oii! we are done "
    
    #ternary operator
    output = "ten" if (x==10) else "not ten" 

#match
color = "mygenta"
match (color):
    case "green":
        output = "green light!"
    case "yellow":
        output = "get ready!"
    case "blue":
        output = "Line to swim"
    case _:
        output = "I'm color blind"

    
start = 0
end =10

# while(start<=end ):
#     print("=> ",start)
#     start +=1


# print("=======================")
# while(start<=end ):
#     print("=> ",start)
#     start +=1
#     if start == 3:
#         break

# print("=======================")

print("=======================")
while(start<=end ):
    print("=> ",start)
    if start == 3:
        break
    start +=1 
print("=======================")

name = " Peter Parker"

for i in name:
    if (i == "r"):
        continue #skip 
    #print(i)

for num in range



# print("=======================")
# print(output) # standard output
# print("=======================")