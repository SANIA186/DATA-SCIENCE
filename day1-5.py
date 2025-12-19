# # print ("hello")
# a= "Dace"
# print(type(a))
# b="Smith"
# print(f"My name is {b} and IM learning Python")
# print(a,end=" ")
# print(b)

# x=input()
# y=input()
# print(x+y)

# print(""" lorem20bhjhfherncfjnvjvnfvg
#       fvnfjvfvnfvjfvf
#       jfnfjfrdf """ )


# a = "10-23-89"
# b=a.split("-")
# print(b)


# a = int(input("Enter number: "))
# if a%2==0:
#     print("Even")
# else:
#     print("Odd")

# a=89
# b=76
# print(str(a)+str(b))


# s1=95
# s2=85
# s3=98
# avg=(s1+s2+s3)/3
# print("Average is ",avg)
# total=s1+s2+s3
# print("Total is ",total)
# percentage=(total/300)*100
# print("Percentage is ",percentage)
# if avg>=90:
#     print("Grade A")
# elif avg>=80:
#     print("Grade B")
# elif avg>=70:
#     print("Grade C")
# else:
#     print("Below C Grade")





# a=10
# b=20
# print(a&b)
# print(a|b)
# print(a^b)


# mark=int(input("Enter your mark: "))
# if mark>=90:
#     print("Grade A")
# elif mark>=80:
#     print("Grade B")
# elif mark>=70:
#     print("Grade C")
# else:
#     print("below 70")




# a=10
# b=20
# print("Before swapping: ",a,b)
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print("After swapping: ",a,b)


# marks=45
# a="pass" if marks>30 else "fail"
# print(a)

# marks=85
# a=("pass","fail" ) [marks<30]
# print(a)


# a=int(input("Enter a number: "))
# if a>0:
#     print("Positive")
# elif a<0:
#     print("Negative")
# else:
#     print("Zero")


# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# if a>=b and a>=c:
#     print(a,"is the largest")
# elif b>=a and b>=c:
#     print(b,"is the largest number")
# else:
#     print(c," is the largest number")


# for i in range(1,6,1):
#     print("sania")

# for i in range (10,1,-1):
#     print("hi",i)

# a="sania"
# for i in a:
#     print(i)


# a=["sania","farheen","safa","rumaiz"]
# for i in a:
#     print(i)


# sum =0
# for i in range (1,11):
#     sum+=i
# print(sum)


# a=(input("Enter a string: "))
# vowel=0
# consonant=0
# for i in a:
#     if i in "aeiouAEIOU":
#         vowel=vowel+1
#     else:
#         consonant=consonant+1
# print("Vowels:",vowel)
# print("Consonants:",consonant)
 

# a = int(input("Enter a number: "))
# for i in range (2,a):
#   if a%i==0:
#     print("Not a prime")
#     break
#   else:
#     print("prime")


# n=int(input("enter a input"))
# flag=1
# for i in range (2,n):
#   if (n%i==0):
#     flag=0
#     break
#   else:
#     flag=1
# a=("not prime","prime") [flag==1]
# print(a)




# a =int(input("Enter  a number"))
# fact=1
# for i in range(1,a+1):
#   fact =fact*i
# print("Factorial is ",fact)



# count=0
# for a in range (1,101):
#   if (a%3==0 or a%5==0):
#     count+=1
# print(count)
    
 
# def fun(a,b):
#   print(a+b)
# fun(10,20)  


# def multiply(a,b):
#   return a*b

# result=multiply(5,2)


# i=0
# while (i<=10):
#     print(i)
#     i+=1


# while True:
#     print("hello")


# mark=100
# while True:
#     if mark is 50:
#        print("fail",mark)
#        break
#     else:
#         print("hi",mark) 
#         mark-=10 


# for i in range (10):
#    if i == 5:
#       pass
#    print(i)
  
  
# for i in range (10):
#    if i == 5:
#       continue
#    print(i)
  

  
# for i in range (10):
#    if i == 5:
#       break
#    print(i)


