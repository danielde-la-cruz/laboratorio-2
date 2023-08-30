# juego

import pygame
import random

# Inicializar pygame
pygame.init()

# Definir los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Configurar la pantalla
dimensiones = (800, 600)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Juego")

# Coordenadas del jugador
jugador_x = 400
jugador_y = 500

# Velocidad del jugador
velocidad = 5

# Crear una lista vacía para los enemigos
enemigos = []

# Crear enemigos aleatorios
for i in range(10):
    enemigo_x = random.randint(0, 800)
    enemigo_y = random.randint(0, 300)
    enemigos.append((enemigo_x, enemigo_y))

# Variable para controlar el bucle principal del juego
jugando = True

# Bucle principal del juego
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover al jugador
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_x += velocidad

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar al jugador
    pygame.draw.rect(pantalla, BLANCO, (jugador_x, jugador_y, 50, 50))

    # Dibujar a los enemigos
    for enemigo in enemigos:
        pygame.draw.rect(pantalla, BLANCO, (enemigo[0], enemigo[1], 50, 50))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()
