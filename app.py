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
    {
        "question": "What is the smallest planet in our solar system?",
        "options": ["Mercury", "Mars", "Earth", "Venus"],
        "correct_option": 0,
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "correct_option": 2,
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Australia", "Japan", "India"],
        "correct_option": 2,
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "correct_option": 2,
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Perth", "Canberra", "Melbourne"],
        "correct_option": 2,
    },
    {
        "question": "What is the largest organ of the human body?",
        "options": ["Heart", "Skin", "Liver", "Brain"],
        "correct_option": 1,
    },
    {
        "question": "What year did the Titanic sink?",
        "options": ["1912", "1915", "1920", "1930"],
        "correct_option": 0,
    },
    {
        "question": "What element does 'H' stand for on the periodic table?",
        "options": ["Helium", "Hydrogen", "Hafnium", "Mercury"],
        "correct_option": 1,
    },
    {
        "question": "What is the capital of Spain?",
        "options": ["Barcelona", "Madrid", "Seville", "Valencia"],
        "correct_option": 1,
    },
    {
        "question": "What does DNA stand for?",
        "options": ["Deoxyribonucleic Acid", "Deoxyribogenetic Acid", "Dinucleic Acid", "Dinucleotide Acid"],
        "correct_option": 0,
    },
    {
        "question": "Who wrote 'The Odyssey'?",
        "options": ["Homer", "Virgil", "Socrates", "Plato"],
        "correct_option": 0,
    },
    {
        "question": "In what year did man first land on the moon?",
        "options": ["1969", "1970", "1965", "1972"],
        "correct_option": 0,
    },
    {
        "question": "Who was the first woman to win a Nobel Prize?",
        "options": ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Dorothy Hodgkin"],
        "correct_option": 0,
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["100°C", "90°C", "80°C", "120°C"],
        "correct_option": 0,
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["United Kingdom", "Brazil", "China", "Russia"],
        "correct_option": 1,
    }
]
# Initialize curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

score = 0
total_questions = len(questions)

questions_to_ask=questions
for i in range(10):
    num=random.choice(questions_to_ask)
    result=ask_question(stdscr,num["question"],num["options"],num["correct_option"])
    if result:
        score +=1
    questions_to_ask.remove(num)
    i+=1
# Calculate the score on a scale of 100
percentage_score = (score / 10) * 100

# Display the final score
stdscr.clear()
stdscr.addstr(f"Your score: {score}/{10} ({percentage_score:.2f}%)\nThank you for playing !")
stdscr.refresh()

# Wait for 3 seconds
time.sleep(3)

# Clean up curses
curses.endwin()