# count=1
# for i in range (10):
    
#     for j in range (10):
#         print("hi",count)
#         count+=1

# for i in range (5):
#    for j in range (5):
#       print("#",end='')
#    print()
  

# t=(1,2,3,2,4)
# print(t.index(3))
# print(t.count(2))
# print(len(t))
# print(t*2)
# print(2 in t)x 
# print(5 not in t)
# print(t[0:2])
# l=list(t)
# print(l)
 
# t=(1,2,3)
# a,b,c=t
# print(a,b,c)


# s={"vikram",123,567,90.8}
# # for i in s:
# #     print(i)
# # s.remove("vikram")
# # print(s)
# # s.discard(89)
# # print(s)
# # s.clear()
# # print(s)


# s2={"vikram",123,567,90.8}
# s1={123,897,"sania"}
# s2.union(s1)
# s2.difference(s1)
# print(s2)


# s1={1,2,3,4}
# s2={3,5}
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))
# print(4 in s1)
# print(5 not in s2)
# print(list(s1)) 



# fs=frozenset([1,2,3 ])
# print(fs)

  
      
# l =[23,34,89,38]
# print(max(l))


# # l =[23,34,89,38]
# max = l[0]
# for i in l:
#     if i > max:
#         max= i
# print(max)






# l =[23,34,89,38]
# min = l[0]
# for i in l:
#     if i < min:
#         min= i
# print(min)

# wrong
# l=[23,90,76,45]
# second_max=-1
# max=l[0]
# for i in l:
#     if i > max:
#         max= i
# print(second_max)


# a = [89,90,101,91]

# first = a[0]
# second = a[0]
# for i in a :
#     if i > first:
#         second = first
#         first = i
#     elif i > second and i!=first :
#         second = i
# print(second)


# dict = { 1: 123, "obj": "Table" , "mark": 9.5}
# print(dict[1])
# print(dict["obj"])
# print(dict.get("mark"))
# print(dict.get("name","Not found"))
# dict[(1,2,3)] ="This is Tuple"
# print(dict)
# dict.update({"up":100, "up2": 200, "up":100})
# print(dict)

   
# dict={1:'a',2:'b',3:'c'}
# # dict[3]='r'
# # print(dict)

# # dict.pop(1)
# # print (dict)

# # del dict[2]
# # print(dict)

# # dict.clear()
# # print(dict)

# print(dict.values())
# print(dict.keys())
# for key,value in dict.items():
#     print(key,value, sep=" --> ")

# # for key in dict.items():
# #     print(key)

# # for value in dict.items():
# #     print(value)

# for i in dict.keys():
#     print(i)

# for i in dict.values():
#     print(i)



# dict.setdefault(4,'d')
# print(dict)

# dict.popitem()
# print(dict)

# keys=['a','b','c','d']
# dict2 = dict.fromkeys(keys,30)
# print(dict2)


# #match
# day = 2
# match day:
#     case 1:
#         print("Mon")
#     case 2:
#         print("Tues")
#     case 3:
#         print("Wed")
#     case 4:
#         print("Thur")
#     case 5:
#         print("Fri")


# str=["python","sania","rumaiz"]
# mystr=iter(str)
# print(next(mystr))

# import hi
# print(hi.fun(20,30))

# from hi import confidential
# confidential()


# from hi import *
# confidential()
# fun(10,20)





# str1= "eat"
# str2= "ate"
# if sorted(set(str1))== sorted(set(str2)):
#     print('Anagram')
# else:
#     print("Not an Anagram")

# str1= "listen"
# str2= "abcdeh"
# a=set(str1)
# b=set(str2)
# if a==b :
#     print("Anagram")
# else:
#     print("Not an Anagram")


# s= [0,1,0,1,0]
# zero=[]
# one=[]

# for i in s:
#     if i == 0:
#         zero.append(i)
#     else:
#         one.append(i)
#     result= zero+one
# print(result)
         
         

        

