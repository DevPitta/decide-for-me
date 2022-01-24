import PySimpleGUI as sg
from random import randrange

question_image = 'image/question.png'


class Game:
    def select_response(self):
        while True:
            self.archive = open('answers.txt', 'r')
            self.answers = []
            for line in self.archive:
                line = line.strip()
                self.answers.append(line)
            self.archive.close()
            answer_number = randrange(0, len(self.answers))
            chosen_answer = self.answers[answer_number]
            print(f"Answer: {chosen_answer}")
            sg.popup_ok(chosen_answer, title='Answer', font=12)
            break


class PythonScreen(Game):
    def __init__(self):
        # Change color layout
        sg.change_look_and_feel('Dark Blue 3')
        # Layout
        layout = [
            [sg.Image(filename=question_image)],
            [sg.Text('Ask something to yourself:', font=14)],
            [sg.Input(font=14, size=(40, 0), key='ask')],
            [sg.Output(font=14, size=(40, 20))],
            [sg.Button("Ask", font=14, size=(38, 0), button_color='green')]
        ]
        # Window
        self.window = sg.Window("Ask Something").layout(layout)

    def Start(self):
        while True:
            # Extract screen data
            self.button, self.values = self.window.Read()
            question = self.values['ask']
            print(f"Question: {question}")
            self.select_response()
            print('-' * 30)
            sg.popup_no_buttons("Thanks for asking!", title='Thanks', font=12,
                                auto_close=True,  auto_close_duration=1.5)
            ask_again = sg.popup_yes_no("Do you want to ask something else?",
                                        title='Ask Again', font=12)
            if ask_again == 'No':
                break
