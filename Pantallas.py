import pygame
from pygame import init, display, event, image, transform, Rect, font
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP

class Juego:

    def __init__(self):
        self.WIDTH = 850
        self.HEIGHT = 550
        self.BLANCO = (255, 255, 255)
        self.VERDE = (0, 225, 0)
        self.NEGRO = (0, 0, 0)
        self.TAMANIO_BOTON = (50, 50, 200, 50) #-> (x, y, ancho, alto)
        self.GRIS = (100, 100, 100)
        self.GROSOR_CONTORNO = 3
        self.FONDO = 'fondo.jpg'
        self.TEXTO_BOTON = 'JUGAR'
        self.ESCENARIO = 'R.gif'

    def ventana_pelea(self):
        
        self.pantalla = display.set_mode((self.WIDTH, self.HEIGHT)) # Tamaño de la pantalla
        display.set_caption("Pelea") # Nombre de la pantalla
        self.imagen = image.load(self.ESCENARIO) # Carga la imagen del escenario
        self.imagen_tamanio = transform.scale(self.imagen, (self.WIDTH, self.HEIGHT))

        self.running = True

        while self.running:

            for evento in event.get(): 
                if evento.type == QUIT: # Verifica si algún evento cierra la ventana
                    self.running = False

            self.pantalla.blit(self.imagen_tamanio, (0, 0))
            pygame.display.flip()

        pygame.quit() # Cierra el programa

    def iniciar_juego(self):

        init() #Inicializa el programa

        self.pantalla = display.set_mode((self.WIDTH, self.HEIGHT)) # Tamanio de la pantalla
        display.set_caption("Inicio") # Nombre de la pantalla

        self.imagen = image.load(self.FONDO) # Carga la foto en la pantalla
        self.imagen_tamanio = transform.scale(self.imagen, (self.WIDTH, self.HEIGHT)) # Redimensionando la foto al tamanio de la pantalla

        self.boton_tamanio = Rect(self.TAMANIO_BOTON)
        self.boton_fuente = font.Font(None, 50) # -> (tipado, tamanio de texto)
        self.boton_texto = self.boton_fuente.render(self.TEXTO_BOTON, True, self.BLANCO) # -> (texto, verdadero, texto blanco)

        self.running = True
        self.pressed = False

        while self.running:

            self.eventos()
            self.accion_boton()

        pygame.quit() #cierra el programa
    

    def eventos(self):

        for evento in event.get(): 
            if evento.type == QUIT: # Verifica si algún evento cierra la ventana
                self.running = False
            elif evento.type == MOUSEBUTTONDOWN: # Verifica acción de dar clik
                if self.boton_tamanio.collidepoint(evento.pos): # Verificar click dentro del botón
                    self.pressed = True
                    self.ventana_pelea()
            elif evento.type == MOUSEBUTTONUP:
                if self.boton_tamanio.collidepoint(evento.pos):
                    self.pressed = False


    def accion_boton(self):
            
        self.pantalla.blit(self.imagen_tamanio, (0, 0))
        pygame.draw.rect(self.pantalla, self.GRIS, self.boton_tamanio.move(5, 5)) # -> (pantalla en donde se carga, color, posicion en referencia al boton original)
        pygame.draw.rect(self.pantalla, self.NEGRO, self.boton_tamanio) # Crea el boton original color Negro, lo crea encima del boton color gris de abajo
        if self.pressed:
            pygame.draw.rect(self.pantalla, self.VERDE, self.boton_tamanio.move(2, 2), self.GROSOR_CONTORNO)
        else:
            pygame.draw.rect(self.pantalla, self.VERDE, self.boton_tamanio, self.GROSOR_CONTORNO)
    
        self.pantalla.blit(self.boton_texto, (self.boton_tamanio.x + 40, self.boton_tamanio.y + 10)) # Crea el texto en el botón y donde se posiciciona en el rectangulo
        # pantalla.fill(BLANCO) -> Poner de un color
        display.flip()
