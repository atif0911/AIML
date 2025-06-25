#creating a class
class Student:
    def __init__(self,name,major,gpa):
        self.name=name
        self.major=major
        self.gpa=gpa
#class functions 
    def honors(self):
        if self.gpa>=7:
            return True
        else:
            return False