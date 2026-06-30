# class A:
#     a = 22
#     def m(self):
#         print("Uncodemy")
    


# obj=A()
# print(obj.a)
# obj.m()


# -----------------------------------
# class car:
#     wheels = 4
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         print(f"{self.brand} {self.model} has {self.wheels} wheels")

# obj=car("ab","dd")
# print(obj.wheels)
# obj.display_info()

#-------------------Inheritance
# class A:
#     a= 20

# class B(A):
#     b = 30

# class C(B):
#     c = 40

# obj=C()
# print(obj.a)
# print(obj.b)
# print(obj.c)


#---------------------
class cat:
    def speak(self):
        print("meow")

class dog:
    def speak(self):
        print("woof")

animals = [cat(), dog()]

for animals in animal:
    animal.speak()