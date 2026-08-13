import unittest
from unittest import mock

from tonal import quiz


class QuizUpdateTests(unittest.TestCase):
    def test_all_topic_quizzes_and_combined_quiz_run(self):
        answers = iter([
            # key_signature_quiz
            "4",
            "F# C# G#",
            "F C G D A E B",
            "2",
            "B♭ E♭ A♭",
            "B E A D G C F",
            "Father Charles Goes Down And Ends Battle",
            "C",
            "1",
            # scale_quiz
            "G A B C D E F#",
            "C D E F G A B",
            "W W H W W W H",
            "A B C D E F G",
            "E minor",
            "D E F# G A B C#",
            # chord_quiz
            "G B D",
            "C E G",
            "F A C",
            "A C E",
            "D F# A",
            "1",
            # modes_quiz
            "Dorian",
            "Aeolian",
            "Minor",
            "Lydian",
            "Locrian",
            "Mixolydian",
            # circle_of_fifths_quiz
            "G",
            "F",
            "C G D A E B F# C#",
            "C F B♭ E♭ A♭ D♭ G♭ C♭",
            "One sharp",
            "One flat",
            # transposition_quiz
            "Move every note by the same interval while keeping the pattern of relationships intact",
            "Perfect fifth",
            "The interval pattern and musical shape",
            "The tonal centre and key signature",
            "To suit range, instrument, or comfortable key",
            "They remain the same, just at a new pitch level",
            # bassfret_quiz
            "E A D G",
            "5",
            "7",
            "12th fret",
            "They give easy anchor points for navigation and chord tones",
            "The shape of the fretboard and repeated note relationships",
            # riff_quiz
            "A short repeated musical pattern",
            "Rhythm, repetition, and a strong melodic shape",
            "A simple rhythmic idea and a target chord",
            "It helps the listener remember the phrase and lock into the groove",
            "G",
            # bassline_quiz
            "Support the harmony and pulse",
            "Root",
            "Move smoothly through chord tones with a stepwise motion",
            "They smooth the motion between chord tones",
            "Lock into the beat and support the groove",
            # melody_quiz
            "A clear contour and singable shape",
            "A phrase with a rise, peak, and release",
            "Chord tones and tonic notes",
            "It makes the tune easy to remember",
            "Support it while staying memorable and singable",
            # genre_analysis_quiz
            "Rhythm and metre",
            "Jazz",
            "Blue notes and call and response",
            "Strong riff and tonic dominant pull",
            "What musical choices create the style",
            # walking_bassline_quiz
            "A smooth bassline that moves through chord tones with a steady pulse",
            "Root, third, fifth, and seventh",
            "Because they use stepwise motion and a steady beat",
            "Smooth voice-leading and harmonic clarity",
            "Jazz",
            # combined_quiz
            "4",
            "G A B C D E F#",
            "G B D",
            "Dorian",
            "E minor",
            "B E A D G C F",
            "Aeolian",
            "G",
            "Move every note by the same interval while keeping the pattern of relationships intact",
            "E A D G",
            "A short repeated musical pattern",
            "Support the harmony and pulse",
            "A clear contour and singable shape",
            "Rhythm and metre",
            "A smooth bassline that moves through chord tones with a steady pulse",
        ])

        with mock.patch("builtins.input", side_effect=lambda *args, **kwargs: next(answers)):
            quiz.key_signature_quiz()
            quiz.scale_quiz()
            quiz.chord_quiz()
            quiz.modes_quiz()
            quiz.circle_of_fifths_quiz()
            quiz.transposition_quiz()
            quiz.bassfret_quiz()
            quiz.riff_quiz()
            quiz.bassline_quiz()
            quiz.melody_quiz()
            quiz.genre_analysis_quiz()
            quiz.walking_bassline_quiz()
            quiz.combined_quiz()


if __name__ == "__main__":
    unittest.main()
