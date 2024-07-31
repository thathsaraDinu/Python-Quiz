# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style #install
from quiz_data import quiz_data

#create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

def show_question():
    #get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    #Display the choices
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")
    
    #clear the feedback label and disable net button
    feedback_label.config(text = "")
    next_btn.config(state="disabled")

#function to check the selkected answer and give feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        if score == 10:
            messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Congrats! You got full score: {}/{}".format(score, len(quiz_data)))
        else:
            messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Create a style object
style = ttk.Style()

# Create a custom style for the frame
style.configure("Custom.TFrame", background="lightblue")

outer_frame = tk.Frame(
    root,
    pady=20,
    bg='red'
)
outer_frame.pack(pady=10)

#create the question label
qs_label = ttk.Label(
    outer_frame,
    anchor = "center", 
    wraplength=500,
    padding=10,
)

qs_label.pack(pady=20)

# create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        outer_frame,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    outer_frame,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    outer_frame,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    outer_frame,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0




# Show the first question
show_question()

# Start the main event loop
root.mainloop()

