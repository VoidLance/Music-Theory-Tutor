import re

# This is the quiz side of the app.
# It keeps the learning practical by checking the answers in a flexible way, so the user can type variations that still mean the same thing.
# It also suits the broader project aim: a learning tool that can become more general over time, rather than being locked into one very narrow function.


def normalize_note_sequence(answer: str):
    text = answer.strip().lower().replace("♭", "b").replace("♯", "#").replace("ﬂ", "b")
    text = text.replace(",", " ").replace("-", " ").replace("/", " ")
    text = re.sub(r"([a-g])(?:#|b)", r"\1", text)
    text = re.sub(r"[^a-g\s]", " ", text)
    return " ".join(text.split())

# Create helper to compare numeric answers using both digits and words
# This helps accept "4", "four", and "4 sharps" as equivalent.
def normalize_number_answer(answer: str):
    text = answer.strip().lower().replace("sharp", "").replace("sharps", "").replace("flat", "").replace("flats", "")
    text = text.replace("♭", "b").replace("♯", "#").replace("ﬂ", "b")
    text = re.sub(r"[^a-z0-9]", " ", text)

    number_words = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    for word, number in number_words.items():
        text = text.replace(word, number)

    cleaned = re.sub(r"[^0-9]", "", text)
    return cleaned

# Create helper to compare sequence-based answers such as notes and key-signature order
# This accepts punctuation, commas, accidental marks, and case differences as equivalent.
def answer_is_correct(user_answer: str, expected_answer: str, question_text: str):
    if "how many" in question_text:
        return normalize_number_answer(user_answer) == normalize_number_answer(expected_answer)

    if "mnemonic" in question_text:
        normalized_user = " ".join(re.sub(r"[^a-z]", " ", user_answer.lower()).split())
        normalized_expected = " ".join(re.sub(r"[^a-z]", " ", expected_answer.lower()).split())
        return normalized_user == normalized_expected

    normalized_user = normalize_note_sequence(user_answer)
    normalized_expected = normalize_note_sequence(expected_answer)
    return normalized_user == normalized_expected

# Create function to run a simple key signature quiz
# This quiz covers the main ideas learned so far: number of sharps/flats, accidentals, order, and mnemonic.
def key_signature_quiz():
    questions = [
        {"question": "How many sharps are in E major?", "answer": "4"},
        {"question": "Which notes are sharp in A major?", "answer": "F# C# G#"},
        {"question": "What is the order of sharps?", "answer": "F C G D A E B"},
        {"question": "How many flats are in B♭ major?", "answer": "2"},
        {"question": "Which notes are flat in E♭ major?", "answer": "B♭ E♭ A♭"},
        {"question": "What is the order of flats?", "answer": "B E A D G C F"},
        {"question": "What is the mnemonic to remember the order of sharps?", "answer": "Father Charles Goes Down And Ends Battle"},
        {"question": "What is the relative major key for A minor?", "answer": "C"},
        {"question": "How many sharps are in E minor?", "answer": "1"},
    ]

    score = 0

    print("♯ Key Signature Quiz ♯")
    print("Answer each question as best you can. Press enter to continue.")

    for question in questions:
        print(f"\n{question['question']}")
        try:
            user_answer = input("Your answer: ")
        except EOFError:
            print("\nQuiz ended because no more input was available.")
            return

        question_text = question["question"].lower()

        if answer_is_correct(user_answer, question["answer"], question_text):
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. The correct answer is: {question['answer']}")

    print(f"\nYour score: {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent work! You know your key signatures well.")
    elif score >= len(questions) // 2:
        print("Good effort. Keep practising the order of sharps and flats.")
    else:
        print("Keep going. The order and key patterns are very learnable with repetition.")

# Create function to show the quiz menu and start the selected quiz
# This is the start point for future quiz modules, though only the key signature quiz exists for now.
def quiz(menu_choice: str = None):
    if menu_choice is None:
        print("Quiz Menu")
        print("1. Key Signature Quiz")
        print("2. Exit")

        try:
            menu_choice = input("Choose a quiz: ")
        except EOFError:
            print("No quiz selection was provided.")
            return

    if menu_choice == "1":
        key_signature_quiz()
    elif menu_choice == "2":
        print("Returning to the main menu.")
    else:
        print("Unknown choice. Please choose 1 or 2.")
        quiz()


__all__ = ["normalize_note_sequence", "normalize_number_answer", "answer_is_correct", "key_signature_quiz", "quiz"]
