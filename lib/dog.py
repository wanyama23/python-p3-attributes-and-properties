#!/usr/bin/env python3


APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)





    # def __init__(self, name):
    #     self._name = name

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, new_name):
    #     if type(new_name)!= str:
    #         raise Exception("Invalid value for name")
    #     if len(new_name) < 1:
    #         raise Exception("Invalid value for name")
    #     self._name = new_name
  

        # d = Dog("Fido")
        # print(d.name) # Output: Fido

        # d.name = "Rufus"
        # print(d.name) # Output: Rufus

        # try:
        #     d.name = "spot"
        # except Exception as e:
        #     print(e) # Output: Name must be string between 1 and 25 characters.



    
