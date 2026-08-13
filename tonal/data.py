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
    print("")
    print("Arpeggios")
    print("- An arpeggio is simply a chord broken into individual notes in order.")
    print("- When you play G B D as G - B - D - G, you are arpeggiating the G major chord.")
    print("- Arpeggios are useful for learning chord tones, smooth bass movement, and melodic fills.")
    print("- Practice by playing each chord tone deliberately, then connecting them without losing the shape of the chord.")
    print("")
    print("Inversions")
    print("- A chord inversion changes which chord tone is in the bass.")
    print("- Root position: G B D (root in the bass)")
    print("- First inversion: B D G (3rd in the bass)")
    print("- Second inversion: D G B (5th in the bass)")
    print("- Inversions help the bassline move smoothly and keep the harmony connected without jumping between roots too much.")
    print("- Use inversions to create a better voice-leading line and to keep the bass line more musical than just repeating roots.")
    print("")
    print("How to construct a chord across four, five, and six strings")
    print("A bass chord can be voiced across any number of strings, but the goal is always the same: keep the chord tones clear and playable.")
    print("Across four strings:")
    print("- Use the root, 3rd, 5th, and optionally the octave or 7th for colour.")
    print("- Example for G major on a four-string bass: G - B - D - G")
    print("- This gives a clear triad with enough fullness to sound balanced without being muddy.")
    print("Across five strings:")
    print("- Add an extra octave or a nearby extension to widen the chord.")
    print("- Example: G - B - D - G - B, or G - D - G - B - D depending on the register you want.")
    print("- This is helpful when you want a fuller voicing or a more spread-out arpeggio pattern.")
    print("Across six strings:")
    print("- You can spread the chord across a wider range and use even more interval colour.")
    print("- Example: G - D - G - B - D - G, or a 3rd/5th/7th layout if you want more colour.")
    print("- On bass, make sure the chord still sounds like a bass chord, not a dense guitar-like stack of notes.")
    print("")
    print("When two notes fall on the same string")
    print("- This is a very common problem when building inversions or extended arpeggios.")
    print("- If two notes share the same string, you cannot play them simultaneously as separate pitches on that string without changing fingering or reordering the voicing.")
    print("- The usual fix is to choose a different inversion, move one note to another string, or re-order the notes into a more playable sequence.")
    print("- For example, a G major inversion such as G - B - D - G can become B - D - G - B when you want the 3rd in the bass, but if the note layout causes two notes to collide on one string, move the upper chord tone to the next string instead of forcing the clash.")
    print("- The rule is: keep the chord tones clear, and let the arrangement of strings support the intended inversion rather than fight it.")
    print("- In practice, if you see two notes on one string, choose the string that keeps the line smoothest and then adjust the voicing by moving one note to an adjacent string.")
    print("- Bass players often solve this by re-voicing the chord into a different inversion or by choosing a more compact position that keeps the chord shape playable.")
    print("")
    print("A useful practical method")
    print("1. Start with the root, third, fifth, and octave of the chord.")
    print("2. Decide which chord tone should sit in the bass.")
    print("3. Choose the string layout that keeps the notes spread cleanly across strings.")
    print("4. If a note repeats on the same string, shift one note to the next string or change inversion.")
    print("5. Smooth the motion between chord shapes so the arpeggio feels like a musical line, not a static shape.")
    print("")
    print("This is the heart of bass voicing: the chord is not just a formula, it is a playable arrangement of notes across the neck.")

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

# Transposition helpers and guides.
def _normalize_note_name(note: str):
    return note.strip().replace("♯", "#").replace("♭", "b")


def _prefer_flat_for_note(note: str):
    normalized = _normalize_note_name(note)
    if normalized in {"C", "D", "E", "F", "G", "A", "B"}:
        return False
    return normalized.endswith("b") and len(normalized) > 1


def _note_to_pitch(note: str):
    normalized = _normalize_note_name(note)
    pitch_map = {
        "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4,
        "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9,
        "A#": 10, "Bb": 10, "B": 11, "Cb": 11, "B#": 0,
    }
    if normalized in pitch_map:
        return pitch_map[normalized]

    match = re.match(r"^([A-Ga-g])(#|b|##|bb)?$", normalized)
    if not match:
        return None

    letter = match.group(1).upper()
    accidental = match.group(2) or ""
    base = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}[letter]
    accidental_value = accidental.count("#") - accidental.count("b")
    return (base + accidental_value) % 12


