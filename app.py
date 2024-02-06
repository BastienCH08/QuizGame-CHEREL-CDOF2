import curses
import time
import random

def draw_progress_bar(stdscr, time_left, total_time=10):
    """Draws a progress bar showing the time left."""
    bar_length = 20  # Length of the progress bar
    progress_length = int((time_left / total_time) * bar_length)

    bar = '[' + '=' * progress_length + ' ' * (bar_length - progress_length) + ']'
    stdscr.addstr(2, 0, f"Time left: {bar} {time_left:.1f}s\n\n")

def quiz_progress_bar(stdscr, question, options, selected_option, time_left):
    """Displays the quiz question, options, and the progress bar."""
    stdscr.clear()
    stdscr.addstr(f"{question}\n\n")

    draw_progress_bar(stdscr, time_left)

    for i, option in enumerate(options):
        highlight = i == selected_option
        stdscr.addstr(f"[{'=' if highlight else ' '}] {option}\n")

    stdscr.refresh()

def ask_question(stdscr, question, options, correct_option):
    """Asks a quiz question and returns True if the answer is correct, False if time is up."""
    stdscr.nodelay(1)  # Set stdscr.getch() to non-blocking mode
    selected_option = 0
    time_limit = 10  # Time limit for each question in seconds
    start_time = time.time()

    while True:
        time_left = time_limit - (time.time() - start_time)
        quiz_progress_bar(stdscr, question, options, selected_option, time_left)

        if time_left <= 0:
            # Refresh the progress bar with 0 seconds left before displaying "Time's up"
            quiz_progress_bar(stdscr, question, options, selected_option, 0)
            stdscr.addstr("\nTime's up!")
            stdscr.refresh()
            time.sleep(2)
            return False  # Return False if time is up

        key = stdscr.getch()
        if key == curses.KEY_UP and selected_option > 0:
            selected_option -= 1
        elif key == curses.KEY_DOWN and selected_option < len(options) - 1:
            selected_option += 1
        elif key == 10:  # Enter key
            break

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
