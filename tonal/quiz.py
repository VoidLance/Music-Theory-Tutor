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

# Circle of fifths quiz.
def circle_of_fifths_quiz():
    questions = [
        {"question": "Which key is a perfect fifth above C major?", "answer": "G"},
        {"question": "Which key is a perfect fifth below C major?", "answer": "F"},
        {"question": "What is the order of the sharp keys around the circle?", "answer": "C G D A E B F# C#"},
        {"question": "What is the order of the flat keys around the circle?", "answer": "C F B♭ E♭ A♭ D♭ G♭ C♭"},
        {"question": "What happens to the key signature each step clockwise on the circle?", "answer": "One sharp"},
        {"question": "What happens to the key signature each step counterclockwise on the circle?", "answer": "One flat"},
    ]
    run_quiz("🔁 Circle of Fifths Quiz 🔁", questions)

# Transposition quiz.
def transposition_quiz():
    questions = [
        {"question": "What does transposition mean?", "answer": "Move every note by the same interval while keeping the pattern of relationships intact"},
        {"question": "If you transpose C major to G major, what interval do you move by?", "answer": "Perfect fifth"},
        {"question": "What stays the same when you transpose a melody?", "answer": "The interval pattern and musical shape"},
        {"question": "What usually changes when a piece is transposed?", "answer": "The tonal centre and key signature"},
        {"question": "Why do musicians transpose music?", "answer": "To suit range, instrument, or comfortable key"},
        {"question": "What is the effect of transposition on chord functions?", "answer": "They remain the same, just at a new pitch level"},
    ]
    run_quiz("♫ Transposition Quiz ♫", questions)

# Bass fretboard quiz.
def bassfret_quiz():
    questions = [
        {"question": "What are the open strings on a 4-string bass?", "answer": "E A D G"},
        {"question": "Which fret on any string gives the same pitch as the next string open?", "answer": "5"},
        {"question": "Which fret is a useful landing point for chord tones and root movement?", "answer": "7"},
        {"question": "Where does the note-name pattern repeat on the bass neck?", "answer": "12th fret"},
        {"question": "Why are the 5th and 7th frets so useful?", "answer": "They give easy anchor points for navigation and chord tones"},
        {"question": "What do the money notes help you learn?", "answer": "The shape of the fretboard and repeated note relationships"},
    ]
    run_quiz("🎸 Bass Fretboard Quiz 🎸", questions)

# Riff quiz.
def riff_quiz():
    questions = [
        {"question": "What is a riff?", "answer": "A short repeated musical pattern"},
        {"question": "What makes a riff memorable?", "answer": "Rhythm, repetition, and a strong melodic shape"},
        {"question": "What is the best place to begin when building a riff?", "answer": "A simple rhythmic idea and a target chord"},
        {"question": "Why is repetition important in a riff?", "answer": "It helps the listener remember the phrase and lock into the groove"},
        {"question": "What is one useful starting note choice for a riff over G major?", "answer": "G"},
    ]
    run_quiz("🎶 Riff Quiz 🎶", questions)

# Bassline quiz.
def bassline_quiz():
    questions = [
        {"question": "What is the main job of a bassline?", "answer": "Support the harmony and pulse"},
        {"question": "Which chord tone is most useful for grounding the harmony?", "answer": "Root"},
        {"question": "What does a walking bassline mostly do?", "answer": "Move smoothly through chord tones with a stepwise motion"},
        {"question": "Why are passing notes useful in a bassline?", "answer": "They smooth the motion between chord tones"},
        {"question": "What should a bassline do in relation to the drums?", "answer": "Lock into the beat and support the groove"},
    ]
    run_quiz("🪕 Bassline Quiz 🪕", questions)

# Melody quiz.
def melody_quiz():
    questions = [
        {"question": "What makes a melody memorable?", "answer": "A clear contour and singable shape"},
        {"question": "What is an important melodic idea to build around?", "answer": "A phrase with a rise, peak, and release"},
        {"question": "What do good melodies often use to feel stable?", "answer": "Chord tones and tonic notes"},
        {"question": "Why is repetition useful in a melody?", "answer": "It makes the tune easy to remember"},
        {"question": "What should a melody do in relation to the harmony?", "answer": "Support it while staying memorable and singable"},
    ]
    run_quiz("🎼 Melody Quiz 🎼", questions)

# Genre analysis quiz.
def genre_analysis_quiz():
    questions = [
        {"question": "What is the first thing to analyse in a genre?", "answer": "Rhythm and metre"},
        {"question": "What does a walking bassline often suggest?", "answer": "Jazz"},
        {"question": "What is a common clue in blues music?", "answer": "Blue notes and call and response"},
        {"question": "What kind of harmonic language often signals rock?", "answer": "Strong riff and tonic dominant pull"},
        {"question": "What is the main question for genre analysis?", "answer": "What musical choices create the style"},
    ]
    run_quiz("🎵 Genre Analysis Quiz 🎵", questions)

