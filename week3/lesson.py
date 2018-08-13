class Pet:
    '''_init_() is a method of the class Pet
    .A method is a function that belongs to a
    class instance. All methods of a class first
    parameter is self'''
    def _init_(self,name,age,animal="Dog"):
        '''self.name and self.age are instance attributes or
         data members of the class Pet. Instance attributes are
         unique in every occurrence (instance) of a Pet
         object'''
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hunger = False
        self.mood = "happy"

    def eat(self):
        self.is_hunger = False

        def _str_(self):
            return "{0} {1}".format(self)
'''The pet class has the members age,name,count, _init()_self.
To call the _init_() function we use the class name with the
respective parameters within parenthesis.'''

def makeHunger(pet):
    pet.is_hunger = True

#o is an object of Pet
o = Pet("Dog",3)

#t is another object of Pet
t = Pet("Cat",4)

print "Before call to makeHunger()"
print o.name, o.age, o.is_hunger
print t.name, t.age, o.is_hunger

makeHunger(o)

print "After call to makeHunger() and before call to eat()"
print o.name, o.age, o.is_hunger
print t.name, t.age, o.is_hunger

o.eat()

print
