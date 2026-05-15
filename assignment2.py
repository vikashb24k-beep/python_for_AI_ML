#Write aprogram that takes as input.Using conditional statements,calculate the based on these rules: 
# Q1 salaryfinaltaxrate•Ifsalary<30,000→5%•Ifsalaryis30,000–70,000→15%•Ifsalary>70,000→25%

# salary=float(input("Enter the salary"))
# if(salary<30000):
#     tax_rate=0.05
# elif(30000<=salary<=70000):
#     tax_rate=0.15
# elif(salary>70000):
#     tax_rate=0.25

# tax=salary*tax_rate
# print(f"the tax rate is { tax_rate*100}% and tax amount is { tax}")

#q2
# for i in range(1,10):
#     if(i%2==0):
#         print(i)

#q3

# n = int(input("Enter the number: "))

# while num > 0:
#     print(num % 10)   # last digit
#     num = num // 10   # remove last digit


#q4
# n = int(input("Enter the number: "))
# def count(num):
#     c=0
#     while num>0:
#         c+=1
#         num=num//10
#     print("total number of digits are ",c)
# count(n)

#q5

# def sum(num):
#     s=0
#     while num>0:
#         s+=num%10
#         num//=10
#     print("the sum is ",s)

# sum(n)

#q6 
# for i in range(1,100):
#     if(i%3==0 and i%5==0):
#         print(i)


#q7

# while True:
#     num=(input("Enter the no: "))
#     if(num=="quite"):
#         print("stop")
#         break
#     n=int(num)
#     print("positive") if(n>0) else print("negative")

# def calculator(a, b, op):
#     if(op=='+'):
#         return a+b
#     elif(op=='-'):
#         return a-b
#     elif(op=='*'):
#         return a*b
#     elif(op=='/'):
#         return a/b
#     elif(op=='//'):
#         return a//b

# a=int(input("enter a: " ))
# b=int(input("enter b: " ))
# op=input("enter operator")
# print(calculator(a,b,op))

#q9
def prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True 