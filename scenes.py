import pygame
import time
from player import Player
from enemy import Enemy

class GameScene:
    def __init__(self, level=1):
        self.level = level
        self.player = Player(400, 550)
        self.enemies = self.create_enemies(level)
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(self.player, self.enemies)
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.game_win = False
        self.last_kill_time = None
        self.background = pygame.image.load('fundo.png').convert()  # Carrega a imagem de fundo


    def create_enemies(self, level):
        columns = 4 + (level - 1) * 2
        rows = 5 + (level - 1)
        speed_multiplier = 2 + (level - 1) * 1.0

        enemies = pygame.sprite.Group(
            [Enemy(x * 60, y * 50) for x in range(columns) for y in range(rows)]
        )
        for enemy in enemies:
            enemy.speed *= speed_multiplier
        return enemies

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.player.shoot(self.bullets)

    def update(self):
        if self.game_over:
            return
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.bullets.update()
        self.enemies.update()
        self.enemy_bullets.update()

        for bullet in self.bullets:
            hit = pygame.sprite.spritecollideany(bullet, self.enemies)
            if hit:
                bullet.kill()
                hit.kill()
                self.score += self.calculate_score()
                self.last_kill_time = time.time()

        if len(self.enemies) == 0:
            if self.level <= 2:
                self.level += 1
                self.enemies = self.create_enemies(self.level)
                self.all_sprites.add(self.enemies)
            else:
                self.game_win = True
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.game_over = True

    def calculate_score(self):
        if self.last_kill_time is None:
            return 10
        elapsed_time = time.time() - self.last_kill_time
        
        if elapsed_time < 1:
            return 30
        elif elapsed_time < 2:
            return 20
        else:
            return 10

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.all_sprites.draw(screen)
        self.bullets.draw(screen)
        self.enemy_bullets.draw(screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        level_text = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        screen.blit(level_text, (10, 40))
        if self.game_win:
            if self.level > 2:
                game_text = self.font.render("VICTORY! Game Completed!", True, (0, 255, 0))
                screen.blit(game_text, (250, 300))
        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, (300, 300))
