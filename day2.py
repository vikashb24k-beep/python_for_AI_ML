# # #conditional statements if, else, elif and nested if and match case statements


# # # age=18
# # # if age>=15:
# # #     print ("you can give boarding pass")

# # # #outhentication system
# # # username=input("enter your username:")
# # # password=input("enter your password:")
# # # if username=="admin" and password=="1234":
# # #     print("welcome admin!")
# # # else:
# # #     print("invalid username or password.")

# # # #odd or even
# # # num=int(input("enter a number:"))
# # # if num%2==0:
# # #     print(num,"is an even number.")
# # # else:
# # #     print(num,"is an odd number.")


# # ##match case statements
# # # color=input("enter a color:")
# # # match color:
# # #     case "green":
# # #         print("go")
# # #     case "red":
# # #         print("stop")
# # #     case "yellow":
# # #         print("wait")


# # #while loop
# # i=1
# # while(i<=5):
# #     print("vikash")
# #     i+=1


# count=5
# while(count>=1):
#     print(count)
#     count-=1

# multiplication of 6

# count=1
# while(count<=10):
#     print("6 x",count,"=",6*count)
#     count+=1


# use of continue and break keyword
# skip no 5
# i=1
# while(i<=10):
#     if(i==5):
#         i+=1
#         continue
#     print(i)
#     i+=1

# brak loop at i=5

i = 1
# while i <= 10:
#     if i == 5:
#         i += 1
#         break
#     print(i)
#     i += 1


# for loop

# for as a
# var="vicky"
# for i in var:
#     print(i)


# for as a sequence

# for i in range(1,11):
#     if(i%2==0):
#         print (i)


# cnt=0
# var="artificial inteligence"
# for i in var:
#     if(i=="0"):
#         cnt+=1

# print("no of i in artificial inteligence is :",cnt)

# vowel count
# cnt=0
# var="vikash"
# for i in var:
#     if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         cnt+=1
# print(cnt)


# print sum of first n natural number


# sum=0
# num=int(input("enter num:"))
# for i in range(1,num+1):
#     sum=sum+i
# print ("sum is :" , sum)


# function
# num=int(input("enter the year :"))
# def leap_year(n):
#     if(n%4==0 & n%100!=0) or (n%400==0):
#         print ("leap year")
#     else: print("not leap year")

# leap_year(num)
# leap year is a year that is divisible by 4 but not divisible by 100, or it is divisible by 400. This means that if a year is divisible by 4 and not divisible by 100, it is a leap year. However, if a year is divisible by 100, it must also be divisible by 400 to be considered a leap year. For example, the year 2000 is a leap year because it is divisible by 400, while the year 1900 is not a leap year because it is divisible by 100 but not by 400.


# Average of 3 nums

# def avg(a,b,c):
#     sum=a+b+c
#     return sum/3
# print(avg(1, 14, 0))


#lembda function

# sum=lambda a,b:a+b
# print(sum(1,2))


# avg=lambda a,b,c:(a+b+c)/3
# print(avg(2,3,9))

#  factorial of n??

pro=1
n=int(input("enter n :"))
for i in range(1,n+1):
    pro=pro*i
    i+=1
print("factorial of n is :",pro)