'''
Author: Michele Alladio, Samuele Forneris, Alessandro Seimandi, Nicolò La Valle
Descrizione:
Codice che implementa la cattura di oggetti di colore rosso tramite la libreria opencv.
Viene ricavata in modo ciclico la coordinata x dell'ogetto di colore rosso e viene utilizzata
per far muovere una macchina mediante la libreria PyGame.
'''

import pygame, sys, random, time
from pygame import mixer
from pygame.locals import *

#variabili globali
ALTEZZA = 700  #altezza schermata PyGame
#BASE = 1170  #base schermata PyGame
BASE = 1400
Y_PREDEFINITA = 550 #y della macchina nella schermata PyGame
X_PREDEFINITA = 550
SPAWN_1 = 20
SPAWN_2 = 140
X_SPAWN_CORSIA_1 = 450
X_SPAWN_CORSIA_2 = 650
X_SPAWN_CORSIA_3 = 860
LIM_MIN_PLAYER = 420
LIM_MAX_PLAYER = 900
VELOCITA_GIOCATORE = 7


velocita_nemico = 3
enemyX = X_SPAWN_CORSIA_1
enemyX2 = X_SPAWN_CORSIA_3
enemyY1 = -100
enemyY2 = -100
enemyY3 = -100
enemyY4 = -100
enemyY5 = -100
enemyY6 = -100

#inizializzazioni
pygame.init()
playerImg = pygame.image.load("player.png")
enemyImg = pygame.image.load("enemy.png")
background = pygame.image.load("Strada.png")
gameOverImg = pygame.image.load("GameOver.png")
gameOverImg = pygame.transform.scale(gameOverImg,(BASE, ALTEZZA))
background = pygame.transform.scale(background,(BASE, ALTEZZA))
clock = pygame.time.Clock()
screen = pygame.display.set_mode((BASE,ALTEZZA))    #schermo

#settaggio dei font
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)


def spawnNemici(enemyX, enemyY1, enemyY2, enemyY3, enemyX2, enemyY4, enemyY5, enemyY6, spawnaSeconda, velocita_nemico):
    screen.blit(background,(0, 0))  #impostazione dello sfondo
    screen.blit(enemyImg,(enemyX, enemyY1))    

    if enemyY3 <= ALTEZZA+100:    #se l'ultima auto è ancora nello schermo
        enemyY1 = enemyY1 + velocita_nemico   #incremento posizione della prima auto   
        if enemyY1 > SPAWN_1:   #quando la prima auto scende sotto una certa y parte la seconda auto
            screen.blit(enemyImg,(enemyX, enemyY2))
            enemyY2 = enemyY2 + velocita_nemico   #incremento posizione della seconda auto 
            if enemyY1 > SPAWN_2:   #quando la seconda auto scende sotto una certa y parte la terza auto
                screen.blit(enemyImg,(enemyX, enemyY3))
                enemyY3 = enemyY3 + velocita_nemico   #incremento posizione della terza auto
                if enemyY1 > SPAWN_2 + 220:
                    spawnaSeconda = True
    else:   #inizio nuova fila di auto
        enemyY3 = -100
        enemyY2 = -100
        enemyY1 = -100
        #scelta random della corsia per lo spawn della fila di automobili
        num = random.randint(1,4)
        if num == 1:
            enemyX = X_SPAWN_CORSIA_1
        elif num == 2:
            enemyX = X_SPAWN_CORSIA_2
        elif num == 3:
            enemyX = X_SPAWN_CORSIA_3

    if (enemyY3 >=300 and spawnaSeconda == True) or (enemyY6 <= ALTEZZA+100 and spawnaSeconda == True):
        screen.blit(enemyImg,(enemyX2, enemyY4))
        if enemyY6 <= ALTEZZA+100:
            enemyY4 = enemyY4 + velocita_nemico
            if enemyY4 > SPAWN_1:
                screen.blit(enemyImg,(enemyX2, enemyY5))
                enemyY5 = enemyY5 + velocita_nemico
                if enemyY4 > SPAWN_2:
                    screen.blit(enemyImg,(enemyX2, enemyY6))
                    enemyY6 = enemyY6 + velocita_nemico
        else:   #inizio di una nuova fila di auto
            velocita_nemico = velocita_nemico + 1
            enemyY4 = -100
            enemyY5 = -100
            enemyY6 = -100
            #scelta random della corsia per lo spawn della fila di automobili
            num = random.randint(1,4)   
            if num == 1:
                enemyX2 = X_SPAWN_CORSIA_1
            elif num == 2:
                enemyX2 = X_SPAWN_CORSIA_2
            elif num == 3:
                enemyX2 = X_SPAWN_CORSIA_3

    return enemyX, enemyY1, enemyY2, enemyY3, enemyX2, enemyY4, enemyY5, enemyY6, spawnaSeconda, velocita_nemico


def disegnaPlayer(playerX, playerY):
    screen.blit(playerImg,(playerX, playerY))  #la macchina viene impostata alla x rilevata da opencv

    

    pressed_keys = pygame.key.get_pressed()
    if playerX >= LIM_MIN_PLAYER:
        if pressed_keys[K_LEFT]:
            playerX=playerX-VELOCITA_GIOCATORE
    if playerX <= LIM_MAX_PLAYER:
        if pressed_keys[K_RIGHT]:
            playerX=playerX+VELOCITA_GIOCATORE

    

    return playerX, playerY
    

def controlloCollisioni(playerX, playerY, enemyX, enemyY1, enemyY2, enemyY3, enemyX2, enemyY4, enemyY5, enemyY6):
    if (((playerX >= enemyX-50 and playerX <= enemyX+50) and (playerY <= enemyY1+80 and playerY >= enemyY3)) or ((playerX >= enemyX2-50 and playerX <= enemyX2+50) and (playerY <= enemyY4+80 and playerY >= enemyY6))):
        screen.blit(gameOverImg,(0, 0))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()

def main():
    global enemyX, enemyY1, enemyY2, enemyY3, enemyX2, enemyY4, enemyY5, enemyY6

    playerX = X_PREDEFINITA
    playerY = Y_PREDEFINITA
    spawnaSeconda = False

    velocita_nemico = 10

    while True:
        enemyX, enemyY1, enemyY2, enemyY3, enemyX2, enemyY4, enemyY5, enemyY6, spawnaSeconda, velocita_nemico = spawnNemici(enemyX, enemyY1, enemyY2, enemyY3, enemyX2, enemyY4, enemyY5, enemyY6, spawnaSeconda, velocita_nemico)
        playerX, playerY = disegnaPlayer(playerX, playerY)

        controlloCollisioni(playerX, playerY, enemyX, enemyY1, enemyY2, enemyY3, enemyX2, enemyY4, enemyY5, enemyY6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #se l'evento è l'uscita
                pygame.quit()
                sys.exit()  #il programma termina in maniera pulita
        
        clock.tick(60)  #60 fps
        pygame.display.update() #update della finestra di pygame
        
main()