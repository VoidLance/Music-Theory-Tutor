import re

# This is a python terminal script to help with learning music theory. I've already learned quite a bit by making it, so it serves two purposes:
# To practice making a python app and show a familiarity with the features of Python I use here
# And to actually help me learn music theory (and of course anyone else who uses it)
# It's also part of a broader project I want to keep expanding as I learn more about music theory, arranging, and the practical concerns of bass guitar and cello.

# Setup sharp order array
orderSharps = ["F", "C", "G", "D", "A", "E", "B"]
mnemonicSharps = ["Father", "Charles", "Goes", "Down", "And", "Ends", "Battle"]

# Setup flat order array
orderFlats = ["B", "E", "A", "D", "G", "C", "F"]
mnemonicFlats = ["Battle", "Ends", "And", "Down", "Goes", "Charles'", "Father"]

# Setup key order array.
# In the usual practical teaching sequence, the standard circle stops at 6 sharps / 6 flats,
# because the 7-sharp and 7-flat keys are enharmonic duplicates of C# and C♭ and are not typically listed in beginner key charts.
sharpKeys = ["C maj (0)", "G maj (1)", "D maj (2)", "A maj (3)", "E maj (4)", "B major (5)", "F# maj (6)"]
flatKeys = ["C maj (0)", "F maj (1)", "B♭ maj (2)", "E♭ maj (3)", "A♭ maj (4)", "D♭ maj (5)", "G♭ maj (6)"]
minorKeys = ["A min (0)", "E min (1)", "B min (2)", "F# min (3)", "C# min (4)", "G# min (5)", "D# min (6)", "D min (1)", "G min (2)", "C min (3)", "F min (4)", "B♭ min (5)", "E♭ min (6)"]

# Setup major key signature map so a specific key can be selected by name
keySignatureMap = {
    "C": {"accidentals": 0, "type": "none"},
    "G": {"accidentals": 1, "type": "sharp"},
    "D": {"accidentals": 2, "type": "sharp"},
    "A": {"accidentals": 3, "type": "sharp"},
    "E": {"accidentals": 4, "type": "sharp"},
    "B": {"accidentals": 5, "type": "sharp"},
    "F#": {"accidentals": 6, "type": "sharp"},
    "C#": {"accidentals": 7, "type": "sharp"},
    "F": {"accidentals": 1, "type": "flat"},
    "B♭": {"accidentals": 2, "type": "flat"},
    "E♭": {"accidentals": 3, "type": "flat"},
    "A♭": {"accidentals": 4, "type": "flat"},
    "D♭": {"accidentals": 5, "type": "flat"},
    "G♭": {"accidentals": 6, "type": "flat"},
    "C♭": {"accidentals": 7, "type": "flat"},
}

minorKeySignatureMap = {
    "A": {"accidentals": 0, "type": "none"},
    "E": {"accidentals": 1, "type": "sharp"},
    "B": {"accidentals": 2, "type": "sharp"},
    "F#": {"accidentals": 3, "type": "sharp"},
    "C#": {"accidentals": 4, "type": "sharp"},
    "G#": {"accidentals": 5, "type": "sharp"},
    "D#": {"accidentals": 6, "type": "sharp"},
    "A#": {"accidentals": 7, "type": "sharp"},
    "D": {"accidentals": 1, "type": "flat"},
    "G": {"accidentals": 2, "type": "flat"},
    "C": {"accidentals": 3, "type": "flat"},
    "F": {"accidentals": 4, "type": "flat"},
    "B♭": {"accidentals": 5, "type": "flat"},
    "E♭": {"accidentals": 6, "type": "flat"},
    "A♭": {"accidentals": 7, "type": "flat"},
}

# Create function to display the entire sharp order and include a reminder of the mnemonic to remember it
# This is the first thing a beginner usually learns, because it helps explain key signatures and accidentals before anything more complex.
def sharp_order():
    print(f"♯ The order of sharps is: ♯\n{' --> '.join(orderSharps)}\n\nThe mnemonic to remember this is:\n'{' '.join(mnemonicSharps)}'\n\nOr simply 'Bead G C F in reverse'\n\nTie this to sharps with:\n'Ends battle sharply' and\n'Beads are not sharp'\n\n")

# Create function to display the entire flat order and include a reminder of the mnemonic to remember it
# This is the opposite pattern and helps explain why flat keys are grouped in a different way.
def flat_order():
    print(f"♭ The order of flats is the reverse of sharps: ♭\n{' --> '.join(orderFlats)}\n\nThe mnemonic to remember this is:\n'{' '.join(mnemonicFlats)}'\n\nOr simply 'Bead GCF'\n\nTie this to flats with:\n'Death lands flatly' and\n'Beads can be flat'\n\n")

# Create function to list the sharp keys in order of number of sharps
# This follows the same pattern as the order of sharps, but shows the key names instead of the accidentals alone.
def sharp_keys():
    print(f"♯ Sharp keys: ♯\n{'\n'.join(sharpKeys)}\nThis is the same order as the sharps inside the key signature, except it starts and ends at C.\nOnly the F and the high C keys are sharp keys. In other words, only F is sharp, and C is natural.\n\n")

# Create function to list the flat keys in order of number of flats
# This mirrors the sharp-key section and helps beginners see the relationship between the key signature and the key name.
def flat_keys():
    print(f"♭ Flat keys: ♭\n{'\n'.join(flatKeys)}\nThis is the same order as the flats inside the key signature, except it starts at C.\nEvery flat key is flat except F and C. In other words, every key except F is flat, and C is natural.\n\n")

