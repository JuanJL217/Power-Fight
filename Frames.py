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

UNION = ' '

LEFT = 'Left'
RIGHT = 'Right'

ACTION = "Action"
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

            # Movimientos a la izquierda
            IDLE+UNION+LEFT: [],
            WALK+UNION+LEFT: [],
            RUN+UNION+LEFT: [],
            JUMP+UNION+LEFT: [],
            SHIELD+UNION+LEFT: [],
            HURT+UNION+LEFT: [],
            ATAACK_1+UNION+LEFT: [],
            ATAACK_2+UNION+LEFT: [],
            ATAACK_3+UNION+LEFT: [],
            DEAD+UNION+LEFT: [],

            # Movimientos a la derecha
            IDLE+UNION+RIGHT: [],
            WALK+UNION+RIGHT: [],
            RUN+UNION+RIGHT: [],
            JUMP+UNION+RIGHT: [],
            SHIELD+UNION+RIGHT: [],
            HURT+UNION+RIGHT: [],
            ATAACK_1+UNION+RIGHT: [],
            ATAACK_2+UNION+RIGHT: [],
            ATAACK_3+UNION+RIGHT: [],
            DEAD+UNION+RIGHT: [],
        }
    
    def agregar_frame(self, accion, movimiento):
        self.frames[accion+UNION+LEFT] = movimiento[LEFT]
        self.frames[accion+UNION+RIGHT] = movimiento[RIGHT]

    def obtener_frames(self, accion):
        return self.frames.get(accion, [])
    
    
def ruta(nombre, accion, direccion, imagen_png):
    
    return os.path.join("Personajes", nombre, accion, direccion, imagen_png)


FRAMES_WALK_SAMURAI = {

    ACTION: WALK,

    LEFT: [
        ruta(SAMURAI, WALK, RIGHT, PNG_1),
        ruta(SAMURAI, WALK, RIGHT, PNG_2),
        ruta(SAMURAI, WALK, RIGHT, PNG_3),
        ruta(SAMURAI, WALK, RIGHT, PNG_4),
        ruta(SAMURAI, WALK, RIGHT, PNG_5),
        ruta(SAMURAI, WALK, RIGHT, PNG_6),
        ruta(SAMURAI, WALK, RIGHT, PNG_7),
        ruta(SAMURAI, WALK, RIGHT, PNG_8)        
    ],

    RIGHT: [
        ruta(SAMURAI, WALK, RIGHT, PNG_1),
        ruta(SAMURAI, WALK, RIGHT, PNG_2),
        ruta(SAMURAI, WALK, RIGHT, PNG_3),
        ruta(SAMURAI, WALK, RIGHT, PNG_4),
        ruta(SAMURAI, WALK, RIGHT, PNG_5),
        ruta(SAMURAI, WALK, RIGHT, PNG_6),
        ruta(SAMURAI, WALK, RIGHT, PNG_7),
        ruta(SAMURAI, WALK, RIGHT, PNG_8)
    ]
}


FRAMES_SHIELD_SAMURAI = {

    ACTION: SHIELD,

    LEFT: [
        ruta(SAMURAI, SHIELD, LEFT, PNG_1),
        ruta(SAMURAI, SHIELD, LEFT, PNG_2)
    ],

    RIGHT: [
        ruta(SAMURAI, SHIELD, RIGHT, PNG_1),
        ruta(SAMURAI, SHIELD, RIGHT, PNG_2)
    ]
}


FRAMES_HURT_SAMURAI = {

    ACTION: HURT,

    LEFT: [
        ruta(SAMURAI, HURT, LEFT, PNG_1),
        ruta(SAMURAI, HURT, LEFT, PNG_2)
    ],

    RIGHT: [
        ruta(SAMURAI, HURT, RIGHT, PNG_1),
        ruta(SAMURAI, HURT, RIGHT, PNG_2)
    ]
}


FRAMES_DEAD_SAMURAI = {

    ACTION: DEAD,

    LEFT: [
        ruta(SAMURAI, DEAD, LEFT, PNG_1),
        ruta(SAMURAI, DEAD, LEFT, PNG_2),
        ruta(SAMURAI, DEAD, LEFT, PNG_3)
    ],

    RIGHT: [
        ruta(SAMURAI, DEAD, RIGHT, PNG_1),
        ruta(SAMURAI, DEAD, RIGHT, PNG_2),
        ruta(SAMURAI, DEAD, RIGHT, PNG_3)
    ]
}


frames_samurai = Frame_Personajes(SAMURAI)
# Hace ciclo for  
frames_samurai.agregar_frame(FRAMES_WALK_SAMURAI)
frames_samurai.agregar_frame(FRAMES_SHIELD_SAMURAI)
frames_samurai.agregar_frame(FRAMES_HURT_SAMURAI)
frames_samurai.agregar_frame(FRAMES_DEAD_SAMURAI)




for i in range(1,4):
    imagen = Image.open(ruta(SAMURAI, DEAD, f"{i}.png"))
    imagen_volteada = imagen.transpose(Image.FLIP_LEFT_RIGHT)
    imagen_volteada.save(f"{i}.png")