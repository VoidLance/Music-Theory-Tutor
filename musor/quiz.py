import random
import re

from .data import key_signature_staff, normalize_key_name

# This is the quiz side of the app.
# It keeps the learning practical by checking the answers in a flexible way, so the user can type variations that still mean the same thing.
# It also suits the broader project aim: a learning tool that can become more general over time, rather than being locked into one very narrow function.


def normalize_note_sequence(answer: str):
    text = answer.strip().lower().replace("♭", "b").replace("♯", "#").replace("ﬂ", "b")
    text = text.replace(",", " ").replace("-", " ").replace("/", " ").replace("(", " ").replace(")", " ")

    text = re.sub(r"(?i)([a-g])\s*(?:sharp|sharps?)", r"\1#", text)
    text = re.sub(r"(?i)([a-g])\s*(?:flat|flats?)", r"\1b", text)
    text = text.replace("sharp", " # ").replace("sharps", " # ")
    text = text.replace("flat", " b ").replace("flats", " b ")

    tokens = []
    for raw_token in re.split(r"[^a-g#b]+", text):
        token = raw_token.strip()
        if re.fullmatch(r"[a-g](?:#|b)?", token):
            tokens.append(token)

    return " ".join(tokens)


def normalize_scale_pattern(answer: str):
    text = answer.strip().lower().replace("whole", "w").replace("tone", "w").replace("half", "h").replace("semitone", "h")
    text = re.sub(r"[^wh\s]", " ", text)
    return "".join(ch for ch in text if ch in "wh").upper()


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
    if user_answer is None or not user_answer.strip():
        return False

    question_text = question_text.lower()

    if "how many" in question_text:
        return normalize_number_answer(user_answer) == normalize_number_answer(expected_answer)

    if "mnemonic" in question_text:
        normalized_user = " ".join(re.sub(r"[^a-z]", " ", user_answer.lower()).split())
        normalized_expected = " ".join(re.sub(r"[^a-z]", " ", expected_answer.lower()).split())
        return normalized_user == normalized_expected

    if "pattern" in question_text and "scale" in question_text:
        return normalize_scale_pattern(user_answer) == normalize_scale_pattern(expected_answer)

    if "key" in question_text or "relative major" in question_text or "relative minor" in question_text:
        normalized_user = normalize_key_name(user_answer)
        normalized_expected = normalize_key_name(expected_answer)
        return normalized_user == normalized_expected

    normalized_user = normalize_note_sequence(user_answer)
    normalized_expected = normalize_note_sequence(expected_answer)
    return normalized_user == normalized_expected


def select_quiz_questions(questions: list, max_questions: int = 10):
    if not questions:
        return []

    if len(questions) <= max_questions:
        return list(questions)

    return random.sample(questions, max_questions)


# Run a generic quiz from a list of question/answer pairs.
def run_quiz(title: str, questions: list):
    selected_questions = select_quiz_questions(questions)
    score = 0
    print(title)
    print(f"Answer {len(selected_questions)} random questions from {len(questions)} available.")
    print("Press enter to continue after each answer.")

    for question in selected_questions:
        if question.get("diagram_key"):
            print(f"\n{key_signature_staff(question['diagram_key'], include_label=False)}")

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

    print(f"\nYour score: {score}/{len(selected_questions)}")
    if score == len(selected_questions):
        print("Excellent work!")
    elif score >= len(selected_questions) // 2:
        print("Good effort. Keep practising.")
    else:
        print("Keep going. Repetition is the key to building confidence.")

