def get_user_menu_choice():
    while True:
        print("Menu:")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "new_game"
        elif choice == "2":
            return "show_scores"
        elif choice == "3":
            return "quit"
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


menu_choice = get_user_menu_choice()
print("User selected:", menu_choice)

def print_results(results):
    print("Game Results:")
    print("--------------")
    print("Wins:", results["win"])
    print("Losses:", results["loss"])
    print("Draws:", results["draw"])
    print("--------------")
    print("Thank you for playing!")


results = {"win": 2, "loss": 4, "draw": 3}
print_results(results)

def get_user_menu_choice():
    while True:
        print("Menu:")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "new_game"
        elif choice == "2":
            return "show_scores"
        elif choice == "3":
            return "quit"
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "new_game":
            
            print("Starting a new game...")
           

        elif choice == "show_scores":
           
            print_results(results)

        elif choice == "quit":
           
            print("Exiting the program...")
            break


main()

def get_user_menu_choice():
    while True:
        print("Menu:")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "new_game"
        elif choice == "2":
            return "show_scores"
        elif choice == "3":
            return "quit"
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def print_results(results):
    print("Game Results:")
    print("--------------")
    print("Wins:", results["win"])
    print("Losses:", results["loss"])
    print("Draws:", results["draw"])
    print("--------------")
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "new_game":
           
            game = Game()
          
            game_result = game.play()
           
            results[game_result] += 1

        elif choice == "show_scores":
           
            print_results(results)

        elif choice == "quit":
            
            print("Exiting the program...")
            break


main()

def get_user_menu_choice():
    while True:
        print("Menu:")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "new_game"
        elif choice == "2":
            return "show_scores"
        elif choice == "3":
            return "quit"
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def print_results(results):
    print("Game Results:")
    print("--------------")
    print("Wins:", results["win"])
    print("Losses:", results["loss"])
    print("Draws:", results["draw"])
    print("--------------")
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "new_game":
            
            game = Game()
           
            game_result = game.play()
            
            results[game_result] += 1

        elif choice == "show_scores":
            
            print_results(results)

        elif choice == "quit":
            
            print("Exiting the program...")
            print_results(results)
            break


main()

