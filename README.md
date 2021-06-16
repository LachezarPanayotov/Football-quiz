# Football-quiz
**This is a school project. It's basically two quizzes in one menu.**

**But only the quiz with the questions is finished**


# About Football questions

**class Quiz:**

class to define the components of the GUI

**def __init__(self):**

This is the first method which is called when a new object of the class is initialized.

**def display_result(self):**

This method is used to display the result. It counts the number of correct and wrong answers and then display them at the end as a message Box.

**def check_ans(self, random_num):**

This method checks the Answer after we click on Next.

**def next_btn(self):**

This method is used to check the answer of the current question. If it is last question then it calls display result to show the message box. Otherwise shows next question.

**def buttons(self):**

This method shows the button on the screen. The next_button moves to next question.

**def display_easy_question(self):**

**def display_medium_question(self):**

**def display_hard_question(self):**

This methods show the current Question on the screen.

**def display_easy_options(self):**

**def display_medium_options(self):**

**def display_hard_options(self):**

This method deselect the radio button on the screen. Then it is used to display the options available for the current question.

**def display_title(self):**

This method is used to Display Title.

**def radio_buttons(self):**

This method shows the radio buttons to select the Question on the screen at the specified position. It also returns a list of radio button which are later used to add the options to them.

**def validate():**

This function is used to check if the username contains 3 or more characters.
