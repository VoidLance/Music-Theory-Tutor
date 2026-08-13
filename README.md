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

## Install as a shell command

On Arch-based systems such as CachyOS, `python3 -m pip install --user -e .` often fails because the system Python is in an externally managed environment. The safe approach is to create a virtual environment for the project, install the package there, and then expose the generated `tonal` command via your shell.

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

After that, you can either add the venv's `bin` directory to your `PATH` for the current shell:

```bash
export PATH="$PWD/.venv/bin:$PATH"
```

Or create a simple alias so you can call the app as `tonal` without permanently changing your `PATH`:

```fish
alias tonal "$HOME/Music-Theory-Tutor/.venv/bin/tonal"
```

To make that alias permanent in fish:

```fish
echo 'alias tonal "$HOME/Music-Theory-Tutor/.venv/bin/tonal"' >> ~/.config/fish/config.fish
```

If you prefer to add the script to your `PATH` instead, a common option is:

```fish
mkdir -p ~/.local/bin
ln -sf "$HOME/Music-Theory-Tutor/.venv/bin/tonal" ~/.local/bin/tonal
set -gx PATH $HOME/.local/bin $PATH
```

Then reload your shell or run:

```fish
source ~/.config/fish/config.fish
```

After that, the app is available as:

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
