class person:
    x=10
    y=10
    tup=(1,2,3)
    c=[5,6,7]
    d={100,300,500}

    def func(self):
        print("this is my class function")
     

#p1 is a object, person is  a class
p1=person()
p1.func()
print(p1.x)
print(p1.y)
print(p1.tup)
print(p1.c)
print(p1.d)
