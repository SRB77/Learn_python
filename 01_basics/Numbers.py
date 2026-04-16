import datetime

"""
num1 = 2
num2 = 3
num3 = 4
print(num1+num2)
print(num2**num3)

x = "chai"
y = "code"
print(x+y) #Operator Overloading 

print(num1 , num2 , num3)

print(num1 ** 100)
"""

#! Operator Overloading example 
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # For pretty printing
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(4, 4)
v2 = Vector(6, 3)

# This uses the __add__ method we defined!
v3 = v1 + v2

print(v3)  # Output: Vector(3, 7)
""" 

# site1 = site2 = "cavite.in"
# print(site1)
# print(site2)


# result = 1 / 3.0
# print(result , type(result))

# print("Hello")
# hii = repr("Hello")
# hiiii=str("Hello")
# print(hii)
# print(hiiii)

# s = 'Hello, Geeks.'
# print (type(str(s)))
# print (type(str(2.0/11.0)))
# print(type(str(30.4)) , type(str(46)) , type(str(True)))
# print((repr(30.4)) , (repr(46)) , (repr(True)))
# print((str(30.4)) , (str(46)) , (str(True)))
# In the above case both repr and str are converting any given obj into string and representing in 2 differnt format


# print (repr(5))
# print("5")


#! Let's understand the "Print()"

"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
1. this objects parameter is the obj we will provide to print 
2. te sep parameter is says we can print multiple obj by separating with space(which is default) , but we can use comma and hypen  or any other delimeters 
3. 
"""

# print("35")
# print(str("Hello"))
# print(str("35"))

# name = "chai"
# print(str(name))
# print(repr(name))

# now = datetime.datetime.now()
# print(str(now))
# print(repr(now))

# with open ("file.txt","w")as f1:
#     print("Hello world" , file=f1)

# print("Hello world welcome to NVIM buddy !")


