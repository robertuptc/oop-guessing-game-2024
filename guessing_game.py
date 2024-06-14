import random

# #####---> Solution 1 <---#####
# class GuessingGame:
#     def __init__(self, user_guess):
#         self.user_guesss = user_guess
#         self.number = 20
#         self.answer = ''
    
#     def guess(self, user_input):
#         if self.user_guesss == self.number:
#             self.answer = True
#             return "correct"
#         elif self.user_guesss < self.number:
#             self.answer = False
#             return "low"
#         else:
#             self.answer = False
#             return "high"

#     def solved(self):
#         if self.answer:
#             return True
#         else:
#             return False

# game = GuessingGame(21)
# print(game.guess())
# print(game.solved())


# #####---> Solution 2 <---#####
class GuessingGame:
    def __init__(self, num_to_guess):
        self.num_to_guess = num_to_guess
        self.answer = ''


    def guess(self, user_input):
        if self.num_to_guess == int(user_input):
            self.answer = True
            return "correct"
        elif int(user_input) < self.num_to_guess:
            self.answer = False
            return "low"
        else:
            self.answer = False
            return "high"


    def solved(self):
        if self.answer:
            return True
        else:
            return False


game = GuessingGame(random.randint(1,3))
last_guess = None
last_result = None

while game.solved() == False:
    if last_guess != None:
        print(f"Ooops! Your last guess {last_guess} was {last_result}.")
        print("")
    
    last_guess = input("Enter your guess: ")
    last_result = game.guess(last_guess)

print(f"{last_guess} was correct!")