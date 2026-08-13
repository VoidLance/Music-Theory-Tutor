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

# Run a generic quiz from a list of question/answer pairs.
def run_quiz(title: str, questions: list):
    score = 0
    print(title)
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
        print("Excellent work!")
    elif score >= len(questions) // 2:
        print("Good effort. Keep practising.")
    else:
        print("Keep going. Repetition is the key to building confidence.")

# Create function to run a simple key signature quiz.
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
    run_quiz("♯ Key Signature Quiz ♯", questions)

# Scale quiz.
def scale_quiz():
    questions = [
        {"question": "What is the G major scale?", "answer": "G A B C D E F#"},
        {"question": "What is the C major scale?", "answer": "C D E F G A B"},
        {"question": "What is the scale pattern for a major scale?", "answer": "W W H W W W H"},
        {"question": "What is the natural minor scale for A minor?", "answer": "A B C D E F G"},
        {"question": "What is the relative minor of G major?", "answer": "E minor"},
        {"question": "What is the D major scale?", "answer": "D E F# G A B C#"},
    ]
    run_quiz("♭ Scale Quiz ♭", questions)

# Chord quiz.
def chord_quiz():
    questions = [
        {"question": "What is the G major triad?", "answer": "G B D"},
        {"question": "What is the C major triad?", "answer": "C E G"},
        {"question": "What are the 1st, 3rd, and 5th notes of F major?", "answer": "F A C"},
        {"question": "What is the A minor triad?", "answer": "A C E"},
        {"question": "What is the D major triad?", "answer": "D F# A"},
        {"question": "What is the key note used to build a triad?", "answer": "1"},
    ]
    run_quiz("♮ Chord Quiz ♮", questions)

# Modes quiz.
def modes_quiz():
    questions = [
        {"question": "What is the second mode of C major called?", "answer": "Dorian"},
        {"question": "What mode is built from the 6th degree of C major?", "answer": "Aeolian"},
        {"question": "What is the quality of Dorian?", "answer": "Minor"},
        {"question": "What mode is the bright, airy major mode built on the 4th degree of C major?", "answer": "Lydian"},
        {"question": "What is the 7th mode of C major called?", "answer": "Locrian"},
        {"question": "What mode is commonly described as bluesy and relaxed?", "answer": "Mixolydian"},
    ]
    run_quiz("♯ Modes Quiz ♯", questions)

# Combined quiz.
def combined_quiz():
    questions = [
        {"question": "How many sharps are in E major?", "answer": "4"},
        {"question": "What is the G major scale?", "answer": "G A B C D E F#"},
        {"question": "What is the G major triad?", "answer": "G B D"},
        {"question": "What mode is built on the 2nd degree of C major?", "answer": "Dorian"},
        {"question": "What is the relative minor of G major?", "answer": "E minor"},
        {"question": "What is the order of flats?", "answer": "B E A D G C F"},
        {"question": "What is the 6th mode of C major called?", "answer": "Aeolian"},
        {"question": "What is the C major triad?", "answer": "C E G"},
        {"question": "What is the natural minor scale for A minor?", "answer": "A B C D E F G"},
        {"question": "What is the quality of Locrian?", "answer": "Diminished"},
    ]
    run_quiz("🎼 Combined Music Theory Quiz 🎼", questions)

# Create function to show the quiz menu and start the selected quiz.
def quiz(menu_choice: str = None):
    if menu_choice is None:
        print("Quiz Menu")
        print("1. Key Signature Quiz")
        print("2. Scale Quiz")
        print("3. Chord Quiz")
        print("4. Modes Quiz")
        print("5. Combined Quiz")
        print("6. Exit")

        try:
            menu_choice = input("Choose a quiz: ")
        except EOFError:
            print("No quiz selection was provided.")
            return

    selection = menu_choice.strip().lower()

    if selection in ["1", "key", "keys", "key signature", "key_signature"]:
        key_signature_quiz()
    elif selection in ["2", "scale", "scales"]:
        scale_quiz()
    elif selection in ["3", "chord", "chords"]:
        chord_quiz()
    elif selection in ["4", "mode", "modes"]:
        modes_quiz()
    elif selection in ["5", "combined", "all"]:
        combined_quiz()
    elif selection in ["6", "exit", "quit"]:
        print("Returning to the main menu.")
    else:
        print("Unknown choice. Please choose 1-6 or a quiz name.")
        quiz()


__all__ = [
    "normalize_note_sequence", "normalize_number_answer", "answer_is_correct",
    "key_signature_quiz", "scale_quiz", "chord_quiz", "modes_quiz", "combined_quiz", "quiz"
]
