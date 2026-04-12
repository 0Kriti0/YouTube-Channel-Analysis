class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name: ",self.name)
        print("Roll no:",self.age)
class student(person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def display(self):
        print(self.rollno)
s=student("kriti",18,33)
#p=person("Kriti",18)
#p.display
s.display()
