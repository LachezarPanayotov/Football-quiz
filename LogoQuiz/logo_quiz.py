from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_logo()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(logo)
        self.correct = 0

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_logo()
            self.display_options()

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)

        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_logo(self):
        photo = PhotoImage(file=logo[self.q_no])
        q_no = Label(gui, image=photo, width=120, height=120,
                     font=('ariel', 16, 'bold'), anchor='w', bg='black')
        q_no.place(x=250, y=30)

    def display_title(self):
        title = Label(gui, text="Football quiz",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 150

        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))

            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        return q_list

gui = Tk()
gui.geometry("640x480")
gui.title("Logo quiz")

with open('easy_logos.json', encoding='utf-8') as f:
    data = json.load(f)

logo = (data['logos'])
options = (data['options'])
answer = (data['answer'])

quiz = Quiz()

gui.mainloop()