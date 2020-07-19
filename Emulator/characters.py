#!/usr/bin/env python3
"""
Dict with letters and numbers and corresponding bytes.
Copied from ZeroSeg library.
"""

UNDEFINED = 0x08

CHARS = {
    " ": 0x00,
    "-": 0x01,
    "_": 0x08,
    "0": 0x7E,
    "1": 0x30,
    "2": 0x6D,
    "3": 0x79,
    "4": 0x33,
    "5": 0x5B,
    "6": 0x5F,
    "7": 0x70,
    "8": 0x7F,
    "9": 0x7B,
    "a": 0x7D,
    "b": 0x1F,
    "c": 0x0D,
    "d": 0x3D,
    "e": 0x6F,
    "f": 0x47,
    "g": 0x7B,
    "h": 0x17,
    "i": 0x10,
    "j": 0x18,
    # 'k': cant represent
    "l": 0x06,
    # 'm': cant represent
    "n": 0x15,
    "o": 0x1D,
    "p": 0x67,
    "q": 0x73,
    "r": 0x05,
    "s": 0x5B,
    "t": 0x0F,
    "u": 0x1C,
    "v": 0x1C,
    # 'w': cant represent
    # 'x': cant represent
    "y": 0x3B,
    "z": 0x6D,
    "A": 0x77,
    "B": 0x7F,
    "C": 0x4E,
    "D": 0x7E,
    "E": 0x4F,
    "F": 0x47,
    "G": 0x5E,
    "H": 0x37,
    "I": 0x30,
    "J": 0x38,
    # 'K': cant represent
    "L": 0x0E,
    # 'M': cant represent
    "N": 0x76,
    "O": 0x7E,
    "P": 0x67,
    "Q": 0x73,
    "R": 0x46,
    "S": 0x5B,
    "T": 0x0F,
    "U": 0x3E,
    "V": 0x3E,
    # 'W': cant represent
    # 'X': cant represent
    "Y": 0x3B,
    "Z": 0x6D,
    ",": 0x80,
    ".": 0x80,
}
