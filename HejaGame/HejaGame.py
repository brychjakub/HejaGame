import pygame, random

#Initiailze pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

CD_HIT = pygame.USEREVENT + 1

slava_sound = pygame.mixer.Sound('slava.mp3')
background_sound = pygame.mixer.Sound('vesela_prihoda.mp3')
background_sound.play(-1)
    



dark_green = (80,150,75)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Heja Game!")

system_font = pygame.font.SysFont('calibri', 35)



image_height = 50
image_width = 50

FPS = 60
clock = pygame.time.Clock()

VELOCITY = 8

background_image = pygame.transform.scale(pygame.image.load("background.jpg"), (WINDOW_WIDTH, WINDOW_HEIGHT))

player_image = pygame.image.load("hlava.jpg")
player = pygame.transform.scale(player_image, (image_width,image_height))
player_rect = player.get_rect()
player_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

CD_image = pygame.transform.scale(pygame.image.load("CD.jpg"), (image_width,image_height))
CD_rect = CD_image.get_rect()
CD_rect.topleft = (23,25)

CD_counter = 0
   

#The main game loop


running = True
while running:
    #Loop through a list of Event objects that have occured
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_rect.left > 0:
        player_rect.x -= VELOCITY   
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_rect.right < WINDOW_WIDTH:
        player_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w])and player_rect.top > 0 + image_height:
        player_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s])and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += VELOCITY

    

    display_surface.fill((0,0,0))
    display_surface.blit(background_image, (0,0))
    display_surface.blit(player, player_rect)
    display_surface.blit(CD_image, CD_rect)
           
    if player_rect.colliderect(CD_rect):
        slava_sound.play()
        CD_counter += 1
        CD_rect.x = random.randint(0, WINDOW_WIDTH - image_width)  
        CD_rect.y = random.randint(0, WINDOW_HEIGHT - image_width)

    system_text = system_font.render("Chyť si svoje cédo! Teď máš " + str(CD_counter), 1, dark_green, True)
    system_text_rect = system_text.get_rect()
    system_text_rect.center = (WINDOW_WIDTH//2, 20)

    display_surface.blit(system_text, system_text_rect)



    pygame.display.update() 
    
    clock.tick(FPS)

#End the game
pygame.quit()


