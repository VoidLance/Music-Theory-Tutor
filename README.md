# Tonal

Quick start for Arch/CachyOS users:

```bash
cd /mnt/1TB-HDD/Python
rm -rf "Music Theory Tutor"
git clone https://github.com/VoidLance/Music-Theory-Tutor.git "Music Theory Tutor"
cd "Music Theory Tutor"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Then run:

```bash
tonal quiz
```

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

## Clean reinstall / update from a fresh clone

If the project directory already exists or a previous install failed, remove the old folder and start from a fresh copy before trying again.

```bash
cd /mnt/1TB-HDD/Python
rm -rf "Music Theory Tutor"
git clone https://github.com/VoidLance/Music-Theory-Tutor.git "Music Theory Tutor"
cd "Music Theory Tutor"
```

This avoids the repeated `fatal: destination path ... already exists` error and ensures you are working in the actual project directory.

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

On Arch-based systems such as CachyOS, `python3 -m pip install --user -e .` often fails because the system Python is in an externally managed environment. The most reliable way to install this project as a normal shell command is through `pipx`, which creates its own virtual environment and exposes the `tonal` entry point without touching the system Python.

If the repo is already present locally, skip the `git clone` step and change into the actual project directory:

```bash
cd /path/to/Music-Theory-Tutor
```

If you want a clean reinstall, remove the old folder first:

```bash
rm -rf /path/to/Music-Theory-Tutor
git clone https://github.com/VoidLance/Music-Theory-Tutor.git /path/to/Music-Theory-Tutor
cd /path/to/Music-Theory-Tutor
```

Then install it with `pipx`:

```bash
sudo pacman -S python-pipx
pipx install .
```

If `pipx` is already installed, you can skip the `pacman` step and run just:

```bash
pipx install .
```

After installation, the command should be available directly as:

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

If you prefer not to use `pipx`, you can still install in a local virtual environment and call the script from that environment:

```bash
cd /path/to/Music-Theory-Tutor
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

In fish, use:

```fish
source /path/to/Music-Theory-Tutor/.venv/bin/activate.fish
```

Then run commands from that environment, or add an alias that points to the exact project path on disk, not a guessed one.

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
