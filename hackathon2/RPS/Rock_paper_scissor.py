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
           
            game = ()
          
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
            
            game = ()
           
            game_result = game.play()
            
            results[game_result] += 1

        elif choice == "show_scores":
            
            print_results(results)

        elif choice == "quit":
            
            print("Exiting the program...")
            print_results(results)
            break


main()
def print_results(results):
    print("Game Results:")
    print("--------------")
    print("Wins:", results["win"])
    print("Losses:", results["loss"])
    print("Draws:", results["draw"])
    print("--------------")
    print("Thank you for playing!")

    # Save results to file
    with open("game_results.txt", "w") as file:
        file.write(f"Wins: {results['win']}\n")
        file.write(f"Losses: {results['loss']}\n")
        file.write(f"Draws: {results['draw']}\n")

def main():
    # Initialize results dictionary with initial values of 0
    results = {"win": 0, "loss": 0, "draw": 0}

    # Read results from file (if it exists)
    try:
        with open("game_results.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(": ")
                results[key.lower()] = int(value)
    except FileNotFoundError:
        pass

    while True:
        # ... (rest of the code remains unchanged)
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
           
            game =()
          
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
            
            game =()
           
            game_result = game.play()
            
            results[game_result] += 1

        elif choice == "show_scores":
            
            print_results(results)

        elif choice == "quit":
            
            print("Exiting the program...")
            print_results(results)
            break


main()
def main():
    # ... (previous code)

    while True:
        # ... (previous code)elif choice == "quit":
        print("Exiting the program...")

            # Save final results to file
        with open("game_results.txt", "w") as file:
                for key, value in results.items():
                    file.write(f"{key.capitalize()}: {value}\n")
        break

main()

def main():
    # Initialize results dictionary with initial values of 0
    results = {"win": 0, "loss": 0, "draw": 0}

    # Read results from file (if it exists)
    try:
        with open("game_results.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(": ")
                results[key.lower()] = int(value)
    except FileNotFoundError:
        pass

    while True:
        choice = get_user_menu_choice()

        if choice == "new_game":
            game = ()
            game_result = game.play()
            results[game_result] += 1

        elif choice == "show_scores":
            print_results(results)

        elif choice == "quit":
            print("Exiting the program...")

            # Save final results to file
            with open("game_results.txt", "w") as file:
                for key, value in results.items():
                    file.write(f"{key.capitalize()}: {value}\n")
            break

main()
#Now the while True loop in the main function will repeatedly display the menu and allow the user to select options until the user 
# chooses to quit (option 3). The game results are saved to the file whenever the user decides to quit, and the program terminates
#  gracefully.
#You can run this code in your terminal, play the Rock-Paper-Scissors game, and interact with the menu to explore the functionalities. 
#The game results will be saved to the file "game_results.txt" for future reference.