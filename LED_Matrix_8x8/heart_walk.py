#!/usr/bin/env python

import time
import unicornhat as unicorn

print("""heart_vereinfacht2.py
Der Pi leuchtet jetzt.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()
#width  = 8 = colnum = x
#height = 4 = rownum = y
color_violet = [148, 0, 211]
color_indigo = [75,0,130]
color_blue  = [0,0,255]
color_green = [0,255,0]
color_yellow= [255,255,0]
color_orange = [255,127,0]
color_red   = [255,0,0]
default = [0,0,0]
color = default
color_rainbow = [color_violet, color_indigo, color_blue, color_green,  color_yellow, color_orange, color_red]
heart = 	[ [0, 1, 0, 1, 0],
              [1, 1, 1, 1, 1],
              [0, 1, 1, 1, 0],
              [0, 0, 1, 0, 0],
			  [0, 0, 0, 0, 1, 0, 1, 0],
              [0, 0, 0, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 0]]
position_x = 0
reset = 0
color_pick = 0
anzahl_ubergang = 0
n = 0
while True:
#for n in range(0,30): #color_change: oder while bis man abbricht, timer
#	print "----------------------------------------------------------------------", n
	for heart_y, row in enumerate(heart):
		for heart_x, col in enumerate(row):
			if col is 1:
				color = color_rainbow[n%7]
			else:
				color = default

			if heart_x + position_x < width:
				unicorn.set_pixel(heart_x + position_x, heart_y, color[0], color[1], color[2])
			else:
				#unicorn.set_pixel(heart_x + position_x - width, heart_y, color[0], color[1], color[2]) original
				#unicorn.set_pixel(heart_x + position_x - width * anzahl_ubergang, heart_y, color[0], color[1], color[2])
				unicorn.set_pixel((heart_x + position_x) %8, heart_y, color[0], color[1], color[2])
	unicorn.show()
	time.sleep(0.3)
	unicorn.clear()
	position_x += 1
	if n == 7: # um uberlauf zu verhindern weil while
		n = -1
	n += 1
	