# Create function to display all information about key signatures
# This is the combined reference section when the user wants the whole picture in one place.
def keys():
    sharp_order()
    flat_order()
    sharp_keys()
    flat_keys()
    minor_keys()

# Create a practical scale-builder so the user can turn any key signature into the actual notes of the scale.
def scale_from_key(key_name: str):
    text = key_name.strip()
    normalized = normalize_key_name(text)
    is_minor = "minor" in text.lower() or text.strip().lower().endswith("m") or text.strip().lower().endswith("min")

    major_scale_map = {
        "C": ["C", "D", "E", "F", "G", "A", "B", "C"],
        "G": ["G", "A", "B", "C", "D", "E", "F#", "G"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#", "D"],
        "A": ["A", "B", "C#", "D", "E", "F#", "G#", "A"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#", "E"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A#", "B"],
        "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"],
        "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#", "C#"],
        "F": ["F", "G", "A", "B♭", "C", "D", "E", "F"],
        "B♭": ["B♭", "C", "D", "E♭", "F", "G", "A", "B♭"],
        "E♭": ["E♭", "F", "G", "A♭", "B♭", "C", "D", "E♭"],
        "A♭": ["A♭", "B♭", "C", "D♭", "E♭", "F", "G", "A♭"],
        "D♭": ["D♭", "E♭", "F", "G♭", "A♭", "B♭", "C", "D♭"],
        "G♭": ["G♭", "A♭", "B♭", "C♭", "D♭", "E♭", "F", "G♭"],
        "C♭": ["C♭", "D♭", "E♭", "F♭", "G♭", "A♭", "B♭", "C♭"],
    }

    minor_scale_map = {
        "A": ["A", "B", "C", "D", "E", "F", "G", "A"],
        "E": ["E", "F#", "G", "A", "B", "C", "D", "E"],
        "B": ["B", "C#", "D", "E", "F#", "G", "A", "B"],
        "F#": ["F#", "G#", "A", "B", "C#", "D", "E", "F#"],
        "C#": ["C#", "D#", "E", "F#", "G#", "A", "B", "C#"],
        "G#": ["G#", "A#", "B", "C#", "D#", "E", "F#", "G#"],
        "D#": ["D#", "E#", "F#", "G#", "A#", "B", "C#", "D#"],
        "A#": ["A#", "B#", "C#", "D#", "E#", "F#", "G#", "A#"],
        "D": ["D", "E", "F", "G", "A", "B♭", "C", "D"],
        "G": ["G", "A", "B♭", "C", "D", "E♭", "F", "G"],
        "C": ["C", "D", "E♭", "F", "G", "A♭", "B♭", "C"],
        "F": ["F", "G", "A♭", "B♭", "C", "D♭", "E♭", "F"],
        "B♭": ["B♭", "C", "D♭", "E♭", "F", "G♭", "A♭", "B♭"],
        "E♭": ["E♭", "F", "G♭", "A♭", "B♭", "C♭", "D♭", "E♭"],
        "A♭": ["A♭", "B♭", "C♭", "D♭", "E♭", "F♭", "G♭", "A♭"],
    }

    scale_map = major_scale_map if not is_minor else minor_scale_map
    key_name_clean = normalized

    if key_name_clean not in scale_map:
        print(f"Unknown key: {key_name}")
        available = ", ".join(sorted(scale_map.keys()))
        print("Try one of:", available)
        return

    scale = scale_map[key_name_clean]
    scale_label = "minor" if is_minor else "major"
    print(f"{key_name_clean} {scale_label}")
    print("How to build it:")
    print("1. Pick the root note of the key.")
    print("2. Use the key signature to know which notes are altered.")
    print("3. Move step by step through the scale, keeping the correct pattern of tones and semitones.")
    if not is_minor:
        print("4. For a major scale, the formula is: tone, tone, semitone, tone, tone, tone, semitone.")
        print("5. Apply that pattern to the root note and keep the accidentals required by the key.")
    else:
        print("4. For natural minor, the formula is: tone, semitone, tone, tone, semitone, tone, tone.")
        print("5. Use the relative major to identify the same key signature, then build the minor pattern from the minor root.")
    print(f"Scale: {' '.join(scale)}")
    print("Example: G major uses F# because the key signature contains one sharp, so the scale is G A B C D E F# G.")

# Generic scales guide.
def scales_overview():
    print("Scales")
    print("=====")
    print("A scale is a sequence of notes built from a key in order.")
    print("To build a scale, start with the key note and then follow the scale pattern.")
    print("For a major scale, the formula is: tone, tone, semitone, tone, tone, tone, semitone.")
    print("For a natural minor scale, the formula is: tone, semitone, tone, tone, semitone, tone, tone.")
    print("Before you build the notes, check the key signature so you know which notes are sharp or flat.")
    print("Example: G major has one sharp, so the scale is G A B C D E F# G.")
    print("Example: A minor has no sharps or flats, so the natural minor scale is A B C D E F G A.")

