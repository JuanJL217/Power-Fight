import pygame
from pygame import init, display, event, image, transform, font, Rect, time
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from Frames import Frame_Personajes, FRAMES_SAMURAI, LEFT, RIGHT, RUN, WALK, IDLE, JUMP


SAMURAI = 'Samurai'
WIDTH = 800
HEIGHT = 600
BLANCO = (255, 255, 255)
VERDE = (0, 225, 0)
NEGRO = (0, 0, 0)
TAMANIO_BOTON = (50, 50, 200, 50) #-> (x, y, ancho, alto)
GRIS = (100, 100, 100)
GROSOR_CONTORNO = 3
FONDO = 'fondo.jpg'
ESCENARIO = 'R.gif'

def pantalla_pelea():
    
    pantalla = display.set_mode((WIDTH, HEIGHT)) # Tamaño de la pantalla
    display.set_caption("Pelea") # Nombre de la pantalla
    imagen = image.load(ESCENARIO) # Carga la imagen del escenario
    imagen_tamanio = transform.scale(imagen, (WIDTH, HEIGHT)) # Redimensiona la imagen al tamaño de la pantalla



    Samurai = Frame_Personajes(SAMURAI)
    Samurai.agregar_frame(FRAMES_SAMURAI)
    parado_izquierda, parado_derecha = Samurai.obtener_frames(IDLE)
    caminar_izquierda, caminar_derecha = Samurai.obtener_frames(WALK)
    correr_izquierda, correr_derecha = Samurai.obtener_frames(RUN)
    saltar_inzquierda, saltar_derecha = Samurai.obtener_frames(JUMP)

    x = 200
    y = 420
    width_personaje = 5
    height_personaje = 5
    vel = 5

    personaje_samurai = parado_derecha[0].get_rect()
    personaje_samurai.center = (x, y)

    frame_index = 0
    frame_rate = 15

    movement_speed = 8
    run_speed = 15

    clock = time.Clock()

    running = True

    left = False
    right = False

    ultima_direccion = None

    while running:

        for evento in event.get(): 
            if evento.type == QUIT: # Verifica si algún evento cierra la ventana
                running = False

        keys = pygame.key.get_pressed()

        quieto = True


        if keys[pygame.K_LSHIFT] and keys[pygame.K_a]:
            personaje_samurai.x -= run_speed
            run = True
            right = False
            left = True
            quieto = False
            salto = False

        elif keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
            personaje_samurai.x += run_speed
            run = True
            right = True
            left = False
            quieto = False
            salto = False

        elif keys[pygame.K_SPACE] and keys[pygame.K_a]:
            personaje_samurai.x -= run_speed
            run = False
            right = False
            left = True
            quieto = False
            salto = True 

        elif keys[pygame.K_SPACE] and keys[pygame.K_d]:
            personaje_samurai.x += run_speed
            run = False
            right = True
            left = False
            quieto = False
            salto = True         

        elif keys[pygame.K_a]:
            personaje_samurai.x -= movement_speed
            run = False
            right = False
            left = True
            quieto = False
            salto = False


        elif keys[pygame.K_d]:
            personaje_samurai.x += movement_speed
            run = False
            right = True
            left = False
            quieto = False
            salto = False


        pantalla.blit(imagen_tamanio, (0, 0))


        if quieto:
            if ultima_direccion == RIGHT:
                frame_index += 1
                if frame_index >= len(parado_derecha):
                    frame_index = 0
                pantalla.blit(parado_derecha[frame_index], personaje_samurai)

            elif ultima_direccion == LEFT:
                frame_index += 1
                if frame_index >= len(parado_izquierda):
                    frame_index = 0
                pantalla.blit(parado_izquierda[frame_index], personaje_samurai)

            else:
                frame_index += 1
                if frame_index >= len(parado_derecha):
                    frame_index = 0
                pantalla.blit(parado_derecha[frame_index], personaje_samurai)                
        
        elif right and run:
            ultima_direccion = RIGHT
            frame_index += 1
            if frame_index >= len(correr_derecha):
                frame_index = 0
            pantalla.blit(correr_derecha[frame_index], personaje_samurai)
        
        elif left and run:
            ultima_direccion = LEFT
            frame_index += 1
            if frame_index >= len(correr_izquierda):
                frame_index = 0
            pantalla.blit(correr_izquierda[frame_index], personaje_samurai)    

        elif right and salto:
            ultima_direccion = RIGHT
            frame_index += 1
            if frame_index >= len(saltar_derecha):
                frame_index = 0
            pantalla.blit(saltar_derecha[frame_index], personaje_samurai)
        
        elif left and salto:
            ultima_direccion = LEFT
            frame_index += 1
            if frame_index >= len(saltar_inzquierda):
                frame_index = 0
            pantalla.blit(saltar_inzquierda[frame_index], personaje_samurai)        

        elif right:
            ultima_direccion = RIGHT
            frame_index += 1
            if frame_index >= len(caminar_derecha):
                frame_index = 0
            pantalla.blit(caminar_derecha[frame_index], personaje_samurai)

        elif left:
            ultima_direccion = LEFT
            frame_index += 1
            if frame_index >= len(caminar_izquierda):
                frame_index = 0
            pantalla.blit(caminar_izquierda[frame_index], personaje_samurai)


        # Controlar la velocidad de la animación
        clock.tick(frame_rate)

        pygame.display.flip()

    pygame.quit() # Cierra el programa



def pantalla_inicio():

    init() # Inicializa el programa

    pantalla = display.set_mode((WIDTH, HEIGHT)) # Tamaño de la pantalla
    display.set_caption("Inicio") # Nombre de la pantalla
    imagen = image.load(FONDO) # Carga la foto en la pantalla
    imagen_tamanio = transform.scale(imagen, (WIDTH, HEIGHT)) # Redimensionando la foto al tamaño de la pantalla

    boton_tamanio = Rect(TAMANIO_BOTON)
    boton_fuente = font.Font(None, 50) # -> (tipado, tamaño de texto)
    boton_texto = boton_fuente.render("JUGAR", True, BLANCO) # -> (texto, verdadero, texto blanco)

    running = True
    pressed = False

    while running:

        for evento in event.get(): 
            if evento.type == QUIT: # Verifica si algún evento cierra la ventana
                running = False
            elif evento.type == MOUSEBUTTONDOWN: # Verifica acción de dar click
                if boton_tamanio.collidepoint(evento.pos): # Verificar click dentro del botón
                    pressed = True
                    pantalla_pelea() # Ejecuta pantalla_pelea()
            elif evento.type == MOUSEBUTTONUP:
                if boton_tamanio.collidepoint(evento.pos):
                    pressed = False

        
        pantalla.blit(imagen_tamanio, (0, 0))
        pygame.draw.rect(pantalla, GRIS, boton_tamanio.move(5, 5)) # -> (pantalla en donde se carga, color, posicion en referencia al boton original)
        pygame.draw.rect(pantalla, NEGRO, boton_tamanio) # Crea el botón original color Negro, lo crea encima del botón color gris de abajo
        if pressed:
            pygame.draw.rect(pantalla, VERDE, boton_tamanio.move(2, 2), GROSOR_CONTORNO)
        else:
            pygame.draw.rect(pantalla, VERDE, boton_tamanio, GROSOR_CONTORNO)
    
        pantalla.blit(boton_texto, (boton_tamanio.x + 40, boton_tamanio.y + 10)) # Crea el texto en el botón y donde se posiciona en el rectángulo
        pygame.display.flip()

    pygame.quit() # Cierra el programa
