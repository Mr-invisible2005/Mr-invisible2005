#single class
class Vehicle:
        def __init__(self,milage,cost):
             self.milage=milage
             self.cost=cost
        def show_details(self):
            print("milage is", self.milage)
            print("cost is",self.cost)
            print("i am vehicle")
v1=Vehicle(500,500)
v1.show_details()
print("*************************************************")

class Car(Vehicle):
    def __init__(self,milage,cost,tyres,hp):
             super().__init__(milage,cost)
             self.tyres=tyres
             self.hp=hp   
    def show_car_details(self):
        print("tyres is",self.tyres)
        print("hp is equal to ",self.hp)
c1=Car(300,5000,4,322)
c1.show_details()
c1.show_car_details()
print("*************************************************")
#multiple class

class Parent1:
        def str_1(self,str1):
                self.str1=str1
        def show_str1(self):
                return self.str1
class Parent2:
        def str_2(self,str2):
                self.str2=str2
        def show_str2(self):
                return self.str2
class Derived(Parent1,Parent2):
        def str_3(self,str3):
                self.str3=str3
        def show_str3(self):
                return self.str3
d1=Derived()
d1.str_1("parent 1")
d1.str_2("parent 2")
d1.str_3("parent 3")

print("********************************")
x=d1.show_str1()
y=d1.show_str2()
z=d1.show_str2()

print(x,y,z)

#multulevel class

class Parent:
        def str1(self,name):
                self.name=name
        def show_name(self):
                return self.name
class Child(Parent):
        def str2(self,age):
                self.age=age
        def show_age(self):
                return self.age
class Grand(Child):
        def str3(self,gender):
                self.gender=gender
        def show_gender(self):
                return self.gender

gc=Grand()
gc.str1("Vishal")
gc.str2(20)
gc.str3("Male")

x=gc.show_name()
print(x)
y=gc.show_age()
print(y)
z=gc.show_gender()
print(z)
        
                  
        
