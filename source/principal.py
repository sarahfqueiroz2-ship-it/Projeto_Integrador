import pygame
import sys


 # inicializa o pygame
pygame.init()

#largura e altura da janela
largura = 1280
altura = 720

#configura a janela e o texto do jogo
screen = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo Opala Space')

#loop principal do jogo
while True:

    #captura eventos
    for event in pygame.event.get():

        #evento de fechar a janela
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    #cor de fundo da janela (preto)
    screen.fill ((0,0,0))

#atualiza a tela
pygame.display.update()
