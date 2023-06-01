#Image scaling refers to the resizing of the original image.
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Scaling')
image = pygame.image.load('images/fonot.jpg')
image = pygame.transform.scale(image,(400, 400))

while True:
    screen.fill("White")
    # Screen.blitme(image,imagerect) #using the rect object
    screen.blit(image,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            quit()
    pygame.display.update()