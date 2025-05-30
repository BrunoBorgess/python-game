import random
import pgzrun
from pgzero.actor import Actor
from pgzero.rect import Rect

# Definir as variáveis globais
WIDTH = 800
HEIGHT = 600
hero_speed = 5

# Criar o herói
hero = Actor('hero_idle')  # Usando uma imagem de idle (parado)
hero.x = 400
hero.y = 300

# Criar inimigos
enemies = []
enemy_count = 5

# Criar o fundo e a música
background = Actor('background')
background.x = WIDTH // 2
background.y = HEIGHT // 2
music_on = True

# Função para criar inimigos
def create_enemies():
    global enemies
    for _ in range(enemy_count):
        enemy = Actor('enemy_idle')
        enemy.x = random.randint(50, WIDTH-50)
        enemy.y = random.randint(50, HEIGHT-50)
        enemies.append(enemy)

# Função de movimento do herói
def move_hero():
    if keyboard.left:
        hero.x -= hero_speed
    if keyboard.right:
        hero.x += hero_speed
    if keyboard.up:
        hero.y -= hero_speed
    if keyboard.down:
        hero.y += hero_speed

# Função para movimentar inimigos aleatoriamente
def move_enemies():
    for enemy in enemies:
        direction = random.choice(['left', 'right', 'up', 'down'])
        if direction == 'left':
            enemy.x -= 2
        elif direction == 'right':
            enemy.x += 2
        elif direction == 'up':
            enemy.y -= 2
        elif direction == 'down':
            enemy.y += 2

# Função de animação de sprite para o herói
def animate_hero():
    if keyboard.left:
        hero.image = 'hero_walk_left'
    elif keyboard.right:
        hero.image = 'hero_walk_right'
    elif keyboard.up:
        hero.image = 'hero_walk_up'
    elif keyboard.down:
        hero.image = 'hero_walk_down'
    else:
        hero.image = 'hero_idle'  # Quando ele está parado

# Função para verificar colisões com inimigos
def check_collisions():
    for enemy in enemies:
        if hero.colliderect(enemy):
            print("Game Over!")
            exit()

# Função para alternar o estado da música
def toggle_music():
    global music_on
    if music_on:
        music.stop()
    else:
        music.play('background_music')
    music_on = not music_on

# Função do menu principal
def draw_menu():
    screen.fill((0, 0, 0))
    screen.draw.text("Main Menu", center=(WIDTH//2, 100), fontsize=50, color=(255, 255, 255))
    screen.draw.text("Press 'S' to Start Game", center=(WIDTH//2, 200), fontsize=30, color=(255, 255, 255))
    screen.draw.text("Press 'M' to Toggle Music", center=(WIDTH//2, 250), fontsize=30, color=(255, 255, 255))
    screen.draw.text("Press 'Q' to Quit", center=(WIDTH//2, 300), fontsize=30, color=(255, 255, 255))

# Função para desenhar o jogo
def draw_game():
    background.draw()
    hero.draw()
    for enemy in enemies:
        enemy.draw()

# Função de atualização (movimento e lógica)
def update():
    move_hero()
    animate_hero()
    move_enemies()
    check_collisions()

# Função que detecta a interação com o teclado
def on_key_down(key):
    if key == keys.S:  # Começar o jogo
        create_enemies()
        toggle_music()
    elif key == keys.M:  # Alternar música
        toggle_music()
    elif key == keys.Q:  # Sair
        exit()

# Iniciar o jogo
def main():
    draw_menu()

pgzrun.go()
