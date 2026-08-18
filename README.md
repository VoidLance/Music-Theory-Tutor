# Musor

## Install from a GitHub release (recommended)

The easiest way for most users is to install the published wheel from the release assets.

1. Open the latest GitHub release.
2. Download the wheel file from the release assets.
3. Install it with pip.

### Linux / macOS

```bash
python -m pip install musor-<version>-py3-none-any.whl
```

### Windows

```powershell
py -m pip install musor-<version>-py3-none-any.whl
```

This is the normal install path on all platforms. The wheel is the standard Python package format and is the recommended way to install Musor.

### Source archive fallback (Linux / macOS only)

If you want the source archive instead of the wheel, use the `.tar.gz` file only on Unix-like systems:

```bash
python -m pip install musor-<version>.tar.gz
```

### Windows source-code option (not the normal install path)

If you want the source code instead of the packaged wheel, Windows users usually do one of these:

- clone the repository with Git, or
- download the ZIP archive from the GitHub releases page or repository page.

This is a source-access route, not the usual install path. It is useful if you want to inspect the code, run the project directly from a checkout, or install it in editable mode for development.

To use the ZIP file on Windows:

1. Open the GitHub repository page.
2. Click the Code button.
3. Choose Download ZIP.
4. Extract the ZIP to a place you can easily find, such as your Desktop or a folder like `Music-Theory-Tutor`.
5. Open PowerShell in the extracted folder.
6. Create a virtual environment and activate it:

```powershell
cd path\to\Music-Theory-Tutor
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

7. Install the project in editable mode:

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

8. Run the app:

```powershell
musor quiz
```

If you prefer to use Git instead of the ZIP file, the steps are similar:

```powershell
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
musor quiz
```

This route is for source access and development. For normal use, the wheel install above is the simpler and more standard option.

Then verify the install and launch the app:

```bash
musor --help
musor quiz
```

## Installing on Windows without stress

If you are a beginner or you just want the least-frustrating setup, follow this exact order.

### Windows beginner setup

1. Install Python 3.11 or 3.12 from https://www.python.org/downloads/windows/
   - Make sure the box that says “Add Python to PATH” is checked.
2. Install Git from https://git-scm.com/download/win
3. Open PowerShell.
4. Run these commands exactly as written:

```powershell
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
musor quiz
```

If PowerShell blocks scripts, run this once and then try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

If you prefer Command Prompt instead, this also works:

```cmd
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -e .
musor quiz
```

If the `musor` command is not found, close the terminal, reopen it, and try again. Windows sometimes needs a fresh terminal before new scripts appear in PATH.

## Install from source or for development

If you want to work on the project locally or run it from a checkout instead of the release package:

### Linux / macOS

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

### Windows (development)

```powershell
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
musor quiz
```

### Fish shell users

```fish
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 -m venv .venv
source .venv/bin/activate.fish
python -m pip install -e .
musor quiz
```

## One-line install summary

- Linux / macOS release install: `python -m pip install musor-<version>-py3-none-any.whl`
- Windows release install: `py -m pip install musor-<version>-py3-none-any.whl`
- Linux / macOS source archive fallback: `python -m pip install musor-<version>.tar.gz`
- Development install: `python -m pip install -e .`
- Run app: `musor quiz`

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
```

On Windows, use the same idea with your virtual environment activated:

```powershell
cd Music-Theory-Tutor
git pull --ff-only
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

If you installed the project with `pipx`, update from the repository instead of reinstalling the whole app manually:

```bash
cd Music-Theory-Tutor
git pull --ff-only
pipx install . --force
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
