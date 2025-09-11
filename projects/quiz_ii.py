import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load quiz questions from CSV
quiz_df = pd.read_csv('quiz_questions.csv')

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App Prototype")
        self.current_question = 0
        self.score = 0

        # Question label
        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        # Variable for radio buttons
        self.answer_var = tk.StringVar()

        # Options as radio buttons
        self.radio_buttons = []
        for i in range(3):
            rb = tk.Radiobutton(root, text="", variable=self.answer_var, value=f"Option{i+1}", font=("Arial", 12))
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)

        # Submit button
        self.submit_btn = tk.Button(root, text="Submit Answer", command=self.submit_answer)
        self.submit_btn.pack(pady=10)

        # Score label
        self.score_label = tk.Label(root, text=f"Score: {self.score}")
        self.score_label.pack()

        self.load_question()

    def load_question(self):
        if self.current_question < len(quiz_df):
            row = quiz_df.loc[self.current_question]
            self.question_label.config(text=row['Question'])
            self.answer_var.set(None)  # Reset selection
            self.radio_buttons[0].config(text=row['Option1'])
            self.radio_buttons[1].config(text=row['Option2'])
            self.radio_buttons[2].config(text=row['Option3'])
        else:
            messagebox.showinfo("Quiz Over", f"Your final score is {self.score} out of {len(quiz_df)}")
            self.root.quit()

    def submit_answer(self):
        selected = self.answer_var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        correct = quiz_df.loc[self.current_question, 'Answer']
        if selected == correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.current_question += 1
        self.load_question()

# Run the app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
