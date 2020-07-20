#!/usr/bin/env python3
"""
Implementation of ZeroSeg library methods with corresponding
behaviour but displayed on emulator display.
"""

from Emulator.characters import CHARS, UNDEFINED

METHOD = []


class Screen:
    """
    Representation of `screen` object from ZeroSeg library.
    """
    def __init__(self):
        pass

    def set_byte(self, value: int, position: int, redraw: bool = True):
        METHOD.append(f"draw_symbol(str(hex({value})), {position})")
        # TODO: redraw

    def __get_byte_by_char(self, char: str) -> int:
        return hex(CHARS.get(str(char), UNDEFINED))

    def write_char(
        self, char: str, position: int = 1, dot: bool = False, redraw: bool = True
    ):
        value = self.__get_byte_by_char(char)
        METHOD.append(f"draw_symbol({str(value)}, {position})")
        # TODO: redraw

    def write_number(
        self,
        value: float,
        base: int = 10,
        decimal_places: int = 0,
        zero_pad: bool = False,
        left_justify: bool = False,
    ):
        self.clear()
        if zero_pad:
            pass

        if decimal_places > 0:
            pass

        value = list(str(value))
        value.reverse()
        _bytes = []
        for i in value:
            byte = str(self.__get_byte_by_char(str(i)))
            _bytes.append(byte)

            for i in range(len(_bytes)):
                if left_justify:
                    METHOD.append(f"draw_symbol(str({_bytes[i]}), 8 - {i})")
                else:
                    METHOD.append(f"draw_symbol(str({_bytes[i]}), {i} + 1)")

        # TODO: base

    def write_text(self, text: str):
        self.clear()
        if len(text) <= 8:
            _bytes = []
            for i in text:
                byte = str(self.__get_byte_by_char(i))
                _bytes.append(byte)
            for i in range(len(text)):
                METHOD.append(f"draw_symbol(str({_bytes[i]}), 8 - {i})")
        else:
            return

    def clear(self):
        METHOD.append("init_lines()")


screen = Screen()
