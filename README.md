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

If you prefer to keep the project in a virtual environment, first make sure you are in the repo directory. If you have not cloned it yet, do this once:

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
```

Then create and activate the virtual environment:

```bash
python3 -m venv .venv
```

In bash/zsh:

```bash
source .venv/bin/activate
```

In fish:

```fish
source .venv/bin/activate.fish
```

After that, run the app from the active environment:

```bash
python main.py keys
```

## Install as a shell command

On Arch-based systems such as CachyOS, `python3 -m pip install --user -e .` often fails because the system Python is in an externally managed environment. The safe approach is to create a virtual environment for the project, install the package there, and then expose the generated `tonal` command via your shell.

If the repo is already present locally, skip the `git clone` step and just change into the project directory:

```bash
cd Music-Theory-Tutor
```

If you want to reinstall or update from a fresh copy and the folder already exists, remove it and clone again:

```bash
rm -rf Music-Theory-Tutor
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
```

Then create the environment and install the project:

```bash
python3 -m venv .venv
```

In bash/zsh:

```bash
source .venv/bin/activate
python -m pip install -e .
```

In fish:

```fish
source .venv/bin/activate.fish
python -m pip install -e .
```

If you want to avoid the activation step entirely, you can call the venv Python directly:

```bash
./.venv/bin/python -m pip install -e .
```

After installation, add the command to your shell so you can call it as `tonal`.

First, verify that the entry point was actually created in the virtual environment:

```bash
ls .venv/bin/tonal
```

If that file exists, then in fish a simple alias is the least invasive option:

```fish
alias tonal "$PWD/.venv/bin/tonal"
```

To make that alias permanent:

```fish
echo 'alias tonal "$PWD/.venv/bin/tonal"' >> ~/.config/fish/config.fish
```

Or, if you prefer to make the executable available on your `PATH`:

```fish
mkdir -p ~/.local/bin
ln -sf "$PWD/.venv/bin/tonal" ~/.local/bin/tonal
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
