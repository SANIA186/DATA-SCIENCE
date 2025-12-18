
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

try:
    a = int(input("Enter a Numerator"))
    b= int(input("Enter  a Denominator"))
    print(a//b)

except ZeroDivisionError:
    print("Can't divide by 0")

except ValueError:
    print("Enter correct type of value")

except Exception:
    pass
finally:
    print("PROGRAM ENDS")


