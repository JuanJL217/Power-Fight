import os
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
ATTACK_1 = 'Attack_1'
ATTACK_2 = 'Attack_2'
ATTACK_3 = 'Attack_3'
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
            ATTACK_1+UNION+LEFT: [],
            ATTACK_2+UNION+LEFT: [],
            ATTACK_3+UNION+LEFT: [],
            DEAD+UNION+LEFT: [],

            # Movimientos a la derecha
            IDLE+UNION+RIGHT: [],
            WALK+UNION+RIGHT: [],
            RUN+UNION+RIGHT: [],
            JUMP+UNION+RIGHT: [],
            SHIELD+UNION+RIGHT: [],
            HURT+UNION+RIGHT: [],
            ATTACK_1+UNION+RIGHT: [],
            ATTACK_2+UNION+RIGHT: [],
            ATTACK_3+UNION+RIGHT: [],
            DEAD+UNION+RIGHT: [],
        }
    
    def agregar_frame(self, movimiento):
        
        for direccion in movimiento:
            if direccion != ACTION:
                lista_direcciones = movimiento[direccion]
                for rutas in lista_direcciones:
                    self.frames[movimiento[ACTION]+UNION+direccion].append(image.load(rutas))


    def obtener_frames(self, accion, direccion):
        return self.frames.get(accion+UNION+direccion, [])
    
    
def ruta(nombre, accion, direccion, imagen_png):
    
    return os.path.join("Personajes", nombre, accion, direccion, imagen_png)


FRAMES_ATTACK_1_SAMURAI = {

    ACTION: ATTACK_1,

    LEFT: [
        ruta(SAMURAI, ATTACK_1, LEFT, PNG_1),
        ruta(SAMURAI, ATTACK_1, LEFT, PNG_2),
        ruta(SAMURAI, ATTACK_1, LEFT, PNG_3),
        ruta(SAMURAI, ATTACK_1, LEFT, PNG_4),
        ruta(SAMURAI, ATTACK_1, LEFT, PNG_5),
        ruta(SAMURAI, ATTACK_1, LEFT, PNG_6),
    ],

    RIGHT: [
        ruta(SAMURAI, ATTACK_1, RIGHT, PNG_1),
        ruta(SAMURAI, ATTACK_1, RIGHT, PNG_2),
        ruta(SAMURAI, ATTACK_1, RIGHT, PNG_3),
        ruta(SAMURAI, ATTACK_1, RIGHT, PNG_4),
        ruta(SAMURAI, ATTACK_1, RIGHT, PNG_5),
        ruta(SAMURAI, ATTACK_1, RIGHT, PNG_6),
    ]
}


FRAMES_ATTACK_2_SAMURAI = {

    ACTION: ATTACK_2,

    LEFT: [
        ruta(SAMURAI, ATTACK_2, LEFT, PNG_1),
        ruta(SAMURAI, ATTACK_2, LEFT, PNG_2),
        ruta(SAMURAI, ATTACK_2, LEFT, PNG_3),
        ruta(SAMURAI, ATTACK_2, LEFT, PNG_4),  
    ],

    RIGHT: [
        ruta(SAMURAI, ATTACK_2, RIGHT, PNG_1),
        ruta(SAMURAI, ATTACK_2, RIGHT, PNG_2),
        ruta(SAMURAI, ATTACK_2, RIGHT, PNG_3),
        ruta(SAMURAI, ATTACK_2, RIGHT, PNG_4),        
    ]
}


FRAMES_ATTACK_3_SAMURAI = {

    ACTION: ATTACK_3,

    LEFT: [
        ruta(SAMURAI, ATTACK_3, LEFT, PNG_1),
        ruta(SAMURAI, ATTACK_3, LEFT, PNG_2),
        ruta(SAMURAI, ATTACK_3, LEFT, PNG_3),       
    ],

    RIGHT: [
        ruta(SAMURAI, ATTACK_3, RIGHT, PNG_1),
        ruta(SAMURAI, ATTACK_3, RIGHT, PNG_2),
        ruta(SAMURAI, ATTACK_3, RIGHT, PNG_3),       
    ]
}


