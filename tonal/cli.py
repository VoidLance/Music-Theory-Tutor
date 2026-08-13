import sys

# This is the command-line entry for the app.
# It keeps the menu system separate from the music-theory logic, which makes it easier to keep extending the project without crowding everything into one file.

from .data import (
    flat_keys,
    flat_order,
    keySignatureMap,
    key_signature,
    keys,
    minor_keys,
    mnemonic,
    sharp_keys,
    sharp_order,
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
    "key": key_signature,
    "key_signature": key_signature,
    "mnemonic": mnemonic,
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

    if func_name == "mnemonic":
        if not args:
            print("Please choose 'sharp' or 'flat'.")
            return
        FUNCTIONS[func_name](" ".join(args))
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
