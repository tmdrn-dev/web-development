class Employee:
    # public class variables
    company = 'LGE'
    # private class variables
    __salary = 100000000

    def __init__(self, name, salary):
        # creating public instance variables
        self.name = name

    @classmethod
    # cls: convention, cls is used to refer to the class
    def getEmployInfo(cls):
        return cls.company, cls.__salary

#calling method using class name
print(Employee.getEmployInfo())

class Player:
    # class variables
    teamName ='Liverpool'

    def __init__(self, name = None):
        # creating instance variables
        self.name = name

    @staticmethod
    def demo():
        print ("I am a static method.")

p1 = Player('Seungku')
p1.demo()
Player.demo()