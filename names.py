import numpy as np 
class Players:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def Play(self):
        print("Congrats!!")
name = input("Enter first name : ")
lastnem = input("Enter your Last Name : ")

playr1 = Players(name, lastnem)

# print(playee.first_name)
# print(playee.last_name)
playee.Play()