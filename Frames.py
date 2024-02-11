import os
from PIL import Image
from pygame import sprite, image

SAMURAI = 'Samurai'
FIGHTER = 'Fighter'

PNG_1 = '1.png'
PNG_2 = '2.png'
PNG_3 = '3.png'
PNG_4 = '4.png'
PNG_5 = '5.png'
PNG_6 = '6.png'
PNG_7 = '7.png'
PNG_8 = '8.png'
PNG_9 = '9.png'
PNG_10 = '10.png'
PNG_11 = '11.png'
PNG_12 = '12.png'

IDLE = 'Idle'
WALK = 'Walk'
RUN = 'Run'
JUMP = 'Jump'
SHIELD = 'Shield'
HURT = 'Hurt'
ATAACK_1 = 'Ataack 1'
ATAACK_2 = 'Ataack 2'
ATAACK_3 = 'Ataack 3'
DEAD = 'Dead'

class Frame_Personajes:

    def __init__(self, nombre):
        self.nombre = nombre
        self.frames = {
            IDLE: [],
            WALK: [],
            RUN: [],
            JUMP: [],
            SHIELD: [],
            HURT: [],
            ATAACK_1: [],
            ATAACK_2: [],
            ATAACK_3: [],
            DEAD: []
        }
    
    def agregar_frame(self, accion, lista_frames):
        self.frames[accion] = lista_frames

    def obtener_frames(self, accion):
        return self.frames.get(accion, [])
    
    
def ruta(nombre, accion, nombre_png):
    
    return f"Personajes/{nombre}/{accion}/{nombre_png}"


FRAMES_WALK_SAMURAI = [
    ruta(SAMURAI, WALK, PNG_1),
    ruta(SAMURAI, WALK, PNG_2),
    ruta(SAMURAI, WALK, PNG_3),
    ruta(SAMURAI, WALK, PNG_4),
    ruta(SAMURAI, WALK, PNG_5),
    ruta(SAMURAI, WALK, PNG_6),
    ruta(SAMURAI, WALK, PNG_7),
    ruta(SAMURAI, WALK, PNG_8)
]

FRAMES_SHIELD_SAMURAI = [
    ruta(SAMURAI, SHIELD, PNG_1),
    ruta(SAMURAI, SHIELD, PNG_2)
]

FRAMES_HURT_SAMURAI = [
    ruta(SAMURAI, HURT, PNG_1),
    ruta(SAMURAI, HURT, PNG_2)
]

FRAMES_DEAD_SAMURAI = [
    ruta(SAMURAI, DEAD, PNG_1),
    ruta(SAMURAI, DEAD, PNG_2),
    ruta(SAMURAI, DEAD, PNG_3)
]

frames_samurai = Frame_Personajes(SAMURAI)
frames_samurai.agregar_frame(WALK, FRAMES_WALK_SAMURAI)
frames_samurai.agregar_frame(SHIELD, FRAMES_SHIELD_SAMURAI)
frames_samurai.agregar_frame(HURT, FRAMES_HURT_SAMURAI)
frames_samurai.agregar_frame(DEAD, FRAMES_DEAD_SAMURAI)

for i in range(1,4):
    imagen = Image.open(ruta(SAMURAI, DEAD, f"{i}.png"))
    imagen_volteada = imagen.transpose(Image.FLIP_LEFT_RIGHT)
    imagen_volteada.save(f"{i}.png")