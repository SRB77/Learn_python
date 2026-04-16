 # ! Operators in python 
#* 1. Arithmatic Operator 
num1 = 23 
num2 = 65

# Adding 2 variable and 2 values
num3 = num1 + num2   #> This is the Addition Operator
print(num3)

num4 = num1 - num2  #> This is the subtraction Operator 
num5 = num2- num1
print (num4 , num5)

numa = 45 
numb = 56 
print(numa * numb) #> This is the Multiplication operator 


numc = numa / numb #> This is the Division Operator helps to devide 
print(numc)

numd = numa // numb #> This is floor division, This also helps to divide 

#* Difference between Division and Floor Division 
# print(24//12) and print(24/12) This is where differnce lies 
#? Normal Division / True Division (/): 
# It simply calculate as per the normal division with proper floating points always even it's divide completely or some decimal exist 
#> example : 10/2 >output: 2.0 , 34/3 >output: 11.333..  we can compare these 2 

#? Floor Division / Integer Division (//): 
# It always calculate given operand and then simply try to floor the value and return a whole number at any point 
#> example : 15//4 >output: 3 if we do 15/4 = 3.75 it simply floor it to 3
#! Important point to understand 
# if any of the operand is in float it will return flot (23.5//4 or 34//4.5) .  and it try to floor towards negative infinity so for negative numbers (-34 //4) actual division will be -8.5 and it will floor it to -9

number1 = -39 #?There is a point if i am putting negative number it's behaving something differnt like 39%5 comes 4 so -39%5 should come -4 but it's 1
number2 = 5 
print(number1%number2) #>It simply perform division and return the remainder

# ? How NEGATIVE number act in a modulo 
# It simply because the python floor down towards the negative infinity and for modulo it's uses the floor division and also a formula .
# > Formula is if a % n 
#* a - (n * floor(a/n)) 

#>  let's take the example of 39%5 and -39%5
"""
1>  39 % 5 
    as per the formula : 39 - (5 * floor(39/5))
    39 - (5 * floor(7.8))
    39 - (5 * 7)
    39 - 35 = 4 
2>  -39 % 5 
    as per the formula : 39 - (5 * floor(-39/5))
    39 - (5 * floor(-7.8))
    39 - (5 * (-8))
    39 - (-40)
    1
    That's why this rather than -4 we get only 1 
"""

#! Power Operator (**)
print(45 ** 56 )
# one basic example 
print(2**3) #> Output 8 we all know 


#* Assignment Operators 
""" 

=	Assignment Operator	a = 7
+=	Addition Assignment	a += 1 # a = a + 1
-=	Subtraction Assignment	a -= 3 # a = a - 3
*=	Multiplication Assignment	a *= 4 # a = a * 4
/=	Division Assignment	a /= 3 # a = a / 3
%=	Remainder Assignment	a %= 10 # a = a % 10
**=	Exponent Assignment	a **= 10 # a = a ** 10

"""

# https://www.programiz.com/python-programming/operators

# ! Other important Dattypes are here go and learn as per the need