def _pitch_to_note(pitch: int, prefer_flat: bool = False):
    sharp_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    flat_names = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    choice = flat_names if prefer_flat else sharp_names
    return choice[pitch % 12]


def transpose_notes(notes, semitones: int):
    if isinstance(notes, str):
        notes = [notes]

    transposed = []
    shift = int(semitones) % 12
    for note in notes:
        pitch = _note_to_pitch(note)
        if pitch is None:
            transposed.append(note)
            continue
        prefer_flat = _prefer_flat_for_note(note)
        transposed.append(_pitch_to_note((pitch + shift) % 12, prefer_flat=prefer_flat))
    return transposed


def transpose_key(source_key: str, target_key: str = None):
    source_normalized = normalize_key_name(source_key)
    if source_normalized in ["", None]:
        print(f"Unknown key: {source_key}")
        return

    if target_key is None:
        print("Transposition guide")
        print("==================")
        print(f"To transpose {source_key}, choose a new key and move each note by the same interval.")
        print("General rule: all intervals stay the same, but the pitch centre changes.")
        print("For example, moving from C to G is a perfect fifth and raises the whole piece by 7 semitones.")
        return

    source_pitch = _note_to_pitch(source_normalized)
    target_pitch = _note_to_pitch(normalize_key_name(target_key))
    if source_pitch is None or target_pitch is None:
        print(f"Unable to transpose from {source_key} to {target_key}.")
        return

    distance = (target_pitch - source_pitch) % 12
    interval_names = {
        0: "perfect unison",
        1: "minor second",
        2: "major second",
        3: "minor third",
        4: "major third",
        5: "perfect fourth",
        6: "tritone",
        7: "perfect fifth",
        8: "minor sixth",
        9: "major sixth",
        10: "minor seventh",
        11: "major seventh",
    }

    target_key_name = normalize_key_name(target_key)
    print(f"Transposing {source_key} to {target_key_name} major")
    print(f"Interval: {interval_names.get(distance, f'{distance} semitones')}")
    print(f"This moves the whole piece by {distance} semitones, preserving the pattern of intervals while changing the tonal centre.")
    print("A practical way to think about it:")
    print("- keep the same melodic shape")
    print("- keep the same chord functions")
    print("- adjust the key signature to match the new key")
    print("- re-check accidentals and leading tones in the new context")

    source_scale = ["C", "D", "E", "F", "G", "A", "B"]
    transposed_scale = transpose_notes(source_scale, distance)
    print(f"Example scale pattern: {' '.join(source_scale)}")
    print(f"Transposed scale: {' '.join(transposed_scale)}")
    print("This is the same scale shape, just moved into a new key.")