# Create a function to teach how to build a triad chord from a major key.
def chord_from_key(key_name: str):
    normalized = normalize_key_name(key_name)
    major_scale_map = {
        "C": ["C", "D", "E", "F", "G", "A", "B"],
        "G": ["G", "A", "B", "C", "D", "E", "F#"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#"],
        "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
        "F": ["F", "G", "A", "B♭", "C", "D", "E"],
        "B♭": ["B♭", "C", "D", "E♭", "F", "G", "A"],
        "E♭": ["E♭", "F", "G", "A♭", "B♭", "C", "D"],
        "A♭": ["A♭", "B♭", "C", "D♭", "E♭", "F", "G"],
        "D♭": ["D♭", "E♭", "F", "G♭", "A♭", "B♭", "C"],
        "G♭": ["G♭", "A♭", "B♭", "C♭", "D♭", "E♭", "F"],
    }

    if normalized not in major_scale_map:
        print(f"Unknown key: {key_name}")
        return

    scale = major_scale_map[normalized]
    root = scale[0]
    third = scale[2]
    fifth = scale[4]
    chord = [root, third, fifth]

    print(f"{normalized} major")
    print("How to build it:")
    print("1. Use the major scale for the key.")
    print("2. Pick the 1st, 3rd, and 5th notes of that scale.")
    print("3. Stack them together to make a triad.")
    print(f"Scale in {normalized} major: {' '.join(scale)}")
    print(f"1st = {root}")
    print(f"3rd = {third}")
    print(f"5th = {fifth}")
    print(f"Chord: {' '.join(chord)}")
    print(f"This gives the {root} major triad: {root} {third} {fifth}.")

# Generic chords guide.
def chords_overview():
    print("Chords")
    print("======")
    print("A chord is built from notes in the scale.")
    print("The simplest chord is a triad, built from the 1st, 3rd, and 5th degrees of the scale.")
    print("For example, in G major the notes are G A B C D E F#. The 1st, 3rd, and 5th are G B D.")
    print("So the G major triad is G B D.")
    print("The quality of the triad changes depending on the 3rd: major, minor, or diminished.")

# Create a feature to show the major modes built from a key.
def modes_from_key(key_name: str):
    normalized = normalize_key_name(key_name)
    major_scale_map = {
        "C": ["C", "D", "E", "F", "G", "A", "B"],
        "G": ["G", "A", "B", "C", "D", "E", "F#"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#"],
        "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
        "F": ["F", "G", "A", "B♭", "C", "D", "E"],
        "B♭": ["B♭", "C", "D", "E♭", "F", "G", "A"],
        "E♭": ["E♭", "F", "G", "A♭", "B♭", "C", "D"],
        "A♭": ["A♭", "B♭", "C", "D♭", "E♭", "F", "G"],
        "D♭": ["D♭", "E♭", "F", "G♭", "A♭", "B♭", "C"],
        "G♭": ["G♭", "A♭", "B♭", "C♭", "D♭", "E♭", "F"],
    }

    if normalized not in major_scale_map:
        print(f"Unknown key: {key_name}")
        return

    scale = major_scale_map[normalized]
    mode_details = [
        ("Ionian", "1st", "Major", "bright, stable, resolved"),
        ("Dorian", "2nd", "Minor", "soulful, smooth, wistful"),
        ("Phrygian", "3rd", "Minor", "dark, tense, exotic"),
        ("Lydian", "4th", "Major", "airy, bright, dreamy"),
        ("Mixolydian", "5th", "Major", "bluesy, relaxed, upbeat"),
        ("Aeolian", "6th", "Minor", "melancholic, reflective, natural minor"),
        ("Locrian", "7th", "Diminished", "tense, unstable, dark"),
    ]
    modes = []
    for i in range(len(scale)):
        rotated = scale[i:] + scale[:i]
        name, degree, quality, feeling = mode_details[i]
        modes.append((name, degree, quality, feeling, rotated))

    print(f"Modes of {normalized} major")
    print("How to build them:")
    print("1. Start with the major scale in the key.")
    print("2. Keep the same notes, but begin on a different scale degree.")
    print("3. Each new starting note creates a different mode with a different tonal colour.")
    print(f"Major scale: {' '.join(scale)}")
    for name, degree, quality, feeling, notes in modes:
        print(f"{name} ({quality} mode, starts on {degree} degree): {' '.join(notes)} — {feeling}")
    print("Example: C major = C D E F G A B C. Rotate that pattern to build D Dorian, E Phrygian, F Lydian, G Mixolydian, A Aeolian, and B Locrian.")
    print("These modes are not just different starting points; each one has a characteristic major/minor/diminished quality and a different emotional colour.")

# Generic modes guide.
def modes_overview():
    print("Modes")
    print("=====")
    print("Modes are the same notes as a major scale, but they start on a different degree.")
    print("Each mode keeps the same parent scale, yet it changes the tonal centre, quality, and emotional character.")
    print("Take C major: C D E F G A B. If you start on D, you get D Dorian.")
    print("If you start on E, you get E Phrygian.")
    print("This is why the modes are all related to one parent scale while still feeling different.")
    print("")
    print("The seven modes and their qualities:")
    print("- Ionian: Major mode, bright, stable, resolved")
    print("- Dorian: Minor mode, soulful, smooth, wistful")
    print("- Phrygian: Minor mode, dark, tense, exotic")
    print("- Lydian: Major mode, airy, bright, dreamy")
    print("- Mixolydian: Major mode, bluesy, relaxed, upbeat")
    print("- Aeolian: Minor mode, melancholic, reflective, natural minor")
    print("- Locrian: Diminished mode, tense, unstable, dark")
    print("")
    print("A quick way to remember them:")
    print("- Major-sounding modes: Ionian, Lydian, Mixolydian")
    print("- Minor-sounding modes: Dorian, Phrygian, Aeolian")
    print("- Darkest, most tense mode: Locrian")

# Generic scale/chord/mode entry pages for the app.
def scales_page():
    scales_overview()

def chords_page():
    chords_overview()

def modes_page():
    modes_overview()

# Practical composition and analysis guides.
def riff_guide():
    print("Riffs")
    print("=====")
    print("A riff is usually a short repeated pattern that gives a piece its identity.")
    print("To build a riff, start with a simple rhythmic idea, then choose notes that fit the chord or key.")
    print("Good riffs are usually easy to remember, repeat cleanly, and support the groove.")
    print("Ask three questions: What chord is it over? What rhythm is it based on? What note or interval makes it memorable?")
    print("A simple riff often uses repetition, a strong rhythmic accent, and a small range so it sits clearly in the groove.")
    print("Example: on a G major chord, a riff might emphasise G, B, and D with a repeated rhythmic pattern that locks to the beat.")


def bassline_guide():
    print("Basslines")
    print("=========")
    print("A bassline should support the harmony and the groove at the same time.")
    print("Its first job is to make the chord progression clear, and its second job is to give the music a pulse that people can feel.")
    print("Start by identifying the harmonic rhythm: are the chords changing every bar, every half bar, or every beat?")
    print("Then decide what the bass is meant to do. Is it driving the groove, outlining the root motion, or creating tension with passing notes?")
    print("The basic building plan is simple:")
    print("1. Start on the root or fifth of the chord on the strongest beats.")
    print("2. Add the third when you want to make the chord quality obvious, especially when the harmony is moving quickly.")
    print("3. Use passing notes between chord tones to create smoother motion, but keep the line easy to hear and follow.")
    print("4. Keep the rhythm consistent with the drums; a bassline is strongest when it locks into the beat rather than fighting it.")
    print("5. Treat the bassline like a phrase, not a random stack of notes: motif, repetition, variation, and final resolution all matter.")
    print("")
    print("Advanced bassline tips")
    print("- Root notes keep the harmony grounded; fifths and octaves create stability without clutter.")
    print("- A 3rd adds colour and tells the ear whether a chord is major or minor.")
    print("- Suspended or passing notes can create motion, but if every note is a passing tone the line loses definition.")
    print("- Use syncopation sparingly: a delayed accent can sound cool, but too much can blur the pulse.")
    print("- Build a phrase with contrast. For example, one bar can place roots on beat 1 and 3, then the next bar can use a more active line with passing tones.")
    print("- When a progression is repeated, change the rhythm or the order of notes slightly rather than reusing the exact same pattern every time.")
    print("- In a bassline, leave room for the melody and harmony. The bass should add weight and direction, not compete with the upper parts.")
    print("- If a line feels weak, test whether the issue is rhythmic placement, harmonic clarity, or lack of note-to-note motion.")
    print("")
    print("Walking basslines")
    print("A walking bassline is a smooth line that keeps moving through the chord tones, usually one note per beat.")
    print("It is often used in jazz, swing, and other styles where the bass creates a feeling of constant forward motion.")
    print("How to build one:")
    print("1. Choose the chord progression and decide how many beats each chord will take.")
    print("2. Write one note per beat, often around a steady quarter-note pulse or a flowing eighth-note pattern.")
    print("3. Move through the chord tones in order: root, 3rd, 5th, and 7th are common choices, with passing tones in between when needed.")
    print("4. Keep the line stepwise when possible, so it feels like a continuous walk rather than a jumpy pattern.")
    print("5. Aim for smooth voice-leading: choose notes that lead naturally into the next chord, not just random notes that happen to fit the key.")
    print("6. Make the bassline support the harmonic movement. The listener should hear the chord changes without the line becoming chaotic.")
    print("A simple walking line over C major can move like this: C - E - G - B | A - C - E - G | F - A - C - E | G - B - D - G")
    print("This works because each note sits in the harmonic space of the chord, and the stepwise motion keeps the line moving.")
    print("For a stronger walking line, pay attention to the line's contour: avoid too many large leaps unless they are part of a deliberate phrase, and make sure the line resolves naturally.")
    print("The best walking basslines feel like a conversation between the harmony and the rhythm section: stable enough to anchor the tune, but active enough to keep the groove moving.")


def melody_guide():
    print("Melody")
    print("======")
    print("A melody should be memorable, singable, and shaped around the harmony.")
    print("Start by choosing a scale or mode that matches the mood of the song. Then pick notes that outline the chord tones and the target note of the phrase.")
    print("A melody usually works best when it has a clear contour: a rise, a peak, and a release.")
    print("Use repetition for familiarity, and variety for interest. Long notes can feel stable, while shorter notes create motion.")
    print("Good melodies often sit around the tonic, dominant, and leading tone, and they usually resolve with a sense of purpose.")


def genre_analysis_guide():
    print("Genre analysis")
    print("==============")
    print("To analyse a genre, listen for the things that create its identity: rhythm, harmony, scale colour, phrasing, and texture.")
    print("Ask what makes it feel the way it does: is it a straight groove, a swung feel, a syncopated accent pattern, or a strong drone?")
    print("Listen for the harmonic language: major, minor, modal, bluesy, or heavily functional.")
    print("Check the rhythm and metre. A song built around a steady pulse, a walking bassline, or a punchy syncopated riff will feel very different.")
    print("Look at the melodic material: are the melodies staying close to the pentatonic scale, rotating through modes, or leaning on chord tones and blue notes?")
    print("Finally, identify the key question: what is the music trying to make you feel? Bright, stable, tense, soulful, dark, relaxed, or adventurous?")
    print("The point is not just to name a genre, but to understand what musical decisions create that genre's characteristic sound.")
    print("")
    print("How to analyse sheet music by genre")
    print("1. Start with the time signature and metre. 4/4, 3/4, 12/8, and compound metres immediately suggest different musical feel and phrase shape.")
    print("2. Mark the accents. Ask where the downbeats fall, whether the music is driven by strong quarter-note pulses or by syncopation and off-beat emphasis.")
    print("3. Look at the rhythmic cell. Short repeated patterns often define a style. For example, a repeated dotted rhythm or a repeated eighth-note figure can create a martial or fanfare feel.")
    print("4. Study the harmonic rhythm. Does the harmony move every bar, every half bar, or only on important cadences? This quickly separates many styles.")
    print("5. Check the scale or mode and identify any accidentals. Blues, folk, modal, and jazz writing all contain very different pitch colour.")
    print("6. Identify the phrase shape. Does the melody stick to short repeated motives, or does it expand into long, singing lines with clear cadences?")
    print("7. Look for genre clues in the patterns. Repeated broken-chord figures often suggest fanfares or ceremonial music, while walking bass support and ii-V-I motion suggest jazz.")
    print("8. Pay attention to cadences and endings. A strong authentic cadence feels final, while a plagal or modal ending feels looser and more folk-like.")
    print("")
    print("Spotting the patterns that create a genre")
    print("A good way to train your ear and eye is to look for recurring musical 'motifs' rather than memorising a whole piece.")
    print("Ask: does this music repeat a rhythmic pattern? Is there a repeated bass motion? Is there a repeated interval or phrase shape? Do the pitches outline a set scale or a broken chord?")
    print("If you can identify one or two repeated cells, you are already hearing the style of the piece.")
    print("For example, a fanfare often uses repetition, strong accents, broad leaps, and a short, punchy rhythmic figure that feels ceremonial or heroic.")
    print("A fanfare may also use a broken-chord pattern such as root-fifth-octave or a repeated rising idea that feels like a call to action.")
    print("Try this exercise: take a sheet of music, circle the repeated rhythmic cells, then circle any motif that appears more than once. Once you track those, you can often tell what kind of piece it is.")
    print("The old lesson I remember is a classic example: a page of fanfare pieces can be reduced to a few repeated pattern habits, and once you recognise those, you can make your own fanfare by building a short phrase from them.")
    print("A beginner fanfare recipe is: choose a strong time signature, write a repeated accent pattern, use a broken-chord or arpeggio idea, then repeat it with slight variation and close with a clear cadence.")
    print("This is how pattern recognition becomes composition: you are not copying a piece, you are learning the grammar of a style.")
    print("")
    print("Genre examples")
    print("- Jazz: walking bass, swung rhythm, extended harmony, ii-V-I movement, strong improvisatory phrase shapes.")
    print("- Blues: repeated phrases, dominant tension, blue notes, call-and-response, and a very clear emotional pull.")
    print("- Rock: strong riff-based repetition, power-chord motion, clear tonic-dominant pull, and memorable hooks.")
    print("- Classical and ceremonial music: balanced phrase lengths, sequence patterns, cadences, and repeated fanfare-like motives.")
    print("- Folk and modal music: fewer harmonic changes, modal colour, repeated melodic cells, and strong connection to a local or dance-like pulse.")
    print("The key idea is that each genre is not just a set of chords or scales; it is a set of patterns working together. Once you can spot those patterns on the page, you can start to understand the style and even write in it.")


def walking_bassline_guide():
    bassline_guide()

# Create a terminal-friendly guide to the circle of fifths.
# It explains how to build the pattern, how to read it, and how key relationships are shown in the circle.
def circle_of_fifths():
    print("Circle of Fifths")
    print("================")
    print("A circle of fifths is a map of key relationships built by moving in perfect fifths.")
    print("Clockwise, each step goes up a perfect fifth: C -> G -> D -> A -> E -> B -> F# -> C#")
    print("Counterclockwise, each step goes down a perfect fifth (or up a perfect fourth): C -> F -> B♭ -> E♭ -> A♭ -> D♭ -> G♭ -> C♭")
    print("")
    print("A rough terminal-style layout looks like this:")
    print("""
                C
  ♭         F       G              #
         B♭            D
       E♭                A
        A♭              E
           D♭         B
               G♭/F#
""")
    print("\nThe flat side is the mirror image of the sharp side. The flats belong on the flat-key names:")
    print("F, B♭, E♭, A♭, D♭, G♭, C♭")
    print("That is why the flat circle moves from C to F to B♭ to E♭ to A♭ to D♭ to G♭ to C♭.")
    print("The sharp side uses the equivalent sharp spellings on the other side of the same ring, such as F# instead of G♭, and C# instead of D♭.")
    print("This is the same pitch relationship expressed in a different spelling, depending on whether you are travelling the sharp side or the flat side.")
    print("\nThis is only a simplified version of the circle. The idea is that each move clockwise adds one sharp,")
    print("and each move counterclockwise adds one flat.")
    print("")
    print("How to draw it yourself:")
    print("1. Start at C. It has 0 sharps and 0 flats.")
    print("2. Move clockwise by a perfect fifth: C to G, then D, A, E, B, F#, C#.")
    print("3. Each step adds one sharp to the key signature.")
    print("4. Move counterclockwise from C: C to F, B♭, E♭, A♭, D♭, G♭, C♭.")
    print("5. Each step adds one flat to the key signature.")
    print("")
    print("How to use it:")
    print("- Closely related keys are next to each other on the circle.")
    print("- Moving one step clockwise changes the key by one sharp.")
    print("- Moving one step counterclockwise changes the key by one flat.")
    print("- A key and its relative minor sit next to each other in the same 'spoke' of the wheel.")
    print("- The relative major is the major key that shares the same key signature as a minor key.")
    print("  Example: C major is related to A minor, G major to E minor, F major to D minor.")
    print("")
    print("Key relationships and tonal distance:")
    print("A close relationship means the keys share many notes and feel very much like the same family.")
    print("Adjacent keys on the circle, such as C and G or F and B♭, are close because they differ by only one accidental and usually sound smooth and familiar.")
    print("The tonal quality of a close relationship is often stable and gentle: bright, resolved, or lightly shifted, rather than dramatically different.")
    print("A medium relationship is a little further away, such as C to D or C to A. These keys still share a strong connection, but the change in harmonic colour is more noticeable and often feels more directional or less home-like.")
    print("A distant relationship means the keys are farther apart on the circle, such as C to F# or C to G♭. These move away from the original key more dramatically, so the tonal quality feels more contrasting, tense, or adventurous.")
    print("In other words, the farther apart the keys are on the circle, the less they share and the more their feel changes: from close, stable, and familiar, to medium, clear, and shifting, to distant, dramatic, and strongly contrasting.")
    print("")
    print("Relative key relationships:")
    print("C major  <-> A minor")
    print("G major  <-> E minor")
    print("D major  <-> B minor")
    print("A major  <-> F# minor")
    print("F major  <-> D minor")
    print("B♭ major <-> G minor")
    print("E♭ major <-> C minor")
    print("A♭ major <-> F minor")
    print("")
    print("A simple memory rule:")
    print("- clockwise = sharp side")
    print("- counterclockwise = flat side")
    print("- the circle shows how keys are connected by fifths, not just by name")
    print("- the closer two keys are on the circle, the more they share notes and feel")
    print("")

# Create function to list the minor keys in order of accidentals
# This is where the learner starts to bridge the gap between major keys and minor keys, and it helps explain why the relatives match.
def minor_keys():
    minorSharpKeys = ["A min (0)", "E min (1)", "B min (2)", "F# min (3)", "C# min (4)", "G# min (5)", "D# min (6)", "A# min (7)"]
    minorFlatKeys = ["A min (0)", "D min (1)", "G min (2)", "C min (3)", "F min (4)", "B♭ min (5)", "E♭ min (6)", "A♭ min (7)"]

    print("♯ Minor sharp keys: ♯")
    print(f"{'\n'.join(minorSharpKeys)}")
    print("\n♭ Minor flat keys: ♭")
    print(f"{'\n'.join(minorFlatKeys)}")
    print("\nA simple beginner way to learn minor keys is to find the relative major first.\n")
    print("From there, the pattern follows the same relative-major logic: A minor matches C major, D minor matches F major, G minor matches B♭ major, C minor matches E♭ major, and so on.\n")
    print("The major key and minor key share the same accidentals, but they start on different notes.\n")

# Create helper to show the natural minor scale for a selected minor key
# This keeps the teaching simple by using the relative major key signature and the natural minor scale formula.
def natural_minor_scale(key_root: str):
    minor_scale = {
        "A": ["A", "B", "C", "D", "E", "F", "G"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A"],
        "C": ["C", "D", "E♭", "F", "G", "A♭", "B♭"],
        "D": ["D", "E", "F", "G", "A", "B♭", "C"],
        "E": ["E", "F#", "G", "A", "B", "C", "D"],
        "F": ["F", "G", "A♭", "B♭", "C", "D♭", "E♭"],
        "G": ["G", "A", "B♭", "C", "D", "E♭", "F"],
    }

    if key_root in minor_scale:
        return minor_scale[key_root]

    return None

# Create a function to teach how to build a triad chord from a major key.
def chord_from_key(key_name: str):
    normalized = normalize_key_name(key_name)
    major_scale_map = {
        "C": ["C", "D", "E", "F", "G", "A", "B"],
        "G": ["G", "A", "B", "C", "D", "E", "F#"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#"],
        "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
        "F": ["F", "G", "A", "B♭", "C", "D", "E"],
        "B♭": ["B♭", "C", "D", "E♭", "F", "G", "A"],
        "E♭": ["E♭", "F", "G", "A♭", "B♭", "C", "D"],
        "A♭": ["A♭", "B♭", "C", "D♭", "E♭", "F", "G"],
        "D♭": ["D♭", "E♭", "F", "G♭", "A♭", "B♭", "C"],
        "G♭": ["G♭", "A♭", "B♭", "C♭", "D♭", "E♭", "F"],
    }

    if normalized not in major_scale_map:
        print(f"Unknown key: {key_name}")
        return

    scale = major_scale_map[normalized]
    root = scale[0]
    third = scale[2]
    fifth = scale[4]
    chord = [root, third, fifth]

    print(f"{normalized} major")
    print(f"To build a triad, stack the 1st, 3rd, and 5th notes of the scale.")
    print(f"Scale in {normalized} major: {' '.join(scale)}")
    print(f"1st = {root}")
    print(f"3rd = {third}")
    print(f"5th = {fifth}")
    print(f"Chord: {' '.join(chord)}")
    print(f"This gives the {root} major triad: {root} {third} {fifth}.")

# Create a feature to show the major modes built from a key.
def modes_from_key(key_name: str):
    raw = key_name.strip()
    normalized = normalize_key_name(raw)
    explicit_minor = "minor" in raw.lower() or raw.lower().endswith("m") or "min" in raw.lower()
    major_scale_map = {
        "C": ["C", "D", "E", "F", "G", "A", "B"],
        "G": ["G", "A", "B", "C", "D", "E", "F#"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#"],
        "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
        "F": ["F", "G", "A", "B♭", "C", "D", "E"],
        "B♭": ["B♭", "C", "D", "E♭", "F", "G", "A"],
        "E♭": ["E♭", "F", "G", "A♭", "B♭", "C", "D"],
        "A♭": ["A♭", "B♭", "C", "D♭", "E♭", "F", "G"],
        "D♭": ["D♭", "E♭", "F", "G♭", "A♭", "B♭", "C"],
        "G♭": ["G♭", "A♭", "B♭", "C♭", "D♭", "E♭", "F"],
    }
    relative_major_map = {
        "A": "C", "E": "G", "B": "D", "F#": "A", "C#": "E", "G#": "B", "D#": "F#", "A#": "C#",
        "D": "F", "G": "B♭", "C": "E♭", "F": "A♭", "B♭": "D♭", "E♭": "G♭", "A♭": "C♭",
    }

    if explicit_minor:
        print(f"Modes of {normalized} minor")
        print(f"{normalized} minor is a minor-key request, so it is best understood through its relative major.")
        if normalized not in relative_major_map:
            print(f"The app does not currently support a direct mode build for {normalized} minor as a standalone key.")
            print("For a minor key, find the relative major first and build the modes from that major scale instead.")
            return
        relative_major = relative_major_map[normalized]
        scale = major_scale_map[relative_major]
        print(f"Relative major: {relative_major} major")
        print(f"Parent scale: {' '.join(scale)}")
        print("Mode patterns are still taken from the same parent scale, but the tonal centre is minor in this request.")
        print("This means the mode qualities and emotional colours are interpreted from the minor-key relationship, not from a major-key route.")
        return

    if normalized not in major_scale_map:
        print(f"Unknown key: {key_name}")
        return

    scale = major_scale_map[normalized]
    mode_details = [
        ("Ionian", "1st", "Major", "bright, stable, resolved"),
        ("Dorian", "2nd", "Minor", "soulful, smooth, wistful"),
        ("Phrygian", "3rd", "Minor", "dark, tense, exotic"),
        ("Lydian", "4th", "Major", "airy, bright, dreamy"),
        ("Mixolydian", "5th", "Major", "bluesy, relaxed, upbeat"),
        ("Aeolian", "6th", "Minor", "melancholic, reflective, natural minor"),
        ("Locrian", "7th", "Diminished", "tense, unstable, dark"),
    ]
    modes = []
    for i in range(len(scale)):
        rotated = scale[i:] + scale[:i]
        name, degree, quality, feeling = mode_details[i]
        modes.append((name, degree, quality, feeling, rotated))

    print(f"Modes of {normalized} major")
    print("To build modes, start the scale on each degree of the major scale.")
    print(f"Major scale: {' '.join(scale)}")
    print("Each mode is the same notes, just starting on a different degree, and each one has a different tonal quality.")
    for name, degree, quality, feeling, notes in modes:
        print(f"{name} ({quality} mode, starts on {degree} degree): {' '.join(notes)} — {feeling}")
    print("Example: C major = C D E F G A B C. Rotate that pattern to build D Dorian, E Phrygian, F Lydian, G Mixolydian, A Aeolian, and B Locrian.")
    print("These modes are not just different starting points; major, minor, and diminished qualities change the feeling of the music.")

# Create helper to accept equivalent key spellings everywhere the user may type them
# This includes flat/sharp words, symbolic accidentals, commas, capitals, and spacing differences.
def normalize_key_name(key_name: str):
    text = key_name.strip().lower()
    text = text.replace("double flat", "bb").replace("double sharp", "##")
    text = text.replace("flat", "b").replace("sharp", "#")
    text = text.replace("major", "").replace("maj", "")
    text = text.replace("minor", "")
    if text.endswith("m"):
        text = text[:-1]
    text = text.replace("♭", "b").replace("♯", "#")
    text = text.replace(" ", "").replace("-", "")
    text = re.sub(r"[^a-g#b]", "", text)

    if text in ["cb", "cbb"]:
        return "C♭"
    if text in ["gb", "gbb"]:
        return "G♭"
    if text in ["db", "dbb"]:
        return "D♭"
    if text in ["ab", "abb"]:
        return "A♭"
    if text in ["eb", "ebb"]:
        return "E♭"
    if text in ["bb", "bbb"]:
        return "B♭"
    if text in ["f#", "f##"]:
        return "F#"
    if text in ["c#", "c##"]:
        return "C#"
    if text in ["g", "gb", "g#"]:
        return "G" if text == "g" else ("G♭" if "b" in text else "G")
    if text in ["d", "db", "d#"]:
        return "D" if text == "d" else ("D♭" if "b" in text else "D")
    if text in ["a", "ab", "a#"]:
        return "A" if text == "a" else ("A♭" if "b" in text else "A")
    if text in ["e", "eb", "e#"]:
        return "E" if text == "e" else ("E♭" if "b" in text else "E")
    if text in ["b", "bb", "b#"]:
        return "B" if text == "b" else ("B♭" if "b" in text else "B")
    if text in ["f", "fb", "f#"]:
        return "F" if text == "f" else ("F" if "b" in text else "F#")
    if text in ["c", "cb", "c#"]:
        return "C" if text == "c" else ("C♭" if "b" in text else "C")

    return text.upper()

# Create function to display a specific key signature and the accidentals used within it
# This is a practical lookup function for any major or minor key the user might want to check.
def key_signature(key_name: str):
    key_name_normalized = key_name.strip().lower()
    is_minor = "minor" in key_name_normalized or key_name_normalized.endswith("m")
    normalized_key = normalize_key_name(key_name)

    if is_minor:
        relative_major_map = {
            "A": "C", "E": "G", "B": "D", "F#": "A", "C#": "E", "G#": "B", "D#": "F#", "A#": "C#",
            "D": "F", "G": "B♭", "C": "E♭", "F": "A♭", "B♭": "D♭", "E♭": "G♭", "A♭": "C♭",
        }

        if normalized_key not in relative_major_map:
            print(f"Unknown minor key: {key_name}")
            print("Try one of:", ", ".join(sorted({key for key in minorKeySignatureMap if key in {"A", "E", "B", "F#", "C#", "G#", "D#", "D", "G", "C", "F", "B♭", "E♭"}})))
            return

        relative_major = relative_major_map[normalized_key]
        key_details = keySignatureMap[relative_major]
        accidentals = key_details["accidentals"]
        key_type = key_details["type"]
        natural_minor_notes = natural_minor_scale(normalized_key)

        print(f"Key: {normalized_key} minor")
        print(f"Relative major: {relative_major} major")

        if key_type == "sharp":
            print(f"Key signature: {accidentals} sharps")
            print(f"Sharp(s): {' '.join([f'{note}#' for note in orderSharps[:accidentals]])}")
        elif key_type == "flat":
            print(f"Key signature: {accidentals} flats")
            print(f"Flat(s): {' '.join([f'{note}♭' for note in orderFlats[:accidentals]])}")
        else:
            print("Key signature: 0 sharps or flats")

        if natural_minor_notes is not None:
            print(f"\nNatural minor scale: {' '.join(natural_minor_notes)}")
            print("Formula: 1 2 b3 4 5 b6 b7")

        print("\nRemember: minor keys use the same key signature as their relative major.")
        return

    if normalized_key not in keySignatureMap:
        print(f"Unknown key: {key_name}")
        print("Try one of:", ", ".join(sorted({key for key in keySignatureMap if key in {"C", "G", "D", "A", "E", "B", "F#", "F", "B♭", "E♭", "A♭", "D♭", "G♭"}})))
        return

    key_details = keySignatureMap[normalized_key]
    accidentals = key_details["accidentals"]
    key_type = key_details["type"]

    if key_type == "sharp":
        notes = [f"{note}#" for note in orderSharps[:accidentals]]
        print(f"Key: {normalized_key} major")
        print(f"Accidentals: {accidentals} sharps")
        print(f"\nSharp order: {' -> '.join(orderSharps)}")
        print(f"{normalized_key} major uses the first {accidentals} sharps:")
        print(f"{' '.join(notes)}")
    elif key_type == "flat":
        notes = [f"{note}♭" for note in orderFlats[:accidentals]]
        print(f"Key: {normalized_key} major")
        print(f"Accidentals: {accidentals} flats")
        print(f"\nFlat order: {' -> '.join(orderFlats)}")
        print(f"{normalized_key} major uses the first {accidentals} flats:")
        print(f"{' '.join(notes)}")
    else:
        print(f"Key: {normalized_key} major")
        print("Accidentals: no sharps or flats")

# Create function to display the mnemonic for a selected order
# This helps the user remember the sequence for sharps or flats without having to memorise it by raw pattern alone.
def mnemonic(order_type: str):
    normalized_order = order_type.strip().lower().replace(" ", "")
    normalized_order = normalized_order.replace("sharp", "sharp").replace("flat", "flat")
    normalized_order = normalized_order.replace("sharps", "sharp").replace("flats", "flat")
    normalized_order = normalized_order.replace("s", "sharp") if normalized_order == "s" else normalized_order
    normalized_order = normalized_order.replace("f", "flat") if normalized_order == "f" else normalized_order

    if normalized_order in ["sharp", "sharps"]:
        print(f"The order of sharps is: {' '.join(orderSharps)}")
        print(f"The mnemonic is: {' '.join(mnemonicSharps)}")
    elif normalized_order in ["flat", "flats"]:
        print(f"The order of flats is: {' '.join(orderFlats)}")
        print(f"The mnemonic is: {' '.join(mnemonicFlats)}")
    else:
        print("Unknown order type. Try 'sharp' or 'flat'.")


__all__ = [
    "orderSharps", "mnemonicSharps", "orderFlats", "mnemonicFlats",
    "sharpKeys", "flatKeys", "minorKeys", "keySignatureMap", "minorKeySignatureMap",
    "sharp_order", "flat_order", "sharp_keys", "flat_keys", "keys", "scale_from_key", "scales_overview", "scales_page",
    "chord_from_key", "chords_overview", "chords_page", "modes_from_key", "modes_overview", "modes_page",
    "riff_guide", "bassline_guide", "melody_guide", "genre_analysis_guide", "walking_bassline_guide",
    "circle_of_fifths", "minor_keys", "natural_minor_scale", "normalize_key_name", "key_signature", "mnemonic"
]
