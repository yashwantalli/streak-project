import random
import sys

# quizz-app.py
# Simple interactive CLI quiz with score tracking


QUESTIONS = [
    {
        "question": "What is the currency of Japan?",
        "options": ["Yen", "Rupee", "Euro", "Dollar", "Pound"],
        "answer": "Yen",
    },
    {
        "question": "What is the currency of India?",
        "options": ["Rupee", "Dollar", "Euro", "Pound", "Yen"],
        "answer": "Rupee",
    },
    {
        "question": "What is the currency of the United States?",
        "options": ["Dollar", "Euro", "Pound", "Yen", "Rupee"],
        "answer": "Dollar",
    },
    {
        "question": "What is the currency of the United Kingdom?",
        "options": ["Pound", "Euro", "Dollar", "Yen", "Rupee"],
        "answer": "Pound",
    },
    {
        "question": "What is the currency of the European Union (most member states)?",
        "options": ["Euro", "Dollar", "Pound", "Yen", "Rupee"],
        "answer": "Euro",
    },
    {
        "question": "What is the currency of Australia?",
        "options": ["Australian Dollar", "Dollar", "Euro", "Pound", "Yen"],
        "answer": "Australian Dollar",
    },
    {
        "question": "What is the currency of Canada?",
        "options": ["Canadian Dollar", "Dollar", "Euro", "Pound", "Yen"],
        "answer": "Canadian Dollar",
    },
    {
        "question": "What is the currency of China?",
        "options": ["Renminbi (Yuan)", "Dollar", "Euro", "Pound", "Rupee"],
        "answer": "Renminbi (Yuan)",
    },
]

def ask_question(qobj, qnum, total):
    question = qobj["question"]
    correct = qobj["answer"]
    opts = qobj["options"][:]
    random.shuffle(opts)
    print(f"\nQuestion {qnum}/{total}: {question}")
    for i, opt in enumerate(opts, start=1):
        print(f"  {i}. {opt}")
    print("  q. Quit and show score")
    while True:
        choice = input("Your answer (number or q): ").strip().lower()
        if choice == "q":
            return None  # signal quit
        if not choice.isdigit():
            print("Enter a number corresponding to an option, or 'q' to quit.")
            continue
        idx = int(choice) - 1
        if 0 <= idx < len(opts):
            selected = opts[idx]
            is_correct = selected == correct
            return is_correct, selected, correct
        print("Choice out of range. Try again.")

def run_quiz():
    print("Welcome to the Currency Quiz! Type 'q' to quit anytime.")
    questions = QUESTIONS[:]
    random.shuffle(questions)
    total = len(questions)
    asked = 0
    correct_count = 0

    for i, q in enumerate(questions, start=1):
        result = ask_question(q, i, total)
        if result is None:
            break
        is_correct, selected, correct = result
        asked += 1
        if is_correct:
            correct_count += 1
            print("Correct!")
        else:
            print(f"Incorrect. You answered: {selected!r}. Correct answer: {correct!r}.")

    if asked == 0:
        print("\nNo questions answered. Goodbye.")
        return

    pct = correct_count / asked * 100
    print("\nQuiz complete.")
    print(f"Answered: {asked}  Correct: {correct_count}  Score: {pct:.1f}%")

if __name__ == "__main__":
    try:
        run_quiz()
    except (KeyboardInterrupt, EOFError):
        print("\n\nQuiz interrupted. Goodbye.")
        sys.exit(0)