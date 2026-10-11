# Python Password Strength Checker

A privacy-conscious command-line tool that evaluates password strength using length, character variety, common-password detection, predictable sequences, and repetition checks.

## Features

- Scores passwords from 0 to 100
- Assigns strength ratings from `VERY WEAK` to `STRONG`
- Checks length and character diversity
- Detects common passwords
- Detects predictable sequences
- Detects repeated characters
- Provides improvement recommendations
- Hides password input using Python's `getpass`
- Does not store or transmit passwords

## Security and Privacy

Password input is hidden from the terminal and processed only in memory. The program does not save, log, or transmit the entered password.

Never test a real password on software you do not trust.

## Requirements

- Python 3.10 or newer
- No third-party packages required

## Usage

Run the program:

```bash
python3 password_checker.py
```

Enter a test password when prompted. Nothing will appear while typing because terminal input is intentionally hidden.

Example result:

```text
Security assessment
Score:  90/100
Rating: STRONG

No basic weaknesses were detected.
```

## Checks Performed

- Minimum recommended length
- Uppercase letters
- Lowercase letters
- Numbers
- Symbols
- Character variety
- Common-password matches
- Common words and sequences
- Repeated characters

## Important Limitation

A high score does not prove that a password is safe or that it has never appeared in a breach. This project performs local rule-based analysis and does not query breach databases.

## Skills Demonstrated

- Python functions
- Regular expressions
- Sets and collections
- Secure terminal input
- Input analysis and scoring
- Defensive programming
- Privacy-conscious software design
- Git version control

## Author

Created by [RuDonny](https://github.com/RuDonny) as part of a cybersecurity portfolio.
