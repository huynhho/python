# stack = []

# def view():
#     for x in range(len(stack)):
#         print(stack[x])
# def push():
#     item = input('Please enter the item you wish to add to the stack:')
#     stack.append(item)
# def pop():
#     item = stack.pop(-1)
#     print('You just popped out: ', item)

# while True:
#     print("")
#     print("*********************************")
#     print("1. View Stack")
#     print("*********************************")
#     print("Python Implementation of a Stack")
#     print("")
#     menu_choice = int(input('Please enter your menu choice: '))
#     print("")
#     if menu_choice == 1:
#         view()
#     elif menu_choice == 2:
#         push()
#     elif menu_choice == 3:
#         pop()

    
# class Dog:
#     def __init__(self, name, month, day, year, speakText):
#         self.name = name
#         self.month = month
#         self.day = day
#         self.year = year
#         self.speakText = speakText
#     def speak(self):
#         return self.speakText

#     def getName(self):
#         return self.name

#     def birthDate(self):
#         return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

#     def changeBark(self, bark):
#         self.speakText = bark

#     def __add__(self, otherDog):
#         return Dog("Puppy of" + self.name + " and " + otherDog.name, self.month, self.day, self.year + 1,
#             self.speakText + otherDog.speakText)


# def main():
#     boyDog = Dog("Mesa", 5, 15, 2004, "WOOOF")
#     girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
#     print(boyDog.speak())
#     print(girlDog.speak())
#     print(boyDog.birthDate())
#     print(girlDog.birthDate())
#     boyDog.changeBark("but I didn't really want to go in any case.")
#     print(boyDog.speak())
#     puppy = boyDog + girlDog
#     print(puppy.speak())
#     print(puppy.getName())
#     print(puppy.birthDate())
# if __name__ == "__main__":
#     main()
out_of_the_blue = "HE ANNOUNCED OUT OF THE BLUE THAT HE WANTED A DIVORCE"
print(out_of_the_blue.lower())
print(out_of_the_blue.lower().startswith('h'))



