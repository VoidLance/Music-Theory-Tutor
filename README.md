# Tonal

Tonal is a terminal-based music theory learning app built for practical understanding, not just reference lookup.

It began with key signatures because they are one of the most important foundations in music study, but it has grown into a wider tutor for learning intervals, scales, chords, modes, transposition, fretboard navigation, and beginner-friendly instrument study.

## What the app covers

The project now includes a practical mix of theory and teaching tools:

- key signatures and related mnemonics
- major and minor keys
- scales and scale-building explanations
- chords and triads
- modes and modal feel
- circle of fifths and key relationships
- transposition and interval-based thinking
- bass fretboard guidance and scale study
- cello guidance for beginner home position and staff reading
- composition and musical analysis guides
- quizzes for each topic and a combined quiz

This is designed to help a learner understand how music works in a practical, memorable way rather than just memorising isolated facts.

## Download from GitHub and run with Python

If you want to use the project without installing it system-wide, clone the repository and run it from source.

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 main.py keys
```

This is the simplest option if you want to try the app locally or work on the project without a global install.

You can run other commands directly from the repository root:

```bash
python3 main.py sharp_order
python3 main.py flat_order
python3 main.py mnemonic sharp
python3 main.py key Dm
python3 main.py scale G
python3 main.py chord G
python3 main.py modes
python3 main.py bassfret
python3 main.py cello
python3 main.py quiz
```

If you prefer to keep the project in a virtual environment:

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 -m venv .venv
source .venv/bin/activate
python main.py keys
```

## Install to your PATH and run as a command

If you want to use the app as a normal shell command such as `tonal keys`, install it in editable mode and make sure your user scripts directory is on PATH.

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 -m pip install --user -e .
```

On Linux/macOS, the usual scripts directory is:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

To make that permanent in bash:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

Or in fish:

```fish
echo 'set -gx PATH $HOME/.local/bin $PATH' >> ~/.config/fish/config.fish
```

Then restart your terminal or reload your shell. After that, the app should be available as:

```bash
tonal keys
tonal key Dm
tonal key F
tonal mnemonic sharp
tonal scale G
tonal chord G
tonal modes
tonal bassfret
tonal cello
tonal quiz
```

## Example usage

```bash
tonal sharp_order
tonal flat_order
tonal mnemonic sharp
tonal key G
tonal minor_keys
tonal scale C
tonal chord F
tonal circle_of_fifths
tonal transposition
tonal bassfret money
tonal bassfret intervals
tonal cello
tonal quiz
```

## Quick reference for the main learning areas

- Keys and signatures: `tonal keys`, `tonal key G`, `tonal mnemonic sharp`
- Scales and modes: `tonal scale G`, `tonal modes`, `tonal modes C`
- Chords: `tonal chord G`
- Circle of fifths: `tonal circle_of_fifths`
- Transposition: `tonal transposition`, `tonal transpose C G`
- Bass fretboard: `tonal bassfret`, `tonal bassfret money`, `tonal bassfret intervals`
- Cello: `tonal cello`
- Quizzes: `tonal quiz`

## Project structure

```text
.
├── README.md
├── main.py
├── pyproject.toml
└── tonal/
    ├── __init__.py
    ├── cli.py
    ├── data.py
    └── quiz.py
```

This layout keeps the project maintainable while leaving room for more lessons, practice tools, and instrument-focused guides as the app continues to grow.
