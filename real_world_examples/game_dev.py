# game_dev.py

import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
FPS = 60

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OOP Game Development with Pygame")

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH-40), random.randint(40, HEIGHT-40)))
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randint(40, WIDTH-40)

# Game Manager Class
class GameManager:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(WIDTH//2, HEIGHT-100)
        self.enemies = pygame.sprite.Group(Enemy() for _ in range(5))
        self.all_sprites = pygame.sprite.Group(self.player, *self.enemies)

    def run(self):
        """Main game loop"""
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        """Handles user input and events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Updates game objects"""
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.enemies.update()

        # Check collision
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            print("💥 Game Over! Player hit an enemy.")
            self.running = False

    def draw(self):
        """Renders game objects"""
        screen.fill(WHITE)
        self.all_sprites.draw(screen)
        pygame.display.flip()

# Run the game
if __name__ == "__main__":
    game = GameManager()
    game.run()
    pygame.quit()
