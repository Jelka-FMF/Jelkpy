from jelkpy.jelka import Jelka
from jelkpy.color import Color

def callback(jelka: Jelka):
    jelka.set_light(0, color=Color(0, 255, 0))
    jelka.set_light(1, color=Color(0, 255, 0))
    jelka.set_light(2, color=Color(0, 255, 0))
    jelka.set_light(3, color=Color(0, 255, 0))

def main():
    jelka = Jelka(500, 60, Color(255, 0, 0))
    jelka.run(callback)

main()