FRAMES_WALK_SAMURAI = {

    ACTION: WALK,

    LEFT: [
        ruta(SAMURAI, WALK, LEFT, PNG_1),
        ruta(SAMURAI, WALK, LEFT, PNG_2),
        ruta(SAMURAI, WALK, LEFT, PNG_3),
        ruta(SAMURAI, WALK, LEFT, PNG_4),
        ruta(SAMURAI, WALK, LEFT, PNG_5),
        ruta(SAMURAI, WALK, LEFT, PNG_6),
        ruta(SAMURAI, WALK, LEFT, PNG_7),
        ruta(SAMURAI, WALK, LEFT, PNG_8)        
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


FRAMES_RUN_SAMURAI = {

    ACTION: RUN,

    LEFT: [
        ruta(SAMURAI, RUN, LEFT, PNG_1),
        ruta(SAMURAI, RUN, LEFT, PNG_2),
        ruta(SAMURAI, RUN, LEFT, PNG_3)
    ],

    RIGHT: [
        ruta(SAMURAI, RUN, RIGHT, PNG_1),
        ruta(SAMURAI, RUN, RIGHT, PNG_2),
        ruta(SAMURAI, RUN, RIGHT, PNG_3)
    ]
}


FRAMES_IDLE_SAMURAI = {

    ACTION: IDLE,

    LEFT: [
        ruta(SAMURAI, IDLE, LEFT, PNG_1),
        ruta(SAMURAI, IDLE, LEFT, PNG_2),
        ruta(SAMURAI, IDLE, LEFT, PNG_3),
        ruta(SAMURAI, IDLE, LEFT, PNG_4),
        ruta(SAMURAI, IDLE, LEFT, PNG_5),
        ruta(SAMURAI, IDLE, LEFT, PNG_6),    
    ],

    RIGHT: [
        ruta(SAMURAI, IDLE, RIGHT, PNG_1),
        ruta(SAMURAI, IDLE, RIGHT, PNG_2),
        ruta(SAMURAI, IDLE, RIGHT, PNG_3),
        ruta(SAMURAI, IDLE, RIGHT, PNG_4),
        ruta(SAMURAI, IDLE, RIGHT, PNG_5),
        ruta(SAMURAI, IDLE, RIGHT, PNG_6),        
    ]
}


FRAMES_JUMP_SAMURAI = {

    ACTION: JUMP,

    LEFT: [
        ruta(SAMURAI, JUMP, LEFT, PNG_1),
        ruta(SAMURAI, JUMP, LEFT, PNG_2),
        ruta(SAMURAI, JUMP, LEFT, PNG_3),
        ruta(SAMURAI, JUMP, LEFT, PNG_4),
        ruta(SAMURAI, JUMP, LEFT, PNG_5),
        ruta(SAMURAI, JUMP, LEFT, PNG_6),
        ruta(SAMURAI, JUMP, LEFT, PNG_7),
        ruta(SAMURAI, JUMP, LEFT, PNG_8),
        ruta(SAMURAI, JUMP, LEFT, PNG_9),
        ruta(SAMURAI, JUMP, LEFT, PNG_10),
        ruta(SAMURAI, JUMP, LEFT, PNG_11),
        ruta(SAMURAI, JUMP, LEFT, PNG_12)
    ],

    RIGHT: [
        ruta(SAMURAI, JUMP, RIGHT, PNG_1),
        ruta(SAMURAI, JUMP, RIGHT, PNG_2),
        ruta(SAMURAI, JUMP, RIGHT, PNG_3),
        ruta(SAMURAI, JUMP, RIGHT, PNG_4),
        ruta(SAMURAI, JUMP, RIGHT, PNG_5),
        ruta(SAMURAI, JUMP, RIGHT, PNG_6),
        ruta(SAMURAI, JUMP, RIGHT, PNG_7),
        ruta(SAMURAI, JUMP, RIGHT, PNG_8),
        ruta(SAMURAI, JUMP, RIGHT, PNG_9),
        ruta(SAMURAI, JUMP, RIGHT, PNG_10),
        ruta(SAMURAI, JUMP, RIGHT, PNG_11),
        ruta(SAMURAI, JUMP, RIGHT, PNG_12)
    ]
}


'''frames_samurai = Frame_Personajes(SAMURAI)

frames_samurai.agregar_frame(FRAMES_WALK_SAMURAI)
frames_samurai.agregar_frame(FRAMES_SHIELD_SAMURAI)
frames_samurai.agregar_frame(FRAMES_HURT_SAMURAI)
frames_samurai.agregar_frame(FRAMES_DEAD_SAMURAI)
frames_samurai.agregar_frame(FRAMES_ATTACK_1_SAMURAI)
frames_samurai.agregar_frame(FRAMES_ATTACK_2_SAMURAI)
frames_samurai.agregar_frame(FRAMES_ATTACK_3_SAMURAI)
frames_samurai.agregar_frame(FRAMES_JUMP_SAMURAI)
frames_samurai.agregar_frame(FRAMES_IDLE_SAMURAI)
frames_samurai.agregar_frame(FRAMES_RUN_SAMURAI)'''