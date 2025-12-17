# class person:
#     x=10
#     y=10
#     tup=(1,2,3)
#     c=[5,6,7]
#     d={100,300,500}

#     def func(self):
#         print("this is my class function")
     

# #p1 is a object, person is  a class
# p1=person()
# p1.func()
# print(p1.x)
# print(p1.y)
# print(p1.tup)
# print(p1.c)
# print(p1.d)



# class Engine5kcc:
#     def Onroad(self,kmhr):
#         print(kmhr,"km/hr")

# bmw = Engine5kcc()
# audi =Engine5kcc()
# ferrari = Engine5kcc()

# bmw.Onroad(500)
# audi.Onroad(600)
# ferrari.Onroad(700)



# class Engine5kcc:
#     def __init__(self,kmph,limit):
#         # print("This is my Constructor",kmph)
#         self.a= kmph
#         self.limit=limit

#     def Onroad(self,weight):
#         print(self.a-weight)

#         print("Limit is :", self.limit)
    


# bmw = Engine5kcc(250,500)
# audi =Engine5kcc(600,500)
# ferrari = Engine5kcc(500,500)

# bmw.Onroad(50)
# audi.Onroad(60)
# ferrari.Onroad(70)


# class Calculator():
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# cal =Calculator()
# print(cal.add(10,20))
# print(cal.sub(10,20))
# print(cal.mul(10,20))
# print(cal.div(10,20))


# class Student:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age2

#     def display(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)

# a= Student("sania",20)
# a.display()


# class math:
#     formula ="(a+b)^2"

# class chemistry(math):
#         pass

# obj=chemistry()
# print(obj.formula)



# class math:
#     formula ="(a+b)^2"

# class chemistry(math):
#         x=10
# class biology(math):
#       pass

# obj=biology()
# print(obj.formula)
# print(obj.x)


# class math:
#     formula ="(a+b)^2"
#     a="b=c"

# class chemistry(math):
#         x=10
# class biology(math):
#       pass

# obj=biology()
# print(obj.formula)
# obj2= chemistry()
# print(obj2.a)
# print(obj2.formula)



# class math:
#     formula ="(a+b)^2"
   

# class chemistry:
#         x=10
# class biology(math,chemistry):
#       pass

# obj=biology()
# print(obj.formula)
# print(obj.x)


class xyz:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b

class abc(xyz):
#    def __init__(self, a, b):
#        xyz.__init__(self,a, b)
   def fun(self):
       print("this is fn")
   
    
a = abc(10,20)
print(a.add())
a.fun()


