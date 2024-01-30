import sys
import time
import curses
import random


def quiz_progress_bar(stdscr, question, options, selected_option):
    stdscr.clear()
    stdscr.addstr(f"{question}\n")

    for i, option in enumerate(options):
        highlight = i == selected_option
        stdscr.addstr(f"[{'=' if highlight else ' '}] {option}\n")

    stdscr.refresh()

def ask_question(stdscr, question, options, correct_option):
    selected_option = 0
    quiz_progress_bar(stdscr, question, options, selected_option)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and selected_option > 0:
            selected_option -= 1
        elif key == curses.KEY_DOWN and selected_option < len(options) - 1:
            selected_option += 1
        elif key == 10:  # Enter key
            break

        quiz_progress_bar(stdscr, question, options, selected_option)
        time.sleep(0.1)  # Adjust the sleep duration based on your preferences

    return selected_option == correct_option

# Example usage in a quiz scenario
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Rome", "Madrid"],
        "correct_option": 0,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "correct_option": 1,
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1943", "1945", "1950", "1960"],
        "correct_option": 1,
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "correct_option": 1,
    },
    {
        "question": "What is the largest mammal on Earth?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_option": 1,
    },
]
# Initialize curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

score = 0
total_questions = len(questions)

questions_to_ask=questions
while len(questions_to_ask)!= 0:
    num=random.choice(questions_to_ask)
    result=ask_question(stdscr,num["question"],num["options"],num["correct_option"])
    if result:
        score +=1
    questions_to_ask.remove(num)
# Calculate the score on a scale of 100
percentage_score = (score / total_questions) * 100

# Display the final score
stdscr.clear()
stdscr.addstr(f"Your score: {score}/{total_questions} ({percentage_score:.2f}%)\nThank you for playing !")
stdscr.refresh()

# Wait for 3 seconds
time.sleep(3)

# Clean up curses
curses.endwin()
