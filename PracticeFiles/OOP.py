class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def description(self):
        return f"{self.name} is {self.age} years old."
    



buddy=person("A jay",10)

print(buddy.name,buddy.age)
buddy.description()

buddy2=person("A jayyyyyy",20)

print(buddy2.name,buddy2.age)

