import math as m

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b
def Square_root(a):
    return m.sqrt(a)
def exponent(a,b):
    return(a**b)
def sine(a):
    return m.sin(a)
def cos(a):
    return(m.cos(a))
def tan(a):
    return(m.tan(a))
def radians(a): # Degrees to radians
    return(m.radians(a))
def degrees(a): # Radians to degree
    return(m.degrees(a))
print('''
1. Addition
2. Subtraction
3. Multiply
4. Division
5. Modulus
6. SquareRoot
7. Exponent
8. Sine
9. Cosine
10. Tangent
11. Radians
12. Degrees''')

option=eval(input('What operation do you want to perform: '))

while option<=12:
    if option==1:
        print("---Addition---")
        num1=eval(input('Enter first no.: '))
        num2=eval(input('Enter Second no.: '))
        result=addition(num1,num2)
        print('The Addition of {} and {} is {}'.format(num1,num2,result))

    elif option==2:
        print("---Subtraction---")
        num1=eval(input('Enter first no.: '))
        num2=eval(input('Enter Second no.: '))
        result=subtraction(num1,num2)
        print('The Subtraction of {} and {} is {}'.format(num1,num2,result))

    elif option==3:
        print("---Multiply---")
        num1=eval(input('Enter first no.: '))
        num2=eval(input('Enter Second no.: '))
        result=multiply(num1,num2)
        print('The Multiplication of {} and {} is {}'.format(num1,num2,result))

    elif option==4:
        print("---Division---")
        num1=eval(input('Enter first no.: '))
        num2=eval(input('Enter Second no.: '))
        result=division(num1,num2)
        print('The Division of {} and {} is {}'.format(num1,num2,result))

    elif option==5:
        print("---Modulus---")
        num1=eval(input('Enter first no.: '))
        num2=eval(input('Enter Second no.: '))
        result=modulus(num1,num2)
        print('The Modulus of {} and {} is {}'.format(num1,num2,result))

    elif option==6:
        print("---Square Root---")
        num1=eval(input('Enter any no.: '))
        result=Square_root(num1)
        print('The Square Root of {} is {}'.format(num1,result))

    elif option==7:
        print("---Exponent---")
        num1=eval(input('Enter the number: '))
        num2=eval(input('Enter the number:'))
        result=exponent(num1,num2)
        print('The Exponent of {} and {} is {}'.format(num1,num2,result))

    elif option==8:
        print("---Sine---")
        num1=eval(input('Enter the value:'))
        result=sine(num1)
        print('The Sine of {} is {}'.format(num1,result))

    elif option==9:
        print("---Cosine---")
        num1=eval(input('Enter the value:'))
        result=cos(num1)
        print('The Cosine of {} is {}'.format(num1,result))

    elif option==10:
        print("---Tangent---")
        num1=eval(input('Enter the value:'))
        result=tan(num1)
        print('The Tanget of {} is {}'.format(num1,result))

    elif option==11:
        print("---Degrees to Radians---")
        num1=eval(input('Enter the value:'))
        result=radians(num1)
        print('The Radians of {} is {}'.format(num1,result))

    elif option==12:
        print("---Radians to Degrees---")
        num1=eval(input('Enter the value:'))
        result=degrees(num1)
        print('The degrees of {} is {}'.format(num1,result))

    else:
        print("Choose correct option")

    new_option=eval(input('Do you want to continue other operations(yes-1 or no-0):'))
    if new_option==1:
        option=eval(input("What operation do you perform?"))
    else:
        print("Thank You So Much..")
        break
