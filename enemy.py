import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('enemy.png').convert_alpha()  # Carrega a imagem do inimigo
        self.rect = self.image.get_rect(topleft=(x, y))  # Obtém o retângulo para movimentação e colisões
        self.speed = 2

    def update(self):
        self.rect.x += self.speed  # Move o inimigo para a direita ou esquerda
        if self.rect.right >= 800 or self.rect.left <= 0:  # Se atingir as bordas, inverte a direção
            self.speed = -self.speed
            self.rect.y += 50  # Move o inimigo para baixo após inverter


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.kill()