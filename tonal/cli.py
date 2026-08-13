import sys

# This is the command-line entry for the app.
# It keeps the menu system separate from the music-theory logic, which makes it easier to keep extending the project without crowding everything into one file.

from .data import (
    bassfret_compare,
    bassfret_guide,
    bassfret_intervals,
    bassfret_money_notes,
    bassfret_scale,
    bassline_guide,
    cello_guide,
    chord_from_key,
    chords_overview,
    circle_of_fifths,
    flat_keys,
    flat_order,
    genre_analysis_guide,
    keySignatureMap,
    key_signature,
    keys,
    melody_guide,
    minor_keys,
    mnemonic,
    modes_from_key,
    modes_overview,
    riff_guide,
    scale_from_key,
    scales_overview,
    sharp_keys,
    sharp_order,
    transposition_guide,
    transpose_key,
    walking_bassline_guide,
)
from .quiz import quiz

# Registry mapping user input to functions
# This is deliberately simple so the app can grow into broader music-theory features without a big rewrite.
FUNCTIONS = {
    "sharp_order": sharp_order,
    "flat_order": flat_order,
    "sharp_keys": sharp_keys,
    "flat_keys": flat_keys,
    "minor_keys": minor_keys,
    "keys": keys,
    "circle": circle_of_fifths,
    "circle_of_fifths": circle_of_fifths,
    "scales": scales_overview,
    "scale": scale_from_key,
    "scale_from_key": scale_from_key,
    "chords": chords_overview,
    "chord": chord_from_key,
    "chord_from_key": chord_from_key,
    "modes": modes_overview,
    "modes_from_key": modes_from_key,
    "riff": riff_guide,
    "bassline": bassline_guide,
    "melody": melody_guide,
    "genre": genre_analysis_guide,
    "genre_analysis": genre_analysis_guide,
    "walking_bassline": walking_bassline_guide,
    "transposition": transposition_guide,
    "transpose": transpose_key,
    "transpose_key": transpose_key,
    "bassfret": bassfret_guide,
    "bassfret_money": bassfret_money_notes,
    "bassfret_intervals": bassfret_intervals,
    "bassfret_scale": bassfret_scale,
    "bassfret_compare": bassfret_compare,
    "cello": cello_guide,
    "key": key_signature,
    "key_signature": key_signature,
    "mnemonic": mnemonic,
    "P": mnemonic,
    "quiz": quiz,
}

# Show a quick help menu for the terminal user
# This keeps the app easy to use from the shell while also making it look more like a proper small CLI app.
def show_help():
    print("Tonal")
    print("Usage: tonal <command> [arguments]")
    print("")
    print("Commands:")
    for name in [
        "keys",
        "sharp_order",
        "flat_order",
        "sharp_keys",
        "flat_keys",
        "minor_keys",
        "circle",
        "circle_of_fifths",
        "scales",
        "scale <key>",
        "chords",
        "chord <key>",
        "modes",
        "modes <key>",
        "riff",
        "bassline",
        "melody",
        "genre",
        "walking_bassline",
        "transposition",
        "transpose <source> <target>",
        "cello",
        "bassfret",
        "bassfret money",
        "bassfret intervals",
        "bassfret scale <name>",
        "key <name>",
        "mnemonic <sharp|flat>",
        "quiz",
    ]:
        print(f"  - {name}")
    print("")
    print("Examples:")
    print("  tonal keys")
    print("  tonal key Dm")
    print("  tonal mnemonic sharp")
    print("  tonal quiz")


def show_bassfret_help():
    print("bassfret")
    print("Usage: tonal bassfret [money|intervals|scale <name>]")
    print("")
    print("Available arguments:")
    for name in [
        "money",
        "intervals",
        "scale <name>",
        "compare",
        "help",
    ]:
        print(f"  - {name}")
    print("")
    print("Examples:")
    print("  tonal bassfret")
    print("  tonal bassfret money")
    print("  tonal bassfret intervals")
    print("  tonal bassfret scale G mixolydian")
    print("  tonal bassfret compare")

# Setup input argument function
# The user can pass a function name and any extra arguments, and the app dispatches to the right piece of logic.
def main(func_name: str, *args):
    if func_name in ["--help", "-h", "help"]:
        show_help()
        return
    if func_name not in FUNCTIONS:
        print("Unknown function name.")
        print("Try one of:", ", ".join(FUNCTIONS.keys()))
        return

    if func_name in ["key", "key_signature"]:
        if not args:
            print("Please choose a key, for example: key E")
            print("Try one of:", ", ".join(sorted(keySignatureMap.keys())))
            return
        FUNCTIONS[func_name](" ".join(args))
        return

    if func_name in ["scale", "scale_from_key"]:
        if not args:
            print("Please choose a key, for example: scale G")
            return
        FUNCTIONS[func_name](" ".join(args))
        return

    if func_name in ["chord", "chord_from_key"]:
        if not args:
            print("Please choose a key, for example: chord G")
            return
        FUNCTIONS[func_name](" ".join(args))
        return

    if func_name == "chords":
        FUNCTIONS[func_name]()
        return

    if func_name == "scales":
        FUNCTIONS[func_name]()
        return

    if func_name == "modes":
        if not args:
            FUNCTIONS[func_name]()
            return
        FUNCTIONS["modes_from_key"](" ".join(args))
        return

    if func_name == "modes_from_key":
        if not args:
            print("Please choose a key, for example: modes C")
            return
        FUNCTIONS[func_name](" ".join(args))
        return

    if func_name == "mnemonic":
        if not args:
            print("Please choose 'sharp' or 'flat'.")
            return
        FUNCTIONS[func_name](" ".join(args))
        return

    if func_name == "bassfret":
        if not args:
            FUNCTIONS[func_name]()
            return
        subcommand = args[0].lower()
        if subcommand in ["--help", "-h", "help"]:
            show_bassfret_help()
            return
        if subcommand in ["money", "money_notes", "notes"]:
            FUNCTIONS["bassfret_money"]()
            return
        if subcommand in ["interval", "intervals"]:
            FUNCTIONS["bassfret_intervals"]()
            return
        if subcommand in ["compare", "comparison"]:
            FUNCTIONS["bassfret_compare"]()
            return
        if subcommand in ["scales"]:
            FUNCTIONS["bassfret_compare"]()
            return
        if subcommand in ["scale"]:
            if len(args) > 1:
                FUNCTIONS["bassfret_scale"](" ".join(args[1:]))
            else:
                FUNCTIONS["bassfret_compare"]()
            return
        FUNCTIONS[func_name]()
        return

    if func_name in ["transpose", "transpose_key"]:
        if not args:
            FUNCTIONS[func_name]()
            return
        if len(args) == 1:
            FUNCTIONS[func_name](args[0])
            return
        FUNCTIONS[func_name](args[0], args[1])
        return

    if func_name == "quiz":
        if args:
            FUNCTIONS[func_name](" ".join(args))
        else:
            FUNCTIONS[func_name]()
        return

    FUNCTIONS[func_name]()

# Create block to accept user argument input
# This is the actual CLI entry point for the script and the installed command.
def main_entry(argv=None):
    args = sys.argv[1:] if argv is None else argv

    if len(args) == 0:
        show_help()
        return 1

    main(args[0], *args[1:])
    return 0


if __name__ == "__main__":
    raise SystemExit(main_entry())