def transposition_guide():
    print("Transposition")
    print("=============")
    print("To transpose a piece means to move every pitch by the same interval while keeping the musical relationships intact.")
    print("The purpose is often to suit a different vocal range, a different instrument, a more comfortable fingering, or a different ensemble context.")
    print("")
    print("Generic rules for transposing a piece")
    print("1. Decide the target key or interval before altering any notes.")
    print("2. Move every note by the same amount of semitones.")
    print("3. Keep chord functions and melodic shape the same; only the pitch centre changes.")
    print("4. Check the key signature afterwards, because accidentals may change when you move to the new key.")
    print("5. For arrangements with singers, check range and tessitura before deciding on the new key.")
    print("6. For instruments, consider whether the part is written for concert pitch or for a transposing instrument such as B♭ trumpet or E♭ alto saxophone.")
    print("")
    print("Transposing by key")
    print("- C major to G major: move up a perfect fifth, or +7 semitones.")
    print("- C major to F major: move up a perfect fourth, or +5 semitones.")
    print("- C major to D major: move up a major second, or +2 semitones.")
    print("- A minor to C minor: move up a minor third, or +3 semitones.")
    print("The same ideas work for any key: each key has a fixed interval relationship to the parent key, and the new key signature follows that relationship.")
    print("")
    print("Specific guidance by scale")
    print("- Major scales transpose by preserving the same pattern of steps: tone, tone, semitone, tone, tone, tone, semitone.")
    print("- Natural minor scales keep the same minor-pattern interval structure, while the key signature shifts to match the new minor key.")
    print("- Modes preserve the parent scale shape, but the tonal centre changes. When you transpose a mode, you transpose the whole parent collection and keep the same modal quality.")
    print("- If a melody is based on D Dorian, transposing it means moving the whole Dorian pattern by the same interval while keeping the same modal colour.")
    print("")
    print("Specific guidance by chord")
    print("- A major triad transposed by a perfect fifth becomes the new dominant function of the target key.")
    print("- A minor triad is still a minor triad after transposition; only the pitch centre changes.")
    print("- The chord quality must remain the same unless you deliberately want to change the harmonic colour.")
    print("- For example, G major to C major means moving each note up a perfect fourth; G B D becomes C E G.")
    print("")
    print("Specific guidance by mode")
    print("- Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, and Locrian all keep their interval pattern when transposed.")
    print("- What changes is the root pitch, not the mode's internal structure.")
    print("- If a phrase is in A Aeolian, transposing it to D Aeolian keeps the same minor, reflective feel while moving the whole phrase to a new pitch centre.")
    print("")
    print("Specific guidance by piece condition")
    print("- For a melody alone: move each note by the selected interval and check whether the line still sits comfortably in the singer's range.")
    print("- For a lead sheet: transpose the melody and the chord symbols together so the harmonic function remains coherent.")
    print("- For a full arrangement: transpose the whole harmony, bassline, and melody together unless the ensemble needs a different strategy.")
    print("- For a fixed-pitch instrument: the part must be transposed according to the instrument's written range and transposition convention.")
    print("- For a vocal piece: choose the new key by checking the strongest notes and the part's comfortable tessitura, not only by the written notes.")
    print("")
    print("Quick practical example")
    print("- Original: C major -> melody: C E G")


def _string_note_map():
    return {
        "E": ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"],
        "A": ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"],
        "D": ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D"],
        "G": ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"],
    }


def _note_pitch_set(notes):
    return {_note_to_pitch(note) for note in notes if _note_to_pitch(note) is not None}


def _display_fretboard(title: str, highlight_note_names=None):
    highlight = _note_pitch_set(highlight_note_names or [])
    print(title)
    print("=" * len(title))
    for string_name, notes in reversed(list(_string_note_map().items())):
        cells = []
        for fret, note in enumerate(notes):
            pitch = _note_to_pitch(note)
            label = f"{fret}:{note}"
            if pitch in highlight:
                label = f"[{fret}:{note}]"
            cells.append(f"{label:>8}")
        print(f"{string_name} string: {' '.join(cells)}")
    print("")


def _display_ascii_fretboard(title: str, highlight_note_names=None, fret_markers=None, label_mode="notes"):
    highlight = _note_pitch_set(highlight_note_names or [])
    fret_markers = set(fret_markers or [5, 7])
    print(title)
    print("=" * len(title))
    string_names = ["G", "D", "A", "E"]
    for string_name in string_names:
        notes = _string_note_map()[string_name]
        labels = []
        for fret in range(0, 13):
            note = notes[fret]
            pitch = _note_to_pitch(note)
            if label_mode == "notes":
                label = note if pitch in highlight else "."
            elif label_mode == "roman":
                roman_map = {
                    0: "I", 1: "II", 2: "III", 3: "IV", 4: "V", 5: "VI", 6: "VII", 7: "VIII",
                    8: "IX", 9: "X", 10: "XI", 11: "XII", 12: "XIII"
                }
                label = roman_map.get(fret % 13, ".") if pitch in highlight else "."
            else:
                label = note if pitch in highlight else "."
            labels.append(label)

        width = max(3, max(len(str(label)) for label in labels))
        cells = []
        for fret in range(0, 13):
            label = labels[fret]
            cell_label = f"{label:^{width}}"
            if fret in fret_markers:
                cells.append(f"{fret:>2}:|| {cell_label} ||")
            else:
                cells.append(f"{fret:>2}:| {cell_label} |")
        print(f"{string_name}: " + " ".join(cells))
    print("")


