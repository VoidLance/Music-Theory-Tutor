# Musor

Quick start for most Linux/macOS users:

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Then run:

```bash
musor quiz
```

## Windows quick start (recommended for beginners)

If you are on Windows and want the simplest setup, use this exact order:

1. Install Python 3.11 or 3.12 from https://www.python.org/downloads/windows/
   - Make sure the installer box for “Add Python to PATH” is checked.
2. Install Git from https://git-scm.com/download/win
3. Open PowerShell or Command Prompt.
4. Run these commands:

```powershell
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
musor quiz
```

If PowerShell says script execution is blocked, run this once and then try the activation step again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

If you prefer Command Prompt instead of PowerShell, this works too:

```cmd
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -e .
musor quiz
```

If the command `musor` is not found after install, close and reopen the terminal, then try again. Sometimes Windows needs a fresh terminal before the new entry point appears.

Musor is a terminal-based music theory learning app built for practical understanding, not just reference lookup.

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
rm -rf Music-Theory-Tutor
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
```

This avoids the repeated `fatal: destination path ... already exists` error and ensures you are working in the actual project directory.

## Update the app

If you installed the app from a local clone, update it like this:

```bash
cd Music-Theory-Tutor
git pull --ff-only
source .venv/bin/activate
python -m pip install -e .
musor quiz
```

On Windows, use the same idea with your virtual environment activated:

```powershell
cd Music-Theory-Tutor
git pull --ff-only
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
musor quiz
```

If you installed the project with `pipx`, update from the repository instead of reinstalling the whole app manually:

```bash
cd Music-Theory-Tutor
git pull --ff-only
pipx install . --force
musor quiz
```

If you made local edits, commit or stash them before running `git pull` so you do not lose any work.

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

On Arch-based systems such as CachyOS, `python3 -m pip install --user -e .` often fails because the system Python is in an externally managed environment. The most reliable way to install this project as a normal shell command is through `pipx`, which creates its own virtual environment and exposes the `musor` entry point without touching the system Python.

If the repo is already present locally, skip the `git clone` step and change into the actual project directory:

```bash
cd Music-Theory-Tutor
```

If you want a clean reinstall, remove the old folder first:

```bash
rm -rf Music-Theory-Tutor
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
```

Then install it with `pipx`:

```bash
# Arch / CachyOS
sudo pacman -S python-pipx
pipx install .
```

If `pipx` is already installed, you can skip the `pacman` step and run just:

```bash
pipx install .
```

After installation, remove any stale alias that still points to the old broken path before testing:

```fish
functions -e musor
```

Then add the correct alias for the current install:

```fish
alias musor "$HOME/.local/bin/musor"
```

If you installed via `pipx`, this is the correct alias for most users on Linux and macOS. If you installed in a project-local virtual environment instead, use:

```fish
alias musor "$PWD/Music-Theory-Tutor/.venv/bin/musor"
```

Then test:

```bash
musor keys
musor key Dm
musor key F
musor mnemonic sharp
musor scale G
musor chord G
musor modes
musor bassfret
musor cello
musor quiz
```

If you prefer not to use `pipx`, you can still install in a local virtual environment and call the script from that environment:

```bash
cd Music-Theory-Tutor
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

In fish, use:

```fish
source ./Music-Theory-Tutor/.venv/bin/activate.fish
```

To make the command available as `musor` from a project-local venv, add:

```fish
functions -e musor
alias musor "$PWD/Music-Theory-Tutor/.venv/bin/musor"
```

To make the alias permanent in fish:

```fish
echo 'functions -e musor' >> ~/.config/fish/config.fish
echo 'alias musor "$HOME/Music-Theory-Tutor/.venv/bin/musor"' >> ~/.config/fish/config.fish
```

Then reload your shell and run commands from that environment.

## Example usage

```bash
musor sharp_order
musor flat_order
musor mnemonic sharp
musor key G
musor minor_keys
musor scale C
musor chord F
musor circle_of_fifths
musor transposition
musor bassfret money
musor bassfret intervals
musor cello
musor quiz
```

## Quick reference for the main learning areas

- Keys and signatures: `musor keys`, `musor key G`, `musor mnemonic sharp`
- Scales and modes: `musor scale G`, `musor modes`, `musor modes C`
- Chords: `musor chord G`
- Circle of fifths: `musor circle_of_fifths`
- Transposition: `musor transposition`, `musor transpose C G`
- Bass fretboard: `musor bassfret`, `musor bassfret money`, `musor bassfret intervals`
- Cello: `musor cello`
- Quizzes: `musor quiz`

## Project structure

```text
.
├── README.md
├── main.py
├── pyproject.toml
└── musor/
    ├── __init__.py
    ├── cli.py
    ├── data.py
    └── quiz.py
```

This layout keeps the project maintainable while leaving room for more lessons, practice tools, and instrument-focused guides as the app continues to grow.
