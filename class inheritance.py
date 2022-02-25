# class Animal:
#     def __init__(self, ):
#         self.num_eyes = 2
#
#
#     def breathe(self):
#         print("Inhale, exhale")
#
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def swim(self):
#         print("moving in water")
#
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater")
#
#
#
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()

class Dog:
    def __init__(self):
        self.temperature = 'loyal'

class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperature= 'gentle'

doggo = Dog()
print(f"A dog is {doggo.temperature}")
sparky = Labrador()
print(f"Sparky is {sparky.temperature}")