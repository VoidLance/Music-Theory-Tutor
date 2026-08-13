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

## Installation

### Option 1: local usage with Python directly

From the project folder:

```bash
cd /path/to/Tonal
python3 -m pip install --user -e .
```

This installs the project in editable mode so it can be run as a normal terminal command.

### Option 2: run it directly from the repository

```bash
cd /path/to/Tonal
python3 main.py keys
```

## Running it as a terminal app

After installing with the editable install above, the command is available as:

```bash
tonal keys
```

You can also look up a specific key:

```bash
tonal key Dm
tonal key F
tonal key A minor
```

The quiz is available with:

```bash
tonal quiz
```

## Adding it to your PATH

If the command is not found, add the user Python scripts directory to your PATH.

On Linux/macOS, the usual location is:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

To make that permanent, add the line above to your shell profile, for example:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

or for fish:

```fish
echo 'set -gx PATH $HOME/.local/bin $PATH' >> ~/.config/fish/config.fish
```

Then restart your terminal or reload your config.

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
└── theorytutor/
    ├── __init__.py
    ├── cli.py
    ├── data.py
    └── quiz.py
```

This separation keeps the project maintainable while leaving room for additional theory modules, practice tools, and instrument-focused features as the app grows.
