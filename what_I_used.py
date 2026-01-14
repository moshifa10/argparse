"""
ARGPARSE KEYWORDS & CONCEPTS SUMMARY
===================================

This file contains ALL argparse keywords and concepts I used,
with short, clear explanations.

Use this as a revision / cheat-note file.
"""

# ---------------------------------------------------------
# MODULE
# ---------------------------------------------------------

import argparse
# argparse:
# Standard Python module used to create Command Line Interfaces (CLI).
# It converts terminal input into Python variables safely.

# ---------------------------------------------------------
# CORE OBJECT
# ---------------------------------------------------------

argparse.ArgumentParser
# Creates the main parser object.
# It defines what arguments the program accepts and generates help messages.

# Example:
# parser = argparse.ArgumentParser(description="My CLI app")

# ---------------------------------------------------------
# ADDING ARGUMENTS
# ---------------------------------------------------------

parser.add_argument
# Defines an argument that the CLI accepts.
# Can be positional or optional.

# ---------------------------------------------------------
# POSITIONAL ARGUMENTS
# ---------------------------------------------------------

"name"
# Positional argument.
# - Required by default
# - Does NOT use --
# - Order matters

# Example:
# python app.py Njabulo

# ---------------------------------------------------------
# OPTIONAL ARGUMENTS
# ---------------------------------------------------------

"--age"
# Optional argument.
# - Uses --
# - Can be required or optional
# - Order does not matter

# Example:
# python app.py --age 21

# ---------------------------------------------------------
# SHORT & LONG FLAGS
# ---------------------------------------------------------

"-u", "--upper"
# Short (-u) and long (--upper) versions of the same argument.
# Common in real-world CLIs.

# ---------------------------------------------------------
# PARSING ARGUMENTS
# ---------------------------------------------------------

parser.parse_args
# Reads arguments from the command line.
# Returns an object containing all parsed values.

# Example:
# args = parser.parse_args()

# ---------------------------------------------------------
# ACCESSING VALUES
# ---------------------------------------------------------

args.name
args.age
args.score
# Accesses the value of an argument after parsing.
# Stored as attributes of the args object.

# ---------------------------------------------------------
# HELP TEXT
# ---------------------------------------------------------

help
# Describes what an argument does.
# Shown when user runs: -h or --help

# Example:
# parser.add_argument("--age", help="Your age")

# ---------------------------------------------------------
# TYPE CONVERSION
# ---------------------------------------------------------

type=int
# Converts input from string to integer.
# Prevents invalid data types.

# Example:
# parser.add_argument("--age", type=int)

# ---------------------------------------------------------
# REQUIRED ARGUMENTS
# ---------------------------------------------------------

required=True
# Forces the user to provide the argument.
# Mostly used with optional arguments.

# Example:
# parser.add_argument("--score", required=True)

# ---------------------------------------------------------
# BOOLEAN FLAGS
# ---------------------------------------------------------

action="store_true"
# Creates a flag.
# - False if not provided
# - True if provided

# Example:
# --reverse
# --upper

# ---------------------------------------------------------
# MULTIPLE VALUES
# ---------------------------------------------------------

nargs="+"
# Allows one or more values for a single argument.
# Values are stored as a list.

# Example:
# python add.py 1 2 3 4

# ---------------------------------------------------------
# CHOICES (INPUT VALIDATION)
# ---------------------------------------------------------

choices=["A", "B", "C"]
# Restricts input to specific allowed values.
# argparse automatically throws errors for invalid input.

# Example:
# parser.add_argument("--grade", choices=["A", "B", "C"])

# ---------------------------------------------------------
# DESCRIPTION
# ---------------------------------------------------------

description
# Describes what the program does.
# Appears at the top of the help output.

# Example:
# argparse.ArgumentParser(description="My program")

# ---------------------------------------------------------
# FLAGS VS VALUES
# ---------------------------------------------------------

"--reverse"
# Flag (no value required)

"--age 21"
# Argument with a value


# ---------------------------------------------------------
# WHAT ARGPARSE HANDLES AUTOMATICALLY
# ---------------------------------------------------------

# - Error messages
# - Missing required arguments
# - Invalid choices
# - Help screen (-h / --help)

# ---------------------------------------------------------
# FINAL SUMMARY
# ---------------------------------------------------------

"""
KEY TAKEAWAY
============

Argparse turns terminal input into validated Python variables.

I now know how to:
- Accept user input from the terminal
- Validate and restrict input
- Use flags to control program behavior
- Build real CLI tools like git, pip, and docker
"""
