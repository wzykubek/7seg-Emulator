#!/usr/bin/env python3

from tkinter import Tk, Canvas, Frame, BOTH, LEFT, RIGHT, Button
from Emulator.bytes import BYTES
from Emulator.sectors import LINES
import time

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
    lb_pressed = False
    rb_pressed = False


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
        # horizontal
        for i in range(8):
            for j in range(3):
                self.canvas.create_line(
                    10 + (i * 60),
                    25 + (j * 35),
                    40 + (i * 60),
                    25 + (j * 35),
                    fill=ctx.off_color,
                )

            # dots
            self.canvas.create_rectangle(
                45 + (i * 60),
                90,
                50 + (i * 60),
                95,
                fill=ctx.off_color,
                outline=ctx.off_color,
            )

        # vertical
        for i in range(16):
            self.canvas.create_line(
                10 + (i * 30), 25, 10 + (i * 30), 61, fill=ctx.off_color
            )
            self.canvas.create_line(
                10 + (i * 30), 61, 10 + (i * 30), 96, fill=ctx.off_color
            )

    def left_button_state(self):
        ctx.lb_pressed = True
        time.sleep(0.02)
        ctx.lb_pressed = False

    def right_button_state(self):
        ctx.rb_pressed = True
        time.sleep(0.02)
        ctx.rb_pressed = False

    def init_buttons(self):
        """
        Initialize buttons (not working yet).
        """
        self.button_left = Button(
           self, bg="#000", fg="#fff", text="1", command=self.left_button_state
        )
        self.button_left.pack(side=LEFT, fill=BOTH)
        self.button_right = Button(
            self, bg="#000", fg="#fff", text="2", command=self.right_button_state
        )
        self.button_right.pack(side=RIGHT, fill=BOTH)

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

        byte = int(byte, 0)
        if byte >= 0x80:
            for el in new_bytes[hex(byte - len(BYTES))]:
                self.canvas.create_line(el, fill=ctx.on_color)
            self.canvas.create_rectangle(
                LINES[position][-1], fill=ctx.on_color, outline=ctx.on_color
            )
        else:
            # Required loop avoid bias connected lines.
            for el in new_bytes[hex(byte)]:
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
    from Emulator.library import screen, Button

    bleft = Button("left")
    bright = Button("right")

    while True:
        if bleft.pressed():
            screen.write_text("left")
        if bright.pressed():
            screen.write_text("right")


def main():
    from threading import Thread

    Thread(target=set_method, daemon=True).start()
    Thread(target=ZeroSeg_code, daemon=True).start()

    app.geometry("400x250+300+300")
    app.title(ctx.title)
    app.mainloop()