def _display_interval_pattern(pattern_name: str, root: str, offsets, string_offsets=None):
    print(pattern_name)
    print("-" * len(pattern_name))
    root_pitch = _note_to_pitch(root)
    note_row = []
    for string_name in ["E", "A", "D", "G"]:
        segments = []
        for fret in range(0, 13):
            note = _string_note_map()[string_name][fret]
            if fret in offsets:
                segments.append(f"{fret}:{note}")
            elif fret in [0, 2, 3, 5, 7, 8, 10, 12]:
                segments.append(".")
        row = " | ".join(segments)
        print(f"{string_name}: {row}")
    print("")


def _interval_label(offset: int, flattened: bool = False):
    names = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
    label = names[offset % 8]
    if flattened:
        return f"{label}♭"
    return label


def _display_interval_diagram(title: str, string_positions):
    print(title)
    print("-" * len(title))
    all_labels = []
    for positions in string_positions.values():
        all_labels.extend(str(v) for v in positions.values())
    all_labels = ["."] + all_labels
    cell_width = max(3, max(len(label) for label in all_labels))

    for string_name in ["G", "D", "A", "E"]:
        positions = string_positions.get(string_name, {})
        cells = []
        for fret in range(0, 13):
            label = str(positions.get(fret, "."))
            padded = f"{label:^{cell_width}}"
            if fret in {5, 7}:
                cells.append(f"{fret:>2}:|| {padded} ||")
            else:
                cells.append(f"{fret:>2}:| {padded} |")
        print(f"{string_name}: " + " ".join(cells))
    print("")


def bassfret_money_notes():
    print("Bass fretboard: Money notes")
    print("==========================")
    print("The 'money notes' are the anchor notes that make the fretboard easier to learn.")
    print("If you memorise only a few places, you can quickly find the rest of the notes by pattern and interval.")
    print("The most useful money notes are the open strings, the 5th fret, the 7th fret, and the octave at the 12th fret.")
    print("Open strings are: E A D G")
    print("The 5th fret on any string gives the same pitch as the next string open, which makes string-to-string navigation easy.")
    print("The 7th fret is a very useful landing point when you want to move smoothly around the neck and hold a shape.")
    print("The 12th fret is the octave, so the note name repeats and the pattern resets.")
    print("")
    print("Key spacing rules")
    print("- Across two strings and up two frets: same note an octave higher.")
    print("- Across one string and down 5 frets: same octave, because 5 frets up on a string is the same pitch as the next string open.")
    print("- Across one string and down 4 frets: the same interval pattern as a major-scale step, useful for finding the next note in a scale.")
    print("- Use string-to-string movement by 5ths and 4ths to avoid counting all the way from the root.")
    print("- Learn the octave repeats at 12 and the 5th-fret relationship before memorising every note individually.")
    print("")
    money_notes = ["E", "A", "D", "G", "C", "F", "B", "E"]
    print("Fretboard diagram (5th and 7th frets marked strongly):")
    _display_ascii_fretboard("Money-note map", money_notes, fret_markers=[5, 7], label_mode="notes")
    print("How to use them:")
    print("- Start by learning the open strings and their octave repeats.")
    print("- Use the 5th-fret rule to jump between strings.")
    print("- Learn the 7th fret as a strong tonal landing zone, especially for root movement and chord tones.")
    print("- Treat the 12th fret as a reset point: the note names repeat and the patterns become easier to read.")
    print("This is how you turn the fretboard from a maze into a set of repeating shapes.")


