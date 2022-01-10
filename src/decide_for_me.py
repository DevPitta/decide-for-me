from random import randrange
from time import sleep
from colors import FontColors, Styles

fc = FontColors()
s = Styles()


class Game():
    def select_response(self):
        while True:
            header()
            self.question = str(input(f"{fc.cyan}Ask yourself something: {s.end}"))
            self.archive = open("answers.txt", "r")
            self.answers = []
            for line in self.archive:
                line = line.strip()
                self.answers.append(line)
            self.archive.close()
            answer_number = randrange(0, len(self.answers))
            chosen_answer = self.answers[answer_number]
            answer(chosen_answer)
            self.response = str(
                input("Would you like to ask again? [Y/N] ")).upper().strip()
            if self.response == "N":
                break
            while self.response not in "YN":
                self.response = str(input("Invalid input! Type only Y or N: ")).upper().strip()
        print(f"{fc.magenta}Thanks for asking. Check back often!{s.end}")


def answer(chosen_answer):
    """Choose a answer from answers list"""
    print(f"{fc.yellow}I'm thinking...{s.end}")
    sleep(2)
    print(f"{fc.green}Answer:{s.end} {chosen_answer}")


def header():
    title = "   DECIDE FOR ME   "
    print('-=' * 15)
    print(f"{fc.white}{s.bold}{title.center(30)}{s.end}")
    print('-=' * 15)
