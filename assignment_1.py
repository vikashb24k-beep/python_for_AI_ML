# question 1:>>>>>>>>>>>>>>>>>>>>>
name=input("enter your name:")
age=input("enter your age:")
print("Hello",name,"you are",age,"years old.")
# question 2:>>>>>>>>>>>>>>>>>>>>>
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
sum=num1+num2
diff=num1-num2
pro=num1*num2
div=num1/num2

print("the sum of",num1,"and",num2,"is",sum)
print("the difference of",num1,"and",num2,"is",diff)
print("the product of",num1,"and",num2,"is",pro)
print("the division of",num1,"by",num2,"is",div)
# question 3:>>>>>Asktheusertoentertwointegersandonefloat.Convertthemalltofloatsandprinttheiraverage.
num1=float(input("enter first integer:"))
num2=int(input("enter second integer:"))
num3=int(input("enter a float:"))
avg=(num1+float(num2)+float(num3))/3
print("the average of",num1,num2,"and",num3,"is",avg)

# question 4:>>>>
num=input("enter a number:")
num_1=int(num)
num_2=float(num_1)
num_3=str(num_2)
print(num_1,type(num_1),num_2,type(num_2),num_3,type(num_3))

# question 5:>>>>>>>>
x=10+3*2**2
print("the result of the expression is:",x) #first 2**2 is evaluated to 4, then 3*4 is evaluated to 12, and finally 10+12 is evaluated to 22.   

# question 6:>>>>>>>> swap the values of two variables without using a temporary variable

num_a=int(input("enter first number:"))
num_b=int(input("enter second number:"))
print("before swapping: num_a =",num_a,"num_b =",num_b)
temp=num_a
num_a=num_b
num_b=temp
print("after swapping: num_a =",num_a,"num_b =",num_b)  


# question 7:>>>>>>>>>>>
celcius = int(input("enter temperature in celcius:"))
calcius=float(celcius)
flahrenheit=(calcius*9/5)+32
print("the temperature in flahrenheit is:",flahrenheit) 
 
 
 
#question 8:>>>>>>>>>>>
radius = float(input("enter the radius of the circle:"))
area = 3.14 * radius ** 2
print("the area of the circle is:",area)


#question 9:>>>>>>>>>>>
p=float(input("enter the principal amount:"))
r=float(input("enter the rate of interest:"))
t=float(input("enter the time in years:"))
simple_interest=(p*r*t)/100 
print("the simple interest is:",simple_interest)
amount=p+simple_interest
print("the total amount after",t,"years is:",amount)    


#question 10:>>>>>>>>>>>
dec=float(input("enter a decimal number:")) #45.78
int_part=int(dec) #45   
frac_part=dec-int_part #0.78
print("the integer part is:",int_part)      
print("the fractional part is:",frac_part)


