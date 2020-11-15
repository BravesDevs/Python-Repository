class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and {self.age} year old")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def show(self):
        print(f"I am {self.name} and {self.age} year old and my color is {self.color}")

    def speak():
        print("Meow!")

class Dog(Pet):
    def speak():
        print("Bhauuuu!")

p=Pet("Tim",19)
p.show()

c=Cat("Meme",19,"Black")
c.show()