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

# Setup key order array
sharpKeys = ["C maj (0)", "G maj (1)", "D maj (2)", "A maj (3)", "E maj (4)", "B major (5)", "F# maj (6)", "C# maj (7)"]
flatKeys = ["C maj (0)", "F maj (1)", "B♭ maj (2)", "E♭ maj (3)", "A♭ maj (4)", "D♭ maj (5)", "G♭ maj (6)", "C♭ maj (7)"]
minorKeys = ["A min (0)", "E min (1)", "B min (2)", "F# min (3)", "C# min (4)", "G# min (5)", "D# min (6)", "A# min (7)", "D min (1)", "G min (2)", "C min (3)", "F min (4)", "B♭ min (5)", "E♭ min (6)", "A♭ min (7)"]

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
    print(f"♯ Sharp keys: ♯\n{'\n'.join(sharpKeys)}\nThis is the same order as the sharps inside the key signature, except it starts and ends at C.\nA good beginner tip is to remember that sharp keys usually move upward through the circle of fifths.\n\n")

# Create function to list the flat keys in order of number of flats
# This mirrors the sharp-key section and helps beginners see the relationship between the key signature and the key name.
def flat_keys():
    print(f"♭ Flat keys: ♭\n{'\n'.join(flatKeys)}\nThis is the same order as the flats inside the key signature, except it starts and ends at C.\nA good beginner tip is to remember that flat keys move in the opposite direction from sharp keys.\n\n")

# Create function to display all information about key signatures
# This is the combined reference section when the user wants the whole picture in one place.
def keys():
    sharp_order()
    flat_order()
    sharp_keys()
    flat_keys()
    minor_keys()

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
            print("Try one of:", ", ".join(sorted(minorKeySignatureMap.keys())))
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
        print("Try one of:", ", ".join(sorted(keySignatureMap.keys())))
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
    "sharp_order", "flat_order", "sharp_keys", "flat_keys", "keys", "minor_keys",
    "natural_minor_scale", "normalize_key_name", "key_signature", "mnemonic"
]