def bassfret_intervals():
    print("Bass fretboard: Intervals")
    print("=========================")
    print("Intervals tell you how notes relate to the root and help you build lines without memorising every note by raw position.")
    print("A clear way to think about them is by roman numeral: I = root, II = second, III = third, IV = fourth, V = fifth, VI = sixth, VII = seventh, VIII = octave.")
    print("The practical idea is to learn the interval pattern across the strings, not to repeat the same list on every string.")
    print("Each interval has its own fingering shape, and the easiest ones are the ones that sit inside a compact span around the root.")
    print("")

    root_position = {"E": {4: "I"}, "A": {1: "II"}, "D": {1: "V"}, "G": {1: "VII"}}
    _display_interval_diagram("Perfect 5th: root to V", {"E": {4: "I", 7: "V"}, "A": {1: "II", 5: "IV", 9: "V"}, "D": {1: "I", 4: "IV", 8: "VI"}, "G": {1: "II", 5: "V"}})
    _display_interval_diagram("Tritone: root to IV#/V♭", {"E": {4: "I", 6: "IV#/V♭"}, "A": {1: "II", 4: "IV", 7: "V"}, "D": {1: "I", 5: "IV", 8: "VI"}, "G": {1: "II", 5: "V"}})
    _display_interval_diagram("Major 6th: root to VI", {"E": {4: "I", 9: "VI"}, "A": {1: "II", 4: "IV", 7: "V", 9: "VI"}, "D": {1: "I", 6: "VI"}, "G": {1: "II"}})
    _display_interval_diagram("Major 7th: root to VII", {"E": {4: "I", 10: "VII"}, "A": {1: "II", 5: "IV", 9: "VI", 10: "VII"}, "D": {1: "I", 7: "V"}, "G": {1: "II"}})
    _display_interval_diagram("Octave: root to VIII", {"E": {4: "I", 12: "VIII"}, "A": {5: "VIII"}, "D": {1: "II"}, "G": {1: "II"}})
    _display_interval_diagram("Major 2nd: root to II", {"E": {4: "I", 5: "II"}, "A": {1: "II", 2: "III♭"}, "D": {1: "I", 2: "II"}, "G": {1: "II"}})
    print("Root-to-octave map: practical fingering")
    print("====================================")
    _display_interval_diagram("Root to VIII map", {"E": {0: ".", 1: ".", 2: ".", 4: "I", 5: "II♭", 6: "II", 7: "III♭", 8: "III"}, "A": {1: "II", 2: "III♭", 3: "III", 4: "IV", 5: "IV#/V♭", 6: "V", 7: "V#/VI♭", 8: "VI"}, "D": {1: "V", 2: "V#/VI♭", 3: "VI", 4: "VII♭", 5: "VII", 6: "VIII"}, "G": {1: ".", 2: ".", 3: "."}})
    print("The rule is simple:")
    print("- start from the root and keep the interval span compact")
    print("- do not repeat the same values on every string")
    print("- move through the strings in the practical shape that keeps the same interval logic but makes the fingering easy to play")
    print("- the low string is the root and first few upper intervals, the next string carries the middle of the shape, and the top string finishes the interval motion toward the octave")
    print("")
    print("Practical advice")
    print("- Learn the interval shape, not just a list of numbers.")
    print("- Use the same voice-leading idea across strings instead of repeating the same values on every string.")
    print("- For melodic work, memorise the shape that feels easy to reach and keep the notes connected to the root.")
    print("- The most useful intervals are root, 3rd, 5th, 7th, octave, then the passing tones between them.")
    print("If you can hear the interval and see the shape, you can find it anywhere on the neck without counting from zero every time.")


def _build_scale_comparison_page():
    examples = [
        ("G mixolydian", ("G", [0, 2, 4, 5, 7, 9, 10])),
        ("D dorian", ("D", [0, 2, 3, 5, 7, 9, 10])),
        ("E phrygian", ("E", [0, 1, 3, 5, 7, 8, 10])),
        ("A natural minor", ("A", [0, 2, 3, 5, 7, 8, 10])),
        ("A blues", ("A", [0, 3, 5, 6, 7, 10])),
    ]
    print("Bass fretboard: Scale comparison")
    print("================================")
    print("This page shows a small set of very useful scale shapes together so you can compare their interval patterns and learn them as a family.")
    print("The goal is to hear the difference between major, minor, modal, and blues colours without learning them as unrelated shapes.")
    for name, (root, semitones) in examples:
        notes = _scale_notes_from_root(root, semitones)
        print(f"\n{name.title()} ({root} root): {' '.join(notes)}")
        print("Pattern:")
        print("  " + " ".join(str(n) for n in semitones))
        _display_ascii_fretboard(f"{name.title()} scale", notes, fret_markers=[5, 7])
    print("Teaching note:")
    print("- Mixolydian and Dorian are close cousins, but Mixolydian has a flatter VII while Dorian keeps a smoother minor colour.")
    print("- Phrygian and Aeolian both feel dark and minor, but Phrygian has a more exotic, tense colour because of the flat II.")
    print("- Blues adds the blue third and flat seventh, which is why it feels so expressive and flexible.")
    print("- Learn the interval pattern, not just the note names, so you can use the scale anywhere on the neck.")


def bassfret_compare():
    _build_scale_comparison_page()


