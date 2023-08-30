python
import pygame

# Inicializa Pygame
pygame.init()

# Define las constantes del juego
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BLOCK_SIZE = 30
ROWS = 20
COLS = 10

# Crea la ventana
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Carga las imágenes de los bloques de Tetris
block_images = []
for i in range(7):
    image = pygame.image.load("block" + str(i) + ".png")
    block_images.append(image)

# Define la clase para representar cada bloque de Tetris
class Block:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rotation = 0

    def draw(self, window):
        image = pygame.transform.rotate(self.image, self.rotation * 90)
        window.blit(image, (self.x, self.y))

    def move_left(self):
        self.x -= BLOCK_SIZE

    def move_right(self):
        self.x += BLOCK_SIZE

    def move_down(self):
        self.y += BLOCK_SIZE

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

# Define la clase para representar la pantalla de Tetris
class TetrisScreen:
    def __init__(self):
        self.blocks = []
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.create_new_block()

    def create_new_block(self):
        self.current_block = Block(COLS // 2 * BLOCK_SIZE, 0, block_images[0])
        self.blocks.append(self.current_block)

    def draw(self, window):
        # Dibuja la pantalla de fondo
        window.fill((0, 0, 0))

        # Dibuja los bloques en la pantalla
        for block in self.blocks:
            block.draw(window)

        # Dibuja la barra de puntuación
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        window.blit(text, (10, 10))

        # Dibuja la barra de nivel
        font = pygame.font.Font(None, 36)
        text = font.render("Level: " + str(self.level), True, (255, 255, 255))
        window.blit(text, (10, 50))

        # Dibuja la barra de líneas eliminadas
        font = pygame.font.Font(None, 36)
        text = font.render("Lines Cleared: " + str(self.lines_cleared), True, (255, 255, 255))
        window.blit(text, (10, 90))

    def move_block_down(self):
        for block in self.blocks:
            block.move_down()

        # Comprueba si el bloque choca con el suelo o