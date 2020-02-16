############## OBJECT ORIENTED PYTHON: INTRODUCTION ##############

# Methods are like functions that are part of an object
 
 ############## OBJECT ORIENTED PYTHON: WHAT IS AN OBJECT? ##############
 
# A program is made up of many cooperating objects

# Insted of being the "whole program" -  each object is a little "island" within the program and cooperatively working with other objects.
 
# A program is made up of one or more objects working together - objects make use of each other's capabilities.

# Object: a bit of self-contained code and data, a key aspect of the object approach is to break the problem into smaller understandable parts, objects have boundaries that allow us to ignore unneeded detail. 

############## OBJECT ORIENTED PYTHON: TERMINOLOGY ##############

# Class: a template (ex. Dog)
# Meethod or Message: a defined capability of a class (ex. bark())
# Field or attribute: a bit of data in a class (ex. length)
# Object or instance: a particular instance of a class (ex. Lassie)

############## OBJECT ORIENTED PYTHON: Simple Python Objects ##############

class PartyAnimal:
    
    x = 0
    
    def party(self):
        self.x = self.x + 1
        print "So far", self.x
        
an = PartyAnimal()

an.party()
an.party()
an.party()

############## OBJECT ORIENTED PYTHON: Object Life Cycle ##############

# Objects are created, used and discarded
# We have special blocks of code (methods) that get called
# >> At the moment of creation (constructor)
# >> At the moment of destruction (destructor)
# Constructors are used a lot - The primary purpose of the constructor is to set up some instance variables to have the proper initial values when the object is created
# Destructors are seldom used - 

class PartyAnimal:
    
    x = 0
    
    def _init_(self):
        print "I am constructed"
        
    def party(self):
        self.x = self.x + 1
        print "So far", self.x
    
    def _del_(self):
        print "I am destructed", self.x
        
an = PartyAnimal()

an.party()
an.party()
an.party()

############## OBJECT ORIENTED PYTHON: Inheritance ##############

# When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class

# The new class (child)/(subclasses) inherit features from the (parent)/class

class PartyAnimal:
    
    x = 0
    
    def _init_(self):
        print "I am constructed"
        
    def party(self):
        self.x = self.x + 1
        print "So far", self.x
    
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points +7
        self.party()
        print self.name, "points", self.points
        
