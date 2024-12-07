from colorsys import hsv_to_rgb, rgb_to_hsv
from typing import Tuple
from jelka import Jelka,Color


def callback(jelka: Jelka):
    for i in range(jelka.n):
        hue = rgb_to_hsv(jelka.lights[i].r, jelka.lights[i].g, jelka.lights[i].b)[0] * 360
        hue = (hue + 4) % 360

        color = hsv_to_rgb(hue / 360.0, 1.0, 1.0)
        color = tuple(map(lambda x: int(x * 255), color))
        jelka.set_light(i, Color(color[0], color[1], color[2]))

def main():
    jelka = Jelka(300, 60)
    jelka.run(callback)

main()