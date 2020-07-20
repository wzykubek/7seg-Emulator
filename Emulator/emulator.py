#!/usr/bin/env python3

from tkinter import Tk, Canvas, Frame, BOTH, Button
from Emulator.bytes import BYTES
from Emulator.sectors import LINES

app = Tk()


class ctx(object):
    """
    Emulator context.
    """

    title = "ZeroSeg Simulator"
    off_color = "#bebebe"
    on_color = "#fc0505"
    update_delay = 10  # ms
    method = []


class Display(Frame):
    """
    Main emulator class.
    """

    def __init__(self, master):
        Frame.__init__(self, master)

        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.init_lines()
        self.canvas.pack(fill=BOTH, expand=1)
        self.init_buttons()

        self.update_handler()

    def init_lines(self):
        """
        Draw gray (not activated) lines.
        """
        # Horizontal.
        for i in range(8):
            for j in range(3):
                self.canvas.create_line(
                    10 + (i * 60),
                    25 + (j * 35),
                    40 + (i * 60),
                    25 + (j * 35),
                    fill=ctx.off_color,
                )

        # Vertical.
        for i in range(16):
            self.canvas.create_line(
                10 + (i * 30), 25, 10 + (i * 30), 61, fill=ctx.off_color
            )
            self.canvas.create_line(
                10 + (i * 30), 61, 10 + (i * 30), 96, fill=ctx.off_color
            )

    def init_buttons(self):
        """
        Initialize buttons (not working yet).
        """
        self.button_left = Button(self)
        self.button_left.pack(fill=BOTH)
        self.button_right = Button(self)
        self.button_right.pack(fill=BOTH)

    def update_handler(self):
        """
        Call first method from queue (`ctx.method`) for update screen purpose.
        """
        try:
            eval(f"self.{ctx.method[0]}")
            del ctx.method[0]
        except IndexError:
            pass
        self.after(ctx.update_delay, self.update_handler)

    def draw_symbol(self, byte: int, position: int):
        """
        Draw symbol (activated lines) by byte representation on specified position.
        """
        # Create new dict with lines from `lines` instead schematic numbers.
        new_bytes = {}
        for k, v in BYTES.items():
            new_bytes[hex(k)] = []
            for i in v:
                new_bytes[hex(k)].append(LINES[position][i])

        # Required loop avoid bias connected lines.
        for el in new_bytes[hex(int(byte))]:
            self.canvas.create_line(el, fill=ctx.on_color)

        self.canvas.pack(fill=BOTH, expand=1)


display = Display(app)


def set_method():
    """
    Function to handle methods from ZeroSeg library and save it to
    list in `ctx` object.
    """
    while True:
        from Emulator.library import METHOD

        ctx.method = METHOD


def ZeroSeg_code():
    """
    Testing function with ZeroSeg library example code.
    """
    from Emulator.library import screen
    from datetime import datetime
    import time

    while True:
        now = datetime.now()
        screen.write_text(f"{now.hour}-{now.minute}-{now.second}")
        time.sleep(1)


def main():
    from threading import Thread

    Thread(target=set_method, daemon=True).start()
    Thread(target=ZeroSeg_code, daemon=True).start()

    app.geometry("400x250+300+300")
    app.title(ctx.title)
    app.mainloop()