# Walking bassline quiz.
def walking_bassline_quiz():
    questions = [
        {"question": "What is a walking bassline?", "answer": "A smooth bassline that moves through chord tones with a steady pulse"},
        {"question": "What is a common note choice in a walking line?", "answer": "Root, third, fifth, and seventh"},
        {"question": "Why do walking basslines feel like they move forward?", "answer": "Because they use stepwise motion and a steady beat"},
        {"question": "What do good walking lines try to preserve?", "answer": "Smooth voice-leading and harmonic clarity"},
        {"question": "What style is a walking bassline especially associated with?", "answer": "Jazz"},
    ]
    run_quiz("🚶 Walking Bassline Quiz 🚶", questions)

# Songwriting quiz.
def songwriting_quiz():
    questions = [
        {"question": "What is the best place to start when writing a song?", "answer": "With the emotional core and the song's intention"},
        {"question": "Why is it useful to define the role of each instrument in a song?", "answer": "So they support different musical jobs instead of crowding the same idea"},
        {"question": "What is the main purpose of a chord progression?", "answer": "To carry the song forward through tension and release"},
        {"question": "What should a lyric do in relation to the melody?", "answer": "Fit the rhythm naturally and reinforce the meaning"},
        {"question": "What are the key qualities of a strong lyric?", "answer": "Meaning, poetry, storytelling, rhythm, sound, shape, and emphasis"},
        {"question": "What is one practical songwriting workflow step?", "answer": "Choose the emotional core, then the key, chords, melody, and lyrics"},
    ]
    run_quiz("🎵 Songwriting Quiz 🎵", questions)

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
        {"question": "Which key is a perfect fifth above C major?", "answer": "G"},
        {"question": "What does transposition mean?", "answer": "Move every note by the same interval while keeping the pattern of relationships intact"},
        {"question": "What are the open strings on a 4-string bass?", "answer": "E A D G"},
        {"question": "What is a riff?", "answer": "A short repeated musical pattern"},
        {"question": "What is the main job of a bassline?", "answer": "Support the harmony and pulse"},
        {"question": "What makes a melody memorable?", "answer": "A clear contour and singable shape"},
        {"question": "What is the first thing to analyse in a genre?", "answer": "Rhythm and metre"},
        {"question": "What is a walking bassline?", "answer": "A smooth bassline that moves through chord tones with a steady pulse"},
        {"question": "What is the best place to start when writing a song?", "answer": "With the emotional core and the song's intention"},
        {"question": "What should a lyric do in relation to the melody?", "answer": "Fit the rhythm naturally and reinforce the meaning"},
        {"question": "Why is it useful to define the role of each instrument in a song?", "answer": "So they support different musical jobs instead of crowding the same idea"},
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
        print("5. Circle of Fifths Quiz")
        print("6. Transposition Quiz")
        print("7. Bass Fretboard Quiz")
        print("8. Riff Quiz")
        print("9. Bassline Quiz")
        print("10. Melody Quiz")
        print("11. Genre Analysis Quiz")
        print("12. Walking Bassline Quiz")
        print("13. Songwriting Quiz")
        print("14. Combined Quiz")
        print("15. Exit")

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
    elif selection in ["5", "circle", "circle_of_fifths", "fifths"]:
        circle_of_fifths_quiz()
    elif selection in ["6", "transpose", "transposition"]:
        transposition_quiz()
    elif selection in ["7", "bassfret", "bass_fretboard", "fretboard", "bass fretboard"]:
        bassfret_quiz()
    elif selection in ["8", "riff", "riffs"]:
        riff_quiz()
    elif selection in ["9", "bassline", "basslines"]:
        bassline_quiz()
    elif selection in ["10", "melody", "melodies"]:
        melody_quiz()
    elif selection in ["11", "genre", "genre analysis", "genre_analysis"]:
        genre_analysis_quiz()
    elif selection in ["12", "walking bassline", "walking_bassline", "walking"]:
        walking_bassline_quiz()
    elif selection in ["13", "songwriting", "song writing", "songwriter"]:
        songwriting_quiz()
    elif selection in ["14", "combined", "all"]:
        combined_quiz()
    elif selection in ["15", "exit", "quit"]:
        print("Returning to the main menu.")
    else:
        print("Unknown choice. Please choose 1-15 or a quiz name.")
        quiz()


__all__ = [
    "normalize_note_sequence", "normalize_number_answer", "answer_is_correct",
    "key_signature_quiz", "scale_quiz", "chord_quiz", "modes_quiz",
    "circle_of_fifths_quiz", "transposition_quiz", "bassfret_quiz",
    "riff_quiz", "bassline_quiz", "melody_quiz", "genre_analysis_quiz",
    "walking_bassline_quiz", "songwriting_quiz", "combined_quiz", "quiz"
]
