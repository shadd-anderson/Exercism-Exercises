# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.correctly_guessed_letters = set()
        self.status = STATUS_ONGOING
        print(f"Welcome to hangman! You have {self.remaining_guesses} guesses remaining. \n"
              f"Your blanks: {self.get_masked_word()}")

    def guess(self, char):
        if self.status == STATUS_ONGOING:
            if char in self.word and char not in self.correctly_guessed_letters:
                self.correctly_guessed_letters.add(char)
                print(f"Correct! Current word: {self.get_masked_word()}")
            else:
                self.remaining_guesses -= 1
                print(f"Nope! Try again. you have {self.remaining_guesses} guesses remaining. \n"
                      f"Current word: {self.get_masked_word()}")
                if self.remaining_guesses == -1:
                    self.status = STATUS_LOSE
                    print(f"Sorry, you lost! The word was {self.word}")

            if self.correctly_guessed_letters.issuperset(self.word):
                self.status = STATUS_WIN
                print(f"Congrats you won! The word was {self.word}")
        else:
            raise ValueError("Game is not currently running! Please start a new game")

    def get_masked_word(self):
        word = self.word
        for letter in word:
            if letter not in self.correctly_guessed_letters:
                word = word.replace(letter, "_")
        return word

    def get_status(self):
        return self.status
