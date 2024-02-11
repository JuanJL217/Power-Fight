import pygame
from pygame import init, display, event, image, transform, font, Rect
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP

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

    running = True

    while running:

        for evento in event.get(): 
            if evento.type == QUIT: # Verifica si algún evento cierra la ventana
                running = False

        pantalla.blit(imagen_tamanio, (0, 0))
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
