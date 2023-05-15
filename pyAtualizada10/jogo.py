import pygame

# Inicialize o Pygame
pygame.init()

# Definir largura e altura da tela
screen = pygame.display.set_mode((800, 600))

# Definir título da janela
pygame.display.set_caption("Jogo de Fases")

# Define as fases
fases = [
    [
        "XXXX",
        "X  X",
        "X  X",
        "X  X",
        "XXXX"
    ],
    [
        "XXXX",
        "X  X",
        "X  X",
        "X  X",
        "XXXX"
    ],
    [
        "XXXX",
        "X  X",
        "X  X",
        "X  X",
        "XXXX"
    ]
]

# Criar a fonte para exibir o texto
font = pygame.font.Font(None, 30)

# Iniciar o laço do jogo
running = True
current_fase = 0
while running:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Verificar se a tecla pressionada foi ESPAÇO
            if event.key == pygame.K_SPACE:
                current_fase += 1
                if current_fase >= len(fases):
                    running = False

    # Preencher a tela com uma cor sólida
    screen.fill((255, 255, 255))

    # Mostrar a fase atual
    for y, linha in enumerate(fases[current_fase]):
        for x, caractere in enumerate(linha):
            # Desenhar a fase usando retângulos
            if caractere == "X":
                pygame.draw.rect(screen, (0, 0, 0), (x*100, y*100, 100, 100), 0)

    # Mostrar o número da fase
    text = font.render("Fase {}".format(current_fase + 1), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Atualizar a tela
    pygame.display.update()

# Finalizar o Pygame
pygame.quit()
