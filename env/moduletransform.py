import pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Loading image')
image = pygame.image.load('images/fonot.jpg')
image = pygame.transform.flip(image, True, False)
image = pygame.transform.rotozoom(image, 90, 1.5)
image = pygame.transform.scalex2(image)

while True:
    screen.fill("white")
    # Screen.blitme(image,imagerect) #using the rect object
    screen.blit(image,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            quit()