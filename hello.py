print("hello world") # printing hello world to the console
# variabes

name="vikash"
age=22
class_=14
print("my name is",name,"my age is",age,"and i am in class",class_)
# data types
name="vikash" # string
age=22 # integer    
height=5.11 # float
is_student=True # boolean
print("name:",name,type(name))
print("age:",age,type(age))
print("height:",height,type(height))
print("is_student:",is_student,type(is_student))
# operators
a=10    
b=5
# arithmetic operators
print("a + b =", a + b)  # addition
print("a - b =", a - b)  # subtraction
print("a * b =", a * b)  # multiplication
print("a / b =", a / b)  # division
print("a % b =", a % b)  # modulus
print("a ** b =", a ** b)  # exponentiation
print("a // b =", a // b)  # floor division
a += 2
print ("a+=2","a=a+2",a)
# comments


# This is a single-line comment
""" This is a multi-line comment
   that spans multiple lines"""
''' This is another multi-line comment
   that also spans multiple lines  '''

# inpython we use snake_case for variable names
first_name="vikash"
last_name="kumar"
full_name=first_name+" "+last_name
print("full name:",full_name)


#logical perators ate of three types and, or, not
x = True
y = False  
print("x and y:", x and y)  # False
print("x or y:", x or y)   # True   
print("not x:", not x)    # False
print("not y:", not y)    # True    

#predecence of operators
# Parentheses () have the highest precedence
# Exponentiation ** comes next
# Multiplication *, Division /, Floor Division //, and Modulus % have the same precedence
# Addition + and Subtraction - have the lowest precedence
#==, !=, >, <, >=, <= have lower precedence than arithmetic operators
#not has lower precedence than and, or  
result = 3 + 4 * 2 / (1 - 5) ** 2
print("result:", result)  # Output: 3.5 

#type conversion 

#type conversion is the process of converting one data type to another. In Python, we can use built-in functions to perform type conversion.
# converting integer to float
num1 = 10   
num2 = float(num1)
print("num1:", num1, type(num1))  # Output: 10 <class 'int'>
print("num2:", num2, type(num2))  # Output: 10.0 <class 'float'>
# converting float to integer
num3 = 5.75     
num4 = int(num3)
print("num3:", num3, type(num3))  # Output: 5.75 <class 'float'>
print("num4:", num4, type(num4))  # Output: 5 <class 'int'>
# converting string to integer
num5 = "20"
num6 = int(num5)
print("num5:", num5, type(num5))  # Output: "20" <class 'str'>
print("num6:", num6, type(num6))  # Output: 20 <class 'int'>
# converting string to float
num7 = "3.14"
num8 = float(num7)
print("num7:", num7, type(num7))  # Output: "3.14" <class 'str'>
print("num8:", num8, type(num8))  # Output: 3.14 <class 'float'>
# converting integer to string
num9 = 42
num10 = str(num9)
print("num9:", num9, type(num9))  # Output: 42 <class 'int'>
print("num10:", num10, type(num10))  # Output: "42" <class 'str'>


