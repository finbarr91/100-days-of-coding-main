# class User:
#     pass

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Finbarr Obierefu"
# print(user_1.username)

# user_2 = User()
# user_2.id = "002"

# class Car:
#     def __init__(self, brand, color,type, control, number_of_seats):
#         self.fuel_efficiency = 'hybrid'
#         self.color = 'color'
#         self.type = 'type'
#         self.control = 'control'
#         self.transmission = 'Automatic'
#         self.brand = brand
#         self.number_of_tires = 4
#         self.number_of_seats = 'number_of_seats'

#     def move(self,forward,backward):

#         if forward =='x':
#             print("Moving forward")
#         if backward=='y':
#             print("moving backward")

# chisom_car = Car( brand ='Lexus', color = 'Blue', type = 'SUV', control = '4WD', number_of_seats= 7)
# chuka_car = Car( brand ='Toyota', type = 'Salon', color='Black', control = '2WD', number_of_seats=5)
# print(chisom_car.number_of_tires)
# chisom_car.move('x','y')

class User:
    def __init__(self,username,user_id):
        self.username = username
        self.user_id = user_id
        self.following = 0
        self.followers = 0

    def follow(self,user):
        self.following=self.following+1
        user.followers+=1

user1 = User(username= "Finbarr Obierefu", user_id= "001")
user2 = User(username="Chisom Amete", user_id= "002")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
