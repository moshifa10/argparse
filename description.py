"""
ARGPARSE LEARNING SUMMARY
========================

This file documents what I learned about argparse by building
multiple small CLI (Command Line Interface) programs.

Argparse allows Python programs to accept input from the terminal
in a clean, safe, and professional way.

Everything below is explained clearly so I can revise later.
"""

import argparse

# ---------------------------------------------------------
# BASIC IDEA OF ARGPARSE
# ---------------------------------------------------------
"""
1. Create an ArgumentParser object
2. Define arguments using add_argument()
3. Read inputs using parse_args()
4. Access inputs using args.<argument_name>
"""

# ---------------------------------------------------------
# CHALLENGE 1: NAME + UPPERCASE FLAG
# ---------------------------------------------------------
"""
Goal:
- Take a positional argument: name
- Add a flag --upper
- If --upper is present, print the name in uppercase
"""

parser = argparse.ArgumentParser(
    description="Takes a name and optionally prints it in uppercase"
)

# Positional argument (required, no --)
parser.add_argument(
    "name",
    help="Your name"
)

# Optional flag
parser.add_argument(
    "-u", "--upper",
    action="store_true",
    help="Convert name to uppercase"
)

args = parser.parse_args()

if args.upper:
    print(f"HELLO {args.name.upper()}")
else:
    print(f"Hello {args.name}")

# ---------------------------------------------------------
# WHAT I LEARNED HERE:
# - Positional arguments do not use --
# - action='store_true' creates a boolean flag
# - args.upper is True only if --upper is provided
# ---------------------------------------------------------


# ---------------------------------------------------------
# CHALLENGE 2: AGE INPUT
# ---------------------------------------------------------
"""
Goal:
- Take an age using --age
- Make it required
- Convert input to an integer
"""

parser = argparse.ArgumentParser(
    description="Takes age as input"
)

parser.add_argument(
    "--age",
    type=int,           # convert input to integer
    required=True,      # user must provide this
    help="Your age"
)

args = parser.parse_args()

print(f"You are {args.age} years old.")

# ---------------------------------------------------------
# WHAT I LEARNED HERE:
# - type=int converts string input to numbers
# - required=True forces the argument to be supplied
# ---------------------------------------------------------


# ---------------------------------------------------------
# CHALLENGE 3: ADD MULTIPLE NUMBERS
# ---------------------------------------------------------
"""
Goal:
- Take multiple numbers as positional arguments
- Add them together
"""

parser = argparse.ArgumentParser(
    description="Adds multiple numbers"
)

parser.add_argument(
    "numbers",
    type=int,
    nargs="+",          # accepts one or more values
    help="Numbers to add"
)

args = parser.parse_args()

print(f"Result: {sum(args.numbers)}")

# ---------------------------------------------------------
# WHAT I LEARNED HERE:
# - nargs='+' allows multiple values
# - argparse stores them as a list
# - sum() can be used directly on the list
# ---------------------------------------------------------


# ---------------------------------------------------------
# CHALLENGE 4: REVERSE TEXT FLAG
# ---------------------------------------------------------
"""
Goal:
- Take text as a positional argument
- Add --reverse flag
- Reverse text only if flag is present
"""

parser = argparse.ArgumentParser(
    description="Optionally reverse text"
)

parser.add_argument(
    "text",
    help="Text input"
)

parser.add_argument(
    "--reverse",
    action="store_true",
    help="Reverse the text"
)

args = parser.parse_args()

if args.reverse:
    print(args.text[::-1])   # string slicing to reverse
else:
    print(args.text)

# ---------------------------------------------------------
# WHAT I LEARNED HERE:
# - Flags control program behavior
# - Python slicing can reverse strings
# ---------------------------------------------------------


# ---------------------------------------------------------
# CHALLENGE 5: SCORE + GRADE (CHOICES)
# ---------------------------------------------------------
"""
Goal:
- Take a score (number)
- Take a grade (A, B, or C only)
- Print both values
"""

parser = argparse.ArgumentParser(
    description="Score and grade input"
)

parser.add_argument(
    "--score",
    type=int,
    required=True,
    help="Your score"
)

parser.add_argument(
    "--grade",
    required=True,
    choices=["A", "B", "C"],   # restrict allowed values
    help="Your grade"
)

args = parser.parse_args()

print(f"Score: {args.score} | Grade: {args.grade}")

# ---------------------------------------------------------
# WHAT I LEARNED HERE:
# - choices limits user input safely
# - argparse automatically validates input
# - Invalid values show clean error messages
# ---------------------------------------------------------


"""
FINAL SUMMARY
=============

By completing these challenges, I learned how to:

- Create CLI programs using argparse
- Use positional and optional arguments
- Use flags with action='store_true'
- Validate input using type, required, and choices
- Accept multiple values using nargs
- Read arguments using args.<name>

This is the foundation of professional Python CLI tools.
"""
