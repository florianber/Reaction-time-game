import pygame
from pygame.constants import QUIT
import random as rd

# Initialization of the screen and the fonts
pygame.init()

screen = width, height = 1280, 720
main_surface = pygame.display.set_mode(screen)
timer_size=80
timer_font = pygame.font.SysFont('Calibri', timer_size,bold=True)
record_size=100 
record_font=pygame.font.SysFont('Calibri',record_size,bold=True)
start_again_size=50
start_again_font=pygame.font.SysFont('Calibri',start_again_size,bold=True)


# Color initialization
GREEN = [0, 255, 0]
RED = [255, 0, 0]
MAUVE = [178, 102, 255]
WHITE = [255, 255, 255]
JAUNE = [255,255,0]
BLEU = [0,162,255]
ROSE = [255,0,222]
GRIS = [35,35,35]
L_COLOR=[RED,MAUVE,JAUNE,BLEU,ROSE,GRIS]

# Function that generate a random delay
def generate_random_delay():
    return rd.randint(1000, 5000)  # This is in milliseconds

record = 10000
home = True 
click = 0       
reaction_time = 0   
random_delay = 0
data=[]
quit=0

# Main loop but we are in the home, not the game yet
while home:
    
    play = False
    enter = 0
    color_amount=None
  
    for event in pygame.event.get():
        
        if event.type == QUIT:  
            home = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                                                                       
            start_delay = pygame.time.get_ticks()                                      
            random_delay = generate_random_delay()   
            play = True    
            broken_record=0 
            
    # Manage the display following what the player did before
    if click == 0:
        main_surface.fill(MAUVE)
        click_to_start_text=timer_font.render("Cliquer pour commencer", True, WHITE)
        
        
        text_width, text_height = click_to_start_text.get_size()                
        x,y=(width - text_width)//2 , (height - text_height)//2                 
        main_surface.blit(click_to_start_text, (x,y))

    elif click == 1:
        main_surface.fill(MAUVE)
        if broken_record:
            record_text=record_font.render("Nouveau record!!!", True, WHITE)
            text_width, text_height = record_text.get_size()
            x,y=(width - text_width)//2 , (height - text_height)//6
            main_surface.blit(record_text, (x,y))
        else:
            stay_focus_text=record_font.render("Tu peux faire mieux! ", True, WHITE)
            text_width, text_height = stay_focus_text.get_size()
            x,y=(width - text_width)//2 , (height - text_height)//6
            main_surface.blit(stay_focus_text,(x,y))

        start_again_text=start_again_font.render("Clique pour recommencer", True, WHITE)
        text_width, text_height = start_again_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)*7//10

        main_surface.blit(start_again_text, (x,y))
        your_time_text=timer_font.render("Temps de réaction: " + str(reaction_time) + " ms", True, WHITE)
        text_width, text_height = your_time_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)*4//10
        main_surface.blit(your_time_text,(x,y))

        record_value_text=timer_font.render("Record: " + str(record) + " ms", True, WHITE)
        text_width, text_height = record_value_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)*5//10
        main_surface.blit(record_value_text,(x,y))
        
    
    elif click == 2:
        main_surface.fill(MAUVE)
        too_soon_text=timer_font.render("Trop rapide, cliquez pour recommencer", True, WHITE)
        text_width, text_height = too_soon_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)//2
        main_surface.blit(too_soon_text,(x,y))

    # Update the screen
    pygame.display.flip()  

    # Playing loop
    while play:
    
        if color_amount==None:
                
                color_amount= rd.randint(1,15)
                intervals=random_delay/color_amount
                intervals_plus_1=intervals
                color=rd.choice(L_COLOR)
            
        main_surface.fill(RED)
        wait_text=timer_font.render("Attend le vert", True, WHITE)
        text_width, text_height = wait_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)//2
        main_surface.blit(wait_text,(x,y))

        # Manage variables and actions related to the time
        if pygame.time.get_ticks()-start_delay<intervals_plus_1:
            
            main_surface.fill(color)
            wait_text=timer_font.render("Attend le vert", True, WHITE)
            text_width, text_height = wait_text.get_size()
            x,y=(width - text_width)//2 , (height - text_height)//2
            main_surface.blit(wait_text,(x,y))
        if pygame.time.get_ticks()-start_delay>intervals_plus_1:
            
            color=rd.choice(L_COLOR)
            main_surface.fill(color)
            wait_text=timer_font.render("Attend le vert", True, WHITE)
            text_width, text_height = wait_text.get_size()
            x,y=(width - text_width)//2 , (height - text_height)//2
            main_surface.blit(wait_text,(x,y))
            intervals_plus_1+=intervals

        if pygame.time.get_ticks() - start_delay > random_delay:
           
            main_surface.fill(GREEN)
            click_as_fast_text=timer_font.render("Clique le plus vite possible", True, WHITE)
            text_width, text_height = click_as_fast_text.get_size()
            x,y=(width - text_width)//2 , (height - text_height)//2
            main_surface.blit(click_as_fast_text,(x,y))

            if enter == 0: 
                                     
                start_time = pygame.time.get_ticks()  
                enter = 1           

        # Listen to the action that the player can do on the screen
        for event in pygame.event.get():
            if event.type == QUIT:
                
                play = False
                quit=1
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if pygame.time.get_ticks() - start_delay > random_delay:   
                    reaction_time = pygame.time.get_ticks() - start_time 
                    
                    data.append(reaction_time)  
                    click = 1   
                    play = False 
        
                    if reaction_time < record:
                        record = reaction_time
                        broken_record=1 
                else: 
                    click = 2   
                    play = False 

        pygame.display.flip() 
    
    # When the player click on the red cross
    if quit==1: 
        home=False


pygame.quit()