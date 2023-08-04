lass Game:
    def get_user_item(self):
        while True:
            user_item = input("Select an item (rock/paper/scissors): ").lower()
            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Invalid item. Please select rock, paper, or scissors.")


game = Game()
user_item = game.get_user_item()
print("User selected:", user_item)

import random

class Game:
    def get_user_item(self):
        while True:
            user_item = input("Select an item (rock/paper/scissors): ").lower()
            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Invalid item. Please select rock, paper, or scissors.")

    def get_computer_item(self):
        items = ["rock", "paper", "scissors"]
        computer_item = random.choice(items)
        return computer_item


game = Game()
user_item = game.get_user_item()
computer_item = game.get_computer_item()

print("User selected:", user_item)
print("Computer selected:", computer_item)

import random

class Game:
    def get_user_item(self):
        while True:
            user_item = input("Select an item (rock/paper/scissors): ").lower()
            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Invalid item. Please select rock, paper, or scissors.")

    def get_computer_item(self):
        items = ["rock", "paper", "scissors"]
        computer_item = random.choice(items)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or (user_item == "paper" and computer_item == "rock") or (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"


game = Game()
user_item = game.get_user_item()
computer_item = game.get_computer_item()
game_result = game.get_game_result(user_item, computer_item)

print("User selected:", user_item)
print("Computer selected:", computer_item)
print("Game result:", game_result)

import random

class Game:
    def get_user_item(self):
        while True:
            user_item = input("Select an item (rock/paper/scissors): ").lower()
            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Invalid item. Please select rock, paper, or scissors.")

    def get_computer_item(self):
        items = ["rock", "paper", "scissors"]
        computer_item = random.choice(items)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or (user_item == "paper" and computer_item == "rock") or (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        game_result = self.get_game_result(user_item, computer_item)

        print("You selected:", user_item)
        print("The computer selected:", computer_item)

        if game_result == "win":
            print("You win!")
        elif game_result == "draw":
            print("It's a draw!")
        else:
            print("You lose!")

        return game_result


game = Game()
game_result = game.play()
print("Game result:", game_result)