#!/usr/bin/env python

import time
import unicornhat as unicorn

print("""heart_vereinfacht2.py
Der Pi leuchtet jetzt.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

color_blue  = [0,0,255]
color_green = [0,255,0]
color_red   = [255,0,0]
color = [0,0,0]
default = color

heart = [[0, 1, 0, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0]]
for rownum, row in enumerate(heart):
    for colnum, col in enumerate(row):
        if col is 1:
            color = color_blue
        else:
            color = default
        #print "-",rownum, "--", row, "---", colnum,"--", col
		unicorn.set_pixel(colnum, rownum, color[0], color[1], color[2])

unicorn.show()
time.sleep(5)