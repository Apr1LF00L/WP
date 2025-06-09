import pygame
import constantes


class Personaje(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.forma = pygame.image.load('recursos/Soldier.jpg').convert_alpha()
        self.forma.center = (x,y)


    def movimiento(self,delta_x,delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz,constantes.COLOR_PERSONAJE,self.forma)
