#!/usr/bin/env python3
"""
Coordinates of lines on each sector.
Each external `list` is a one display sector and each internal list is
one line in this sector sorted in schematic way by index in list.
"""
LINES = [
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