# Create function to run a simple key signature quiz.
def key_signature_quiz():
    questions = [
        {"question": "Which key is shown on the staff?", "answer": "E major", "diagram_key": "E major"},
        {"question": "Which key is shown on the staff?", "answer": "A major", "diagram_key": "A major"},
        {"question": "Which key is shown on the staff?", "answer": "B♭ major", "diagram_key": "B♭ major"},
        {"question": "Which key is shown on the staff?", "answer": "F major", "diagram_key": "F major"},
        {"question": "Which key is shown on the staff?", "answer": "G major", "diagram_key": "G major"},
        {"question": "Which key is shown on the staff?", "answer": "D major", "diagram_key": "D major"},
        {"question": "Which key is shown on the staff?", "answer": "E♭ major", "diagram_key": "E♭ major"},
        {"question": "Which key is shown on the staff?", "answer": "A♭ major", "diagram_key": "A♭ major"},
        {"question": "Which key is shown on the staff?", "answer": "C major", "diagram_key": "C major"},
        {"question": "Which key is shown on the staff?", "answer": "B major", "diagram_key": "B major"},
        {"question": "Which key is shown on the staff?", "answer": "D♭ major", "diagram_key": "D♭ major"},
        {"question": "Which key is shown on the staff?", "answer": "G minor", "diagram_key": "G minor"},
        {"question": "Which key is shown on the staff?", "answer": "C# minor", "diagram_key": "C# minor"},
        {"question": "How many sharps are in E major?", "answer": "4"},
        {"question": "How many sharps are in D major?", "answer": "2"},
        {"question": "How many flats are in B♭ major?", "answer": "2"},
        {"question": "How many flats are in E♭ major?", "answer": "3"},
        {"question": "Which notes are sharp in A major?", "answer": "F# C# G#"},
        {"question": "Which notes are flat in A♭ major?", "answer": "B♭ E♭ A♭ D♭ G♭"},
        {"question": "Which notes are flat in B♭ major?", "answer": "B♭ E♭"},
        {"question": "What is the order of sharps?", "answer": "F C G D A E B"},
        {"question": "What is the order of flats?", "answer": "B E A D G C F"},
        {"question": "What is the mnemonic to remember the order of sharps?", "answer": "Father Charles Goes Down And Ends Battle"},
        {"question": "What is the relative major key for A minor?", "answer": "C"},
        {"question": "What is the relative major of E minor?", "answer": "G"},
        {"question": "What is the relative minor of C major?", "answer": "A minor"},
        {"question": "What is the relative minor of B♭ major?", "answer": "G minor"},
        {"question": "How many sharps are in E minor?", "answer": "1"},
        {"question": "How many flats are in F major?", "answer": "1"},
    ]

    run_quiz("♯ Key Signature Quiz ♯", questions)

def build_scale_quiz_questions():
    return [
        {"question": "What is the G major scale in the sharp-key spelling?", "answer": "G A B C D E F#"},
        {"question": "What is the C major scale in the natural-key spelling?", "answer": "C D E F G A B"},
        {"question": "What is the scale pattern for a major scale?", "answer": "W W H W W W H"},
        {"question": "What is the natural minor scale for A minor in the natural-key spelling?", "answer": "A B C D E F G"},
        {"question": "What is the relative minor of G major in the sharp-key spelling?", "answer": "E minor"},
        {"question": "What is the D major scale in the sharp-key spelling?", "answer": "D E F# G A B C#"},
        {"question": "What is the F major scale in the flat-key spelling?", "answer": "F G A B♭ C D E"},
        {"question": "What is the relative major of D minor in the flat-key spelling?", "answer": "F major"},
        {"question": "What is the A major scale in the sharp-key spelling?", "answer": "A B C# D E F# G#"},
        {"question": "What is the E minor scale in the sharp-key spelling?", "answer": "E F# G A B C D"},
        {"question": "What is the B minor scale in the sharp-key spelling?", "answer": "B C# D E F# G A"},
        {"question": "What is the C minor scale in the flat-key spelling?", "answer": "C D E♭ F G A♭ B♭"},
        {"question": "What is the E major scale in the sharp-key spelling?", "answer": "E F# G# A B C# D#"},
        {"question": "What is the B♭ major scale in the flat-key spelling?", "answer": "B♭ C D E♭ F G A"},
        {"question": "What is the G minor scale in the flat-key spelling?", "answer": "G A B♭ C D E♭ F"},
        {"question": "What is the E♭ major scale in the flat-key spelling?", "answer": "E♭ F G A♭ B♭ C D"},
        {"question": "What is the natural minor scale for E minor in the sharp-key spelling?", "answer": "E F# G A B C D"},
        {"question": "What is the scale pattern for a natural minor scale?", "answer": "W H W W H W W"},
        {"question": "What is the relative major of A minor in the natural-key spelling?", "answer": "C major"},
        {"question": "What is the relative major of G minor in the flat-key spelling?", "answer": "B♭ major"},
    ]

