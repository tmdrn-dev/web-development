class Person():
    def __init__(self, name, language):
        '''constructor'''
        self.name = name
        self.language = language

    def __str__(self):
        '''print(person)'''
        return '{} is {}'.format(self.name, self.language)

    def speak(self):
        print('{} speaks {}'.format(self.name, self.language))

person = Person('csk', 'korean')
person.speak()

# __str__
print(person)

# inherit
class Programmer(Person):
    def __init__(self, name = None, language = None, skill = None):
        # super: call base class method
        # call base class constructor
        super().__init__(name, language)
        self.skill = skill
    def speak(self):
        super().speak()
        print('{} uses {}'.format(self.name, self.skill))

programmer = Programmer('csk', 'korean', 'python')
programmer.speak()