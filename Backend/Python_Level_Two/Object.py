# class name usually first letter Cap and for the function name usually lowercase letter
class Dog():
    # CLASS OBJECT ATTRIBUTE
    species = "mammal"
    def __init__(self,breed,name):  # the most special method in python, they have two underscore starting and ending (self must always passed in as argument)
        self.breed = breed    # whenever creating instances using class, you must pass in the argument which decleared as attribute in the method.
        self.name = name


mydog = Dog(breed = "Lab", name = "Kiwi")# whenever creating instances using class, you must pass in the argument which decleared as attribute in the method. And must be in the same order if declear multiple attributes
print(mydog.breed) #calling the attribute breed (Lab) <-- expected to print out
print(mydog.name)
print(mydog.species) # calling the calss object attributes


################################################################################################################################

class Circle():
    
    pi = 3.14

    def __init__(self, radius =1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi # self.pi also can use instead of Circle.pi, but since pi is class attribute, best is to differentiate using class name.

    def set_radius(self, new_R):
        self.radius = new_R

myc = Circle() # creating instance 
print(myc.radius) #expected output is 1 which passed in at the __init__ method
print(myc.area()) # when calling a methond, () is necessary

newc = Circle(3) # passing in radius = 3
print(newc.radius) #expected output is 3 
print(newc.area()) #expected 28.26 = 3 * 3 * 3.14

newc.set_radius(50) # setting new radius using function inside of classes
print(newc.radius) #expected output is 50