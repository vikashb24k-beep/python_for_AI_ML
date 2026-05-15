# ## oops 

# # creating a class
# class Student:
#     # print("self started")
#     def __init__ (self,subject,college,sem):
#         print("constructor called")
#         self.subject=subject
#         self.college=college
#         self.sem=sem
# std1=Student("java","iiit",3)
# std2=Student("python","iiit",4)


# # print(std1.subject)


# #CAR

# class Car:
#     name="maruti"
#     year=2000
#     model=400

# c1=Car()
# print(c1.__dict__)


# Car by constructor

class Car:
    @staticmethod
    def start():
        print("start")
    @staticmethod
    def stop():
        print("stop")
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year

class Tata(Car):
    @staticmethod
    def f1():
        print("fly")
    @staticmethod
    def f2():
        print("feature 2")
    def __init__(self,model1,year1,name,model,year):
        super().__init__(self,name,model,year)
        self.model1=model1
        self.year1=year1

    def mode(self):
        return self.model1
    

#object

tata1=Tata(400,2000)
car1=Car('sumo',500,2005,)

tata1.start()
print(tata1.mode())




# Student class 

class Student:
    sch_name="SVM"   #class attribute
    def __init__(self,name,roll_no,marks):
        self.name=name   #instance attributes (for object)
        self.roll_no=roll_no #instance attributes (for object)
        self.marks=marks    #instance attributes (for object)

s1=Student("vikash",162,87)
s2=Student("Raman",115,98)
s3=Student("Nikhil",86,95)

print(s1.sch_name)   # --> class variable is access by both class and object
print(Student.sch_name)  # --> class variable is access by both class and object
 