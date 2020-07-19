#!/usr/bin/env python3

from tkinter import Tk, Canvas, Frame, BOTH
from Emulator.bytes import BYTES


class ctx(object):
    title = "ZeroSeg Simulator"
    off_color = "#bebebe"
    on_color = "#fc0505"


class Display(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title(ctx.title)
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)

        # Draw horizontal lines.
        for i in range(8):
            for j in range(3):
                self.canvas.create_line(
                    10 + (i * 60),
                    25 + (j * 35),
                    40 + (i * 60),
                    25 + (j * 35),
                    fill=ctx.off_color,
                )

        # Draw vertical lines.
        for i in range(16):
            self.canvas.create_line(
                10 + (i * 30), 25, 10 + (i * 30), 61, fill=ctx.off_color
            )
            self.canvas.create_line(
                10 + (i * 30), 61, 10 + (i * 30), 96, fill=ctx.off_color
            )

        self.canvas.pack(fill=BOTH, expand=1)

    def draw_symbol(self, byte: int, position: int):
        # Coordinates of lines on each sector.
        # Each external `list` is a one display sector and each internal list is
        # one line in this sector sorted in schematic way by index in list.
        self.lines = [
            [None],
            [
                [430, 25, 460, 25],
                [460, 25, 460, 60],
                [460, 60, 460, 95],
                [430, 95, 460, 95],
                [430, 95, 430, 60],
                [430, 60, 430, 25],
                [430, 60, 460, 60],
                [],  # dot
            ],
            [
                [370, 25, 400, 25],
                [400, 25, 400, 60],
                [400, 60, 400, 95],
                [370, 95, 400, 95],
                [370, 95, 370, 60],
                [370, 60, 370, 25],
                [370, 60, 400, 60],
                [],  # dot
            ],
            [
                [310, 25, 340, 25],
                [340, 25, 340, 60],
                [340, 60, 340, 95],
                [310, 95, 340, 95],
                [310, 95, 310, 60],
                [310, 60, 310, 25],
                [310, 60, 340, 60],
                [],  # dot
            ],
            [
                [250, 25, 280, 25],
                [280, 25, 280, 60],
                [280, 60, 280, 95],
                [250, 95, 280, 95],
                [250, 95, 250, 60],
                [250, 60, 250, 25],
                [250, 60, 280, 60],
                [],  # dot
            ],
            [
                [190, 25, 220, 25],
                [220, 25, 220, 60],
                [220, 60, 220, 95],
                [190, 95, 220, 95],
                [190, 95, 190, 60],
                [190, 60, 190, 25],
                [190, 60, 220, 60],
                [],  # dot
            ],
            [
                [130, 25, 160, 25],
                [160, 25, 160, 60],
                [160, 60, 160, 95],
                [130, 95, 160, 95],
                [130, 95, 130, 60],
                [130, 60, 130, 25],
                [130, 60, 160, 60],
                [],  # dot
            ],
            [
                [70, 25, 100, 25],
                [100, 25, 100, 60],
                [100, 60, 100, 95],
                [70, 95, 100, 95],
                [70, 95, 70, 60],
                [70, 60, 70, 25],
                [70, 60, 100, 60],
                [],  # dot
            ],
            [
                # X,  Y,  x,  y
                [10, 25, 40, 25],  # 0 line
                [40, 25, 40, 60],  # 1 line
                [40, 60, 40, 95],  # 2 ...
                [10, 95, 40, 95],  # ...
                [10, 95, 10, 60],
                [10, 60, 10, 25],
                [10, 60, 40, 60],
                [],  # TODO: Add dots.
            ],
        ]

        # Create new dict with lines from `lines` instead schematic numbers.
        new_bytes = {}
        for k, v in BYTES.items():
            new_bytes[hex(k)] = []
            for i in v:
                new_bytes[hex(k)].append(self.lines[position][i])

        # Required loop avoid bias connected lines.
        for el in new_bytes[f"{byte}"]:
            self.canvas.create_line(el, fill=ctx.on_color)

        self.canvas.pack(fill=BOTH, expand=1)


app = Tk()
display = Display()


def main():
    from Emulator.library import screen

    # Library methods.
    screen.write_number(1)
    screen.write_text("asdf")
    screen.write_char("A", 3)

    app.geometry("400x250+300+300")
    app.mainloop()
