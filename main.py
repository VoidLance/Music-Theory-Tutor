# This is the minimal wrapper for the app.
# The actual logic now lives in the tonal package so the project stays easier to maintain as it grows.
from tonal.cli import main_entry

if __name__ == "__main__":
    raise SystemExit(main_entry())