def _scale_definitions():
    return {
        "g mixolydian": ("G", [0, 2, 4, 5, 7, 9, 10]),
        "d dorian": ("D", [0, 2, 3, 5, 7, 9, 10]),
        "a natural minor": ("A", [0, 2, 3, 5, 7, 8, 10]),
        "e phrygian": ("E", [0, 1, 3, 5, 7, 8, 10]),
        "f lydian": ("F", [0, 2, 4, 6, 7, 9, 11]),
        "a blues": ("A", [0, 3, 5, 6, 7, 10]),
        "g pentatonic major": ("G", [0, 2, 4, 7, 9]),
        "e pentatonic minor": ("E", [0, 3, 5, 7, 10]),
        "b♭ major": ("B♭", [0, 2, 4, 5, 7, 9, 11]),
    }


def _scale_notes_from_root(root_note: str, semitones):
    root_pitch = _note_to_pitch(root_note)
    if root_pitch is None:
        return []
    notes = []
    for offset in semitones:
        pitch = (root_pitch + offset) % 12
        prefer_flat = "b" in _normalize_note_name(root_note).lower()
        notes.append(_pitch_to_note(pitch, prefer_flat=prefer_flat))
    return notes


def bassfret_scale(scale_name: str = "G mixolydian"):
    lookup_name = (scale_name or "G mixolydian").strip().lower()
    root_key = None
    if lookup_name in {"g", "a", "d", "e", "f", "c", "b", "bb", "eb", "ab", "db", "gb"}:
        root_key = lookup_name.upper().replace("BB", "B♭").replace("EB", "E♭").replace("AB", "A♭").replace("DB", "D♭").replace("GB", "G♭")
        print(f"Bass fretboard: {root_key} scale set")
        print("=" * (len(root_key) + 29))
        print("A practical improvisation set for this root: choose the scale colour that suits the musical moment.")
        print("These are the most useful patterns on bass for a wide range of styles and moods.")
        scale_set = []
        if root_key == "G":
            scale_set = [
                ("G mixolydian", ("G", [0, 2, 4, 5, 7, 9, 10])),
                ("G dorian", ("G", [0, 2, 3, 5, 7, 9, 10])),
                ("G major", ("G", [0, 2, 4, 5, 7, 9, 11])),
                ("G blues", ("G", [0, 3, 5, 6, 7, 10])),
                ("G pentatonic major", ("G", [0, 2, 4, 7, 9])),
            ]
        elif root_key == "A":
            scale_set = [
                ("A natural minor", ("A", [0, 2, 3, 5, 7, 8, 10])),
                ("A dorian", ("A", [0, 2, 3, 5, 7, 9, 10])),
                ("A blues", ("A", [0, 3, 5, 6, 7, 10])),
                ("A pentatonic minor", ("A", [0, 3, 5, 7, 10])),
                ("A phrygian", ("A", [0, 1, 3, 5, 7, 8, 10])),
            ]
        elif root_key == "D":
            scale_set = [
                ("D dorian", ("D", [0, 2, 3, 5, 7, 9, 10])),
                ("D mixolydian", ("D", [0, 2, 4, 5, 7, 9, 10])),
                ("D major", ("D", [0, 2, 4, 5, 7, 9, 11])),
                ("D pentatonic major", ("D", [0, 2, 4, 7, 9])),
                ("D minor pentatonic", ("D", [0, 3, 5, 7, 10])),
            ]
        else:
            scale_set = [
                (f"{root_key} mixolydian", (root_key, [0, 2, 4, 5, 7, 9, 10])),
                (f"{root_key} dorian", (root_key, [0, 2, 3, 5, 7, 9, 10])),
                (f"{root_key} blues", (root_key, [0, 3, 5, 6, 7, 10])),
            ]
        for name, (root, intervals) in scale_set:
            notes = _scale_notes_from_root(root, intervals)
            print(f"\n{name.title()}: {' '.join(notes)}")
            _display_ascii_fretboard(f"{name.title()} pattern", notes, fret_markers=[5, 7], label_mode="notes")
        print("Use the scale that matches the mood: brighter and more stable for major colours, darker and more fluid for minor and modal colours.")
        return

    definition = _scale_definitions().get(lookup_name)
    if definition is None:
        available = ", ".join(sorted(_scale_definitions().keys()))
        print(f"Unknown scale selection: {scale_name}")
        print(f"Try one of: {available}")
        return

    root, intervals = definition
    notes = _scale_notes_from_root(root, intervals)
    print(f"Bass fretboard: {scale_name.title()}")
    print("=" * (len(scale_name) + 22))
    print(f"Root: {root} | Notes: {' '.join(notes)}")
    print("This is a useful shape because it keeps the scale in a compact, musical set of positions.")
    print("Look for the repeating interval pattern and use the money-note anchors to navigate the neck.")
    _display_ascii_fretboard(f"{scale_name.title()} pattern", notes, fret_markers=[5, 7], label_mode="notes")
    print("Key teaching point:")
    print("- use the money notes to find the root quickly")
    print("- find the third and seventh to confirm the scale quality")
    print("- move by interval shapes, not by raw counting, once the pattern is familiar")


