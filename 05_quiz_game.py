quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A.Paris"
    },

    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B. 4"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B. HTML"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Earth", "C. Mars", "D. Jupiter"],
        "answer": "C. Mars"
    },
    {
        "question": "Who developed Python?",
        "options": [
            "A. Elon Musk",
            "B. Guido van Rossum",
            "C. Bill Gates",
            "D. Linus Torvalds"
        ],
        "answer": "B. Guido van Rossum"
    }
]

# colores
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


# -------- QUIZ FUNCTION --------
def run_quiz():

    score = 0
    wrong_answers = []

    print("\n====== PYTHON QUIZ GAME ======")

    for i, item in enumerate(quiz, start=1):

        print(f"\nQuestion {i}: {item['question']}")

        for option in item["options"]:  # item["options"]=[A,b,c,D] # option=A
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").upper()

        correct_answer_letter = item["answer"].split(".")[0]

        if user_answer == correct_answer_letter:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            wrong_answers.append(
                (item["question"], item["answer"])
            )

    return score, wrong_answers


# -------- RUN QUIZ --------
score, wrong_anwers = run_quiz()


print("\n"f"{CYAN}===============QUIZ RESULT============={RESET} ")

print(f"Your Score: {score}/{len(quiz)}")


# -------- SHOW CORRECTIONS --------
if wrong_anwers:
    print("\nQuestions you missed:")
    for q, a in wrong_anwers:
        print(f"Q: {q}")
        print(f"Correct Answer: {a}\n")


# -------- PERFORMANCE MESSAGE --------
percentage = (score / len(quiz)) * 100

if percentage == 100:
    print("Excellent! Perfect score!")
elif percentage >= 70:
    print("Good job!")
elif percentage >= 40:
    print("Not bad, keep practicing.")
else:
    print("You should study more.")
print(f"{CYAN}==================================={RESET} ")