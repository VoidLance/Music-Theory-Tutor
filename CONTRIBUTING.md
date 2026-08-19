# Contributing to Musor

Thanks for your interest in improving Musor. Contributions are welcome, whether they are bug fixes, new quiz content, UX improvements, or documentation updates.

## How to contribute

1. Fork the repository and create a feature branch.
2. Set up the project locally:

```bash
git clone https://github.com/VoidLance/Music-Theory-Tutor.git
cd Music-Theory-Tutor
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

3. Make your change in a focused, well-tested way.
4. Run a quick verification for the changed behavior.
5. Open a pull request with a clear summary of the change and any relevant context.

## Project expectations

- Keep changes small and easy to review.
- Prefer clear, readable Python and documentation updates.
- If you add a feature, explain the use case and expected outcome.
- If you fix a bug, include the problem, root cause, and validation.
- Maintain a friendly, respectful tone in comments and discussions.

## Documentation

If you change behavior, installation steps, or user-facing commands, update the relevant documentation in the repository, especially the README and any help text in the CLI.

## Code quality

This project is intentionally lightweight. Please keep code idiomatic, readable, and compatible with the supported Python versions in the project configuration.

Before opening a PR, use the project in the way you changed it. For example:

```bash
musor --help
musor quiz
```

If there are automated tests in the repository, run them as part of your validation before submitting the PR.

## Reporting issues

Please use the issue templates in the repository to report bugs or suggest features. Clear reproduction steps, expected behavior, and actual behavior are very helpful.

## Pull requests

Please include:

- a brief summary of the change
- the reason for the change
- validation steps you performed
- any follow-up work or known limitations

If your pull request touches music theory logic, a short explanation of the domain rule or behavior being corrected is appreciated.

## Code of conduct

This project follows the Contributor Covenant. By participating, you agree to uphold the standards described in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
