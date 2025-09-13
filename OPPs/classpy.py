# class Student:
#     name="vinay"

#     s1 = Student()
#     print(s1.name)

#Class and Objects are useded to represent real world entities in programming. 
# A class is a blueprint for creating objects. An object is an instance of a class.
# A class can have attributes (variables) and methods (functions) that define the behavior of the objects created from the class.
# Objects can access the attributes and methods defined in the class. 
# Classes provide a way to encapsulate data and functionality together, promoting code reusability and organization.
# Example: 
class Car: # class definition 
    colour = "red" # class variable 

    model = "2020" # class variable 

car1 = Car() # object creation 
print(car1.colour) # accessing class variable using object 

# class Car:
#     # Class variables are defined here
#     colour = "red"
#     model = "2020"

# # Now, we instantiate the class outside its definition
# car1 = Car()

# # We can now access the class's attributes
# print(car1.colour)