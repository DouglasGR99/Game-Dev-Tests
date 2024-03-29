import pygame
from pygame.locals import *
from sys import exit
import os
from class_dino import Dino
from class_nuvem import Nuvem
from class_chao import Chao
from class_cacto import Cacto

pygame.init()
pygame.mixer.init()

#controlando os arquivos
diretorio_main = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_main, 'imagens')
diretorio_sons = os.path.join(diretorio_main, 'sons')

# tela
LARGURA, ALTURA = 640, 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Dino')
relogio = pygame.time.Clock()

# cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# spritesheets
sprite_sheet_1 = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png')).convert_alpha()

#sons
som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'sons_death_sound.wav'))
som_colisao.set_volume(2)

# objetos visiveis
todas_as_sprites = pygame.sprite.Group()

# colisões
grupo_obstaculos = pygame.sprite.Group()
colidiu = False


''' OBJETOS '''
# dino (visivel e colisor)
dinossauro = Dino(sprite_sheet_1, LARGURA, ALTURA)  # Cria uma instância da classe Dino
todas_as_sprites.add(dinossauro)

# chao (visivel)
for i in range(20):
    chao = Chao(sprite_sheet_1, LARGURA, ALTURA, i)
    todas_as_sprites.add(chao)

# nuvem (visivel)
for i in range (3):
    nuvem = Nuvem(sprite_sheet_1, LARGURA, ALTURA)
    todas_as_sprites.add(nuvem)

# cacto (visivel e colisor)
cacto = Cacto(sprite_sheet_1,LARGURA,ALTURA)
todas_as_sprites.add(cacto)
grupo_obstaculos.add(cacto)


''' LOOP PRINCIPAL '''
while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
        if evento.type == KEYDOWN:
            if evento.key == K_SPACE:
                if dinossauro.rect.y != dinossauro.posic_inicial_Y:
                    pass
                else:
                    dinossauro.pular()

    todas_as_sprites.draw(tela)

    #a condição true ou false diz se o objeto vai sumir ou não
    colisoes = pygame.sprite.spritecollide(dinossauro, grupo_obstaculos, False, pygame.sprite.collide_mask)
    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True

    if colidiu == True:
        pass
    else:
        todas_as_sprites.update()
    
    pygame.display.flip()