def bassfret_guide():
    print("Bass fretboard guide")
    print("====================")
    print("The fastest way to learn the bass fretboard is to stop thinking of it as 24 random positions and instead think of it as a network of repeating shapes.")
    print("Use the money notes as your anchors: open strings, 5th fret, 7th fret, and octave at the 12th fret.")
    print("Once those are stable, the rest of the neck becomes a pattern puzzle instead of a blind search.")
    print("")
    print("How to learn the notes by relation to the money notes")
    print("1. Learn the open strings by heart: E A D G")
    print("2. Memorise the 5th-fret trick: the 5th fret of the E string is A, the 5th fret of A is D, and the 5th fret of D is G.")
    print("3. Memorise the 7th fret as a strong tonal marker, especially for chord tones and motion between notes.")
    print("4. Treat the 12th fret as a reset point: the notes repeat an octave above the open string.")
    print("5. Fill in the gaps by learning interval shapes, not by memorising every single position individually.")
    print("6. If you know the root and the interval pattern, you can find the rest of the notes without counting carefully every time.")
    print("")
    print("How to stop reading tabs first and start sight-reading the staff")
    print("The method is:")
    print("1. Learn the staff landmarks first: identify the lines and spaces by note name, not by memorising a single pattern.")
    print("2. Read the note names without looking at the fretboard at all for the first pass.")
    print("3. Then find the same pitch on the bass by interval or money-note shape, not by mental conversion from tab.")
    print("4. Practise small, repeated note patterns so you can recognise them as shapes instead of single random notes.")
    print("5. Keep rhythm and pitch separate in your head: first read the note names, then read the beats, then connect them.")
    print("6. Use the same pattern recognition you use in tabs, but apply it to the staff: 3rds, 5ths, scales, and stepwise motion all read the same way on the page.")
    print("")
    print("How to get to sheet music sight-reading speed")
    print("- Read note names by pattern, not by staring at individual notes.")
    print("- Learn the common bass-clef landmarks quickly: G, A, B, C, D, E, F on different lines and spaces.")
    print("- Use interval thinking: if the melody moves by a third, look for the third shape; if it leaps by a fifth, find the fifth directly.")
    print("- Practice reading a short line at a slow pace and immediately find the note on the bass by position and shape.")
    print("- Do not keep depending on the tab as a shortcut. The tab is useful for learning fingering, but the staff is your reading skill.")
    print("- Once you can recognise scale degrees and chord tones on the page, you will stop feeling like the staff is a different language and start seeing it as a direct map of the same musical ideas.")
    print("This is the real goal: reading the notation confidently enough that the tab no longer feels like the easier path.")
    print("If you can recognise intervals, scales, and chord tones on the page and on the fretboard, sight-reading becomes a habit instead of a struggle.")
    print("That is how you move from 'I read tabs first' to 'I can read the music and find it on the bass almost as fast'.")


# Practical composition and analysis guides.
def riff_guide():
    print("- Transposed up a perfect fifth: G B D")
    print("- The interval pattern stays the same: root, third, fifth; only the pitch centre changes.")
    print("This is why transposition is so useful: it preserves the musical logic while changing the overall key. ")


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
    "transpose_notes", "transpose_key", "transposition_guide",
    "bassfret_money_notes", "bassfret_intervals", "bassfret_scale", "bassfret_guide",
    "riff_guide", "bassline_guide", "melody_guide", "genre_analysis_guide", "walking_bassline_guide",
    "circle_of_fifths", "minor_keys", "natural_minor_scale", "normalize_key_name", "key_signature", "mnemonic"
]
