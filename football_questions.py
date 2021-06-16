from tkinter import *
from tkinter import messagebox as mb
import json
import random
from operator import itemgetter

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.random_num = random.randint(0, 9)
        self.display_title()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.buttons()
        self.data_size = 11
        self.correct = 0
        self.next_btn()

    def display_result(self):
        wrong_count = self.data_size - self.correct - 1
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, random_num):
        if self.q_no <= 4:
            if self.opt_selected.get() == easy_answer[random_num]:
                return True
        elif 5 <= self.q_no <= 7:
            if self.opt_selected.get() == medium_answer[random_num]:
                return True
        else:
            if self.opt_selected.get() == hard_answer[random_num]:
                return True

    def next_btn(self):
        if self.check_ans(self.random_num):
            self.correct += 1
            global score
            score += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            self.display_result()
            gui.destroy()
            return
        while True:
            self.random_num = random.randint(0, 9)
            if self.random_num not in asked_questions:
                asked_questions.append(self.random_num)
                break
        if self.q_no <= 4:
            self.display_easy_question()
            self.display_easy_options()
        elif 5 <= self.q_no <= 7:
            self.display_medium_question()
            self.display_medium_options()
        elif self.q_no >= 8:
            self.display_hard_question()
            self.display_hard_options()

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)

    def display_easy_options(self):
        val = 0
        self.opt_selected.set(0)

        for option in easy_options[self.random_num]:
            self.opts[val]['text'] = option
            val += 1

    def display_easy_question(self):
        q_no = Label(gui, text=easy_question[self.random_num], width=80,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=10, y=100)

    def display_medium_options(self):
        val = 0
        self.opt_selected.set(0)

        for option in medium_options[self.random_num]:
            self.opts[val]['text'] = option
            val += 1

    def display_medium_question(self):
        q_no = Label(gui, text=medium_question[self.random_num], width=80,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=10, y=100)

    def display_hard_options(self):
        val = 0
        self.opt_selected.set(0)

        for option in hard_options[self.random_num]:
            self.opts[val]['text'] = option
            val += 1

    def display_hard_question(self):
        q_no = Label(gui, text=hard_question[self.random_num], width=80,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=10, y=100)

    def display_title(self):
        title = Label(gui, text="Football quiz",
                      width=64, bg="green", fg="white", font=("ariel", 20, "bold"), anchor=CENTER)
        title.place(x=0, y=0)

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


def validate():
    username = uname_entry.get()
    global user
    user = username
    if len(username) < 3:
        mb.showinfo(username, "Username must be at least 3 characters!")
    else:
        root.destroy()


def disable_event():
    pass


root = Tk()
root.geometry("600x300")
root.protocol("WM_DELETE_WINDOW", disable_event)
root.title("Football questions")
uname = Label(root, text="User Name")
uname.place(x=100, y=80)
uname_entry = Entry(root, bd=5)
uname_entry.place(x=200, y=80)
user = ""
submit = Button(root, text="Start quiz", command=validate)
submit.place(x=200, y=110)
root.mainloop()

gui = Tk()
gui.geometry("1024x800")
gui.title("Football questions")

score = 0

with open('easy_questions.json', encoding='utf-8') as f:
    data = json.load(f)

easy_question = (data['question'])
easy_options = (data['options'])
easy_answer = (data['answer'])

with open('medium_questions.json', encoding='utf-8') as f:
    data = json.load(f)

medium_question = (data['question'])
medium_options = (data['options'])
medium_answer = (data['answer'])

with open('hard_questions.json', encoding='utf-8') as f:
    data = json.load(f)

hard_question = (data['question'])
hard_options = (data['options'])
hard_answer = (data['answer'])

asked_questions = []

quiz = Quiz()
gui.mainloop()

file = open("scoreboard.TXT", "a")
file.writelines(f'{str(user)},{int(score)}\n')
file.close()

f = open("scoreboard.TXT", "r")
text = f.readlines()
dc = {}
ls = []

for i in range(0, len(text)):
    if '\n' in text[i].split(",")[1]:
        dc = {"name": text[i].split(",")[0], "score": int(text[i].split(",")[1][:len(text[i].split(",")[1])-1])}
    else:
        dc = {"name": text[i].split(",")[0], "score": int(text[i].split(",")[1])}

    ls.append(dc)
sort = sorted(ls, key=itemgetter('score'), reverse=True)
#print(sort)
f.close()

file1 = open('scoreboard.TXT', 'w')
for i in range(0, len(sort)):
    file1.writelines(f'{sort[i]["name"]},{sort[i]["score"]}\n')
file1.close()

#print(score)
#print(asked_questions)
#print(user)
