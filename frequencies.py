"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        frequencies[str(i)] = frequencies[str(i)] + 1 if str(i) in frequencies.keys() else 1
    return frequencies
