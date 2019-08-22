#import unicornhat as uh
import unicornmock as uhc
import time
import colorsys

spacing = 360.0 / 16.0
hue = 0

uh = uhc.unicornmock()

uh.set_layout(0)
uh.brightness(0.5)

print("Starting Unicorn")

#while True:
hue = int(time.time() * 100) % 360
for x in range(8):
    offset = x * spacing
    h = ((hue + offset) % 360) / 360.0
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
    for y in range(4):
        uh.set_pixel(x, y, r, g, b)
uh.show()
time.sleep(0.05)