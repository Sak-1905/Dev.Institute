from anagram_checker import AnagramChecker

class AnagramApp:
    def __init__(self, namelist.txt):
        self.anagram_checker = AnagramChecker(namelist.txt)

    def run(self):
        print("Welcome to the Anagram App!")
        print("----------------------------")

        while True:
            user_input = input("Enter a word (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Thank you for using the Anagram App. Goodbye!")
                break

            if not self.anagram_checker.is_valid_word(user_input):
                print("Invalid word. Please try again.")
                continue

            anagrams = self.anagram_checker.get_anagrams(user_input)
            if not anagrams:
                print("No anagrams found for the given word.")
            else:
                print("Anagrams:")
                for anagram in anagrams:
                    print(anagram)


if __name__ == "__main__":
    namelist = 'namelist.txt'
    app = AnagramApp(namelist.txt)
    app.run()