# Scale quiz.
def scale_quiz():
    questions = build_scale_quiz_questions()
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
        {"question": "What is the E minor triad?", "answer": "E G B"},
        {"question": "What is the B diminished triad?", "answer": "B D F"},
        {"question": "What is the F major triad?", "answer": "F A C"},
        {"question": "What are the notes of a C minor triad?", "answer": "C E♭ G"},
        {"question": "What is the interval relationship between the root and fifth of a major triad?", "answer": "Perfect fifth"},
        {"question": "What is the interval relationship between the root and third of a minor triad?", "answer": "Minor third"},
        {"question": "What is the E major triad?", "answer": "E G# B"},
        {"question": "What is the B♭ major triad?", "answer": "B♭ D F"},
        {"question": "What is the D minor triad?", "answer": "D F A"},
        {"question": "What is the E♭ major triad?", "answer": "E♭ G B♭"},
        {"question": "What is the G minor triad?", "answer": "G B♭ D"},
        {"question": "What is the 3rd of A minor?", "answer": "C"},
        {"question": "What is the 5th of D major?", "answer": "A"},
        {"question": "What is the interval between the root and 3rd of a major triad?", "answer": "Major third"},
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
        {"question": "What mode is built on the 1st degree of C major?", "answer": "Ionian"},
        {"question": "What mode is built on the 3rd degree of C major?", "answer": "Phrygian"},
        {"question": "What mode is built on the 5th degree of C major?", "answer": "Mixolydian"},
        {"question": "What mode is built on the 4th degree of C major?", "answer": "Lydian"},
        {"question": "Which mode is often associated with a dark, tense sound?", "answer": "Phrygian"},
        {"question": "Which mode is the natural minor mode?", "answer": "Aeolian"},
        {"question": "What mode is built on the 2nd degree of C major?", "answer": "Dorian"},
        {"question": "What is the 5th mode of C major called?", "answer": "Mixolydian"},
        {"question": "Which mode has the flattened 7th degree?", "answer": "Mixolydian"},
        {"question": "What mode is built on the 7th degree of C major?", "answer": "Locrian"},
        {"question": "What mode is often associated with a mysterious, tense colour?", "answer": "Phrygian"},
        {"question": "What is the quality of Aeolian?", "answer": "Minor"},
        {"question": "What mode is built on the 1st degree of G major?", "answer": "G Ionian"},
        {"question": "What is the 6th mode of C major called?", "answer": "Aeolian"},
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
        {"question": "Which key has 2 sharps?", "answer": "D major"},
        {"question": "Which key has 3 flats?", "answer": "E♭ major"},
        {"question": "Which key is a perfect fourth above C major?", "answer": "F"},
        {"question": "Which key is a perfect fourth below C major?", "answer": "G"},
        {"question": "What key signature is one step clockwise from G major?", "answer": "D major"},
        {"question": "What key signature is one step counterclockwise from C major?", "answer": "F major"},
        {"question": "Which key is a perfect fifth above G major?", "answer": "D major"},
        {"question": "Which key is a perfect fifth above D major?", "answer": "A major"},
        {"question": "Which key is a perfect fifth below F major?", "answer": "B♭ major"},
        {"question": "Which key has 1 sharp?", "answer": "G major"},
        {"question": "Which key has 1 flat?", "answer": "F major"},
        {"question": "Which key is a perfect fifth below B♭ major?", "answer": "E♭ major"},
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
        {"question": "What is the effect of transposition on rhythm?", "answer": "It stays the same"},
        {"question": "If a melody is transposed up a major third, what happens to the harmony?", "answer": "The harmony also moves up by a major third"},
        {"question": "Which musical element is preserved in transposition?", "answer": "The intervallic relationships"},
        {"question": "What is a typical reason to transpose for a vocalist?", "answer": "To match their comfortable singing range"},
        {"question": "What is a common musical effect of transposition?", "answer": "A different tonal centre with the same melodic shape"},
        {"question": "What remains unchanged when you transpose a motif?", "answer": "Its relative contour and interval pattern"},
        {"question": "If you transpose C major up a whole step, what key do you get?", "answer": "D major"},
        {"question": "If you transpose A minor down a minor third, what key do you get?", "answer": "F major"},
        {"question": "What stays the same when a melody is transposed to another key?", "answer": "Its interval pattern"},
        {"question": "What usually changes in the notation when transposing?", "answer": "The written key signature"},
        {"question": "Why might a band transpose a song for a singer?", "answer": "To keep the melody comfortable to sing"},
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
        {"question": "What note is on the 1st fret of the G string?", "answer": "G#"},
        {"question": "What note is on the 3rd fret of the A string?", "answer": "C"},
        {"question": "What is the note name pattern in each octave on a bass?", "answer": "ABCDEFG"},
        {"question": "Why is the 12th fret a natural landmark?", "answer": "Because the note names repeat an octave higher"},
        {"question": "What is the best way to navigate the bass neck quickly?", "answer": "Use octave shapes and fret landmarks"},
        {"question": "What does a 5th fret move between adjacent strings usually represent?", "answer": "The same note name in a different octave"},
        {"question": "What note is on the 2nd fret of the D string?", "answer": "E"},
        {"question": "What note is on the 4th fret of the A string?", "answer": "C"},
        {"question": "What note is on the 7th fret of the E string?", "answer": "F"},
        {"question": "What note is on the 5th fret of the G string?", "answer": "C"},
        {"question": "What is the relationship between the 5th fret and the next string open?", "answer": "They are the same pitch"},
        {"question": "Why does the bass note pattern repeat at the 12th fret?", "answer": "Because it is one octave higher"},
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
        {"question": "What does a strong riff often reinforce?", "answer": "The song's pulse and harmony"},
        {"question": "How can a riff feel more interesting without becoming too busy?", "answer": "By varying rhythm or accent patterns within a simple shape"},
        {"question": "What is a common ingredient in a memorable riff?", "answer": "A catchy repeated rhythmic hook"},
        {"question": "Why are chord tones useful in a riff?", "answer": "They make the riff feel connected to the harmony"},
        {"question": "What should a riff do in a song?", "answer": "Support the groove and anchor the section"},
        {"question": "What element gives a riff identity?", "answer": "Its melodic contour and rhythmic accent"},
        {"question": "What is a good goal for a riff start?", "answer": "Keep it singable and easy to repeat"},
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
        {"question": "What is a stable bass note for a C major chord?", "answer": "C"},
        {"question": "Why is a root note so effective in a bassline?", "answer": "It clearly defines the harmony"},
        {"question": "What kind of motion often sounds most musical in bass?", "answer": "Stepwise motion"},
        {"question": "Why do basslines often emphasize beats 1 and 3?", "answer": "To reinforce the rhythmic drive of the song"},
        {"question": "What makes a bassline feel strong and confident?", "answer": "A clear connection to the chord progression and pulse"},
        {"question": "What should a bassline avoid doing?", "answer": "Overcomplicating the harmony or fighting the drums"},
        {"question": "What is a common bass note choice for a V chord?", "answer": "The root"},
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
        {"question": "What is a phrase arch?", "answer": "A musical shape that rises and falls over a phrase"},
        {"question": "Why are repeated motifs useful?", "answer": "They create recognition and unity"},
        {"question": "What kind of notes often create a strong melodic centre?", "answer": "Tonic notes"},
        {"question": "What helps a melody feel like it has direction?", "answer": "A clear contour with tension and release"},
        {"question": "What is often the easiest melodic material to sing?", "answer": "Stepwise motion with a memorable contour"},
        {"question": "What should a melody do with the lyric?", "answer": "Fit the rhythm naturally"},
        {"question": "Why should a melody avoid being too busy?", "answer": "So the listener can remember it"},
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
        {"question": "What feature is often associated with reggae?", "answer": "Offbeat accents and a laid-back groove"},
        {"question": "What is a common clue in funk?", "answer": "Syncopation and a strong bassline"},
        {"question": "What style commonly uses complex harmonies and extended chords?", "answer": "Jazz"},
        {"question": "What musical feature often suggests a march?", "answer": "A strong, steady duple pulse"},
        {"question": "What is often a strong clue that a piece belongs to pop?", "answer": "A memorable hook and simple repeated sections"},
        {"question": "What does genre analysis aim to identify?", "answer": "The musical language that defines a style"},
        {"question": "What is a common clue in electronic dance music?", "answer": "A consistent, driving beat and repeated loops"},
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
        {"question": "Why are passing tones useful in walking basslines?", "answer": "They smooth the harmonic motion"},
        {"question": "What does a walking bassline usually emphasize?", "answer": "The pulse and chord changes"},
        {"question": "What note is often used to connect chord roots in a walking line?", "answer": "The 5th or 7th"},
        {"question": "How does a walking bassline support harmony?", "answer": "By outlining each chord with clear stepwise movement"},
        {"question": "What should a walking line avoid?", "answer": "Overly random or disconnected motion"},
        {"question": "What is one beneficial quality of a walking bassline?", "answer": "It gives the music forward momentum"},
        {"question": "What does a walking line often build around?", "answer": "The steady beat and chord progression"},
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
        {"question": "What does a strong song usually need before the details?", "answer": "A clear concept and direction"},
        {"question": "Why is a song's emotional core important?", "answer": "It gives the material identity and meaning"},
        {"question": "What should the melody do with the lyric's phrasing?", "answer": "Support the natural speech rhythm"},
        {"question": "What helps a chord progression feel like it moves forward?", "answer": "Tension and release across the phrase"},
        {"question": "What is a useful reason to revise a song section?", "answer": "To make each part do a clearer musical job"},
        {"question": "What is often the strongest way to begin a song idea?", "answer": "From a strong emotional or lyrical hook"},
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
        {"question": "What is the order of sharps?", "answer": "F C G D A E B"},
        {"question": "What is the 4th mode of C major?", "answer": "Lydian"},
        {"question": "What is the relative major of D minor?", "answer": "F major"},
        {"question": "Which key is a perfect fifth below C major?", "answer": "F"},
        {"question": "What does a walking bassline often emphasize?", "answer": "The pulse and chord changes"},
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
    "select_quiz_questions", "build_scale_quiz_questions", "key_signature_quiz", "scale_quiz", "chord_quiz", "modes_quiz",
    "circle_of_fifths_quiz", "transposition_quiz", "bassfret_quiz",
    "riff_quiz", "bassline_quiz", "melody_quiz", "genre_analysis_quiz",
    "walking_bassline_quiz", "songwriting_quiz", "combined_quiz", "quiz"
]
