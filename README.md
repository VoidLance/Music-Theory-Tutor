# Tonal

Tonal is a terminal-based music theory learning app built around a much broader purpose than a simple key-signature lookup tool.

It began with key signatures because they are one of the most useful foundations in music study, but the real intention is to grow this into a wider music theory tutor that helps a learner understand how music works in a practical and memorable way. The app is designed to be approachable, fast to use, and easy to expand as the project develops.

## The real purpose

This is not just a reference app for sharps, flats, and key signatures. The actual goal is to create a music theory companion that helps with understanding and recall across a much wider range of topics.

At the moment, the project already covers the fundamentals:
- the order of sharps and flats
- mnemonics for remembering those patterns
- major and minor key signatures
- relative major/minor relationships
- natural minor scales
- a simple quiz mode

But this is only the first layer. The longer-term direction is to turn this into a broader music theory tool for learning, revision, and practical application, especially in areas relevant to bass guitar and cello study.

That future direction includes topics such as:
- intervals
- scale patterns
- chord construction
- tonal relationships
- key feel and practical application
- instrument-focused study habits for bass and cello players

## Why this project exists

This project serves two roles at once:

1. It is a useful learning aid for music theory, especially for beginners who need quick, clear, and repeatable reference material.
2. It is also a programming portfolio project, designed to show clean Python structure, CLI design, and a maintainable project layout that can grow over time.

The code is intentionally kept modular so the app can expand naturally without becoming a single giant script.

## Download from GitHub and run with Python

If you want to use the project without installing it system-wide, clone the repository and run it directly from the source folder.

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 main.py keys
```

This is the simplest option if you just want to try the app or work on the project locally.

You can also run other commands directly from the repository root:

```bash
python3 main.py sharp_order
python3 main.py flat_order
python3 main.py mnemonic sharp
python3 main.py key Dm
python3 main.py quiz
```

If you prefer to keep the project in a virtual environment, you can do that too:

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 -m venv .venv
source .venv/bin/activate
python main.py keys
```

## Install to your PATH and run as a command

If you want to use the app as a normal shell command such as `tonal keys`, install it in editable mode and add the Python scripts directory to your PATH.

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 -m pip install --user -e .
```

After installation, make sure your user scripts directory is available on PATH.

On Linux/macOS, the usual location is:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

To make it permanent in bash:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

Or in fish:

```fish
echo 'set -gx PATH $HOME/.local/bin $PATH' >> ~/.config/fish/config.fish
```

Then restart your terminal or reload your shell config. After that, the app should be available as:

```bash
tonal keys
tonal key Dm
tonal key F
tonal mnemonic sharp
tonal quiz
```

## Example usage

```bash
tonal sharp_order
tonal flat_order
tonal mnemonic sharp
tonal key G
tonal minor_keys
tonal quiz
```

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

This separation keeps the project maintainable while leaving room for additional theory modules, practice tools, and instrument-focused features as the app grows.
