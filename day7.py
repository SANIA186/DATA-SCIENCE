
#Encapsulation
# class Student:
#     def __init__(self,marks):
#         self.marks= marks
#     def show_marks(self):
#         return self.marks
# s1=Student(80)
# print(s1.show_marks())



#polymorphism


# class TV:
#     def play(self):
#         print("Playing on TV")
# class Mobile:
#     def play(self):
#         print("Playing on Mobile")
# class Tablet:
#     def play(self):
#         print("Playing on Tablet")

# t=TV()
# m= Mobile()
# ta =Tablet()

# t.play()
# m.play()
# ta.play()


# a = int(input("Enter a Numerator"))
# b= int(input("Enter  a Denominator"))

# try:
#     print(a//b)

# except:
#     print("Can't divide by 0")

# print("sania")


# a = int(input("Enter a Numerator"))
# b= int(input("Enter  a Denominator"))

# try:
#     print(a//b)

# except Exception as e:
#     print("Can't divide by 0",e)

# print("sania")




# try:
#     a = int(input("Enter a Numerator"))
#     b= int(input("Enter  a Denominator"))
#     print(a//b)

# except ZeroDivisionError:
#     print("Can't divide by 0")

# except ValueError:
#     print("Enter correct type of value")

# except Exception:
#     pass

# print("sania")

# try:
#     a = int(input("Enter a Numerator"))
#     b= int(input("Enter  a Denominator"))
#     print(a//b)

# except ZeroDivisionError:
#     print("Can't divide by 0")

# except ValueError:
#     print("Enter correct type of value")

# except Exception:
#     pass
# finally:
#     print("PROGRAM ENDS")


# class Acc:
#     a=10
#     _b=20
#     __c=30
#     print (__c)
# class oft(Acc):
#     pass
   
# class c:
#     def z(self):
#         print(self._b)

# obj =Acc
# # obj=c()
# print(obj.a)
# print(obj._b)
# # print(obj._b)


#lamda fn: lamba is keyword
# add= lambda a,b : a+b
# print(add(110,20))

# add= lambda a,b : "Hi" if a+b> 100 else "bye"
# print(add(110,20))

# isEven = lambda a: "Even" if a%2==0 else "Odd"
# print(isEven(4))


# num= [1,2,3,4,5,6,11]
# add = list(filter(lambda a: a%2==0, num))
# print(add)

# num= [8,1,2,3,4,5,6,11]
# add = list(sorted(lambda a: a%2==0, num))
# print(add)
# print(sorted(num))

#============LIBRARIES===========#

# import numpy as np
# arr = np.array([10,20,30])
# print(arr)

# # import numpy as np
# # arr = np.zeros([1,2,3])
# # print(arr)

# z=np.zeros(5)
# print(z)

# z=np.ones(5)
# print(z)

# ar = np.arange(1,10,2)
# print(ar)

# ar=np.asarray([1,2,3,4,5])
# print(ar)