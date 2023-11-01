import pygame
from pygame.constants import QUIT
import random as rd


# Initialization and setup
pygame.init()
FPS = pygame.time.Clock()
flags = pygame.RESIZABLE
screen = width, height = 1280, 720
pygame.display.set_caption("Reaction game")
main_surface = pygame.display.set_mode(screen,flags)
timer_size=80
timer_font = pygame.font.SysFont('Calibri', timer_size,bold=True)
record_size=100
record_font=pygame.font.SysFont('Calibri',record_size,bold=True)
start_again_size=50
start_again_font=pygame.font.SysFont('Calibri',start_again_size,bold=True)

# The color as the text have been picked up on the website https://humanbenchmark.com/tests/reactiontime 
GREEN = [75, 219, 106]
RED = [206, 38, 54]
BLUE = [43, 135, 209]
WHITE = [255, 255, 255]

# Function to generate a random delay
def generate_random_delay():
    return rd.randint(1000, 5000)  # Delay in milliseconds (1 to 5 seconds)

# Variables initialization
record = 10000
broken_record=0
home = True
click = 0
reaction_time = 0
random_delay = 0
data=[]
quit=0
ratio=1
standard_ratio=1
standard_screen= standard_w, standard_h=screen

# Main loop that launches the game
while home:
    play = False
    enter = 0
    

    # If something happens on the home page
    for event in pygame.event.get():
        if event.type == QUIT:  # Quit the game
            home = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left click
            start_delay = pygame.time.get_ticks()
            random_delay = generate_random_delay()
            play = True
            broken_record=0
        
        if event.type == pygame.VIDEORESIZE:
                # Update the width and height if the window is resized
                ratio_w = standard_w/event.w
                ratio_h = standard_h/event.h

                if ratio_w<1 and ratio_h<1:
                    ratio = min(ratio_w, ratio_h)
                elif ratio_w<1 and ratio_h>1:
                    ratio=ratio_h
                elif ratio_w>1 and ratio_h<1:
                    ratio=ratio_w
                elif ratio_w>1 and ratio_h>1:
                    ratio = max(ratio_w, ratio_h)
                
                # Update the size of the characters following the window size
                screen= width, height = event.w, event.h
                timer_font = pygame.font.SysFont('Calibri', round(timer_size/ratio),bold=True)
                record_font=pygame.font.SysFont('Calibri',round(record_size/ratio),bold=True)
                start_again_font=pygame.font.SysFont('Calibri',round(start_again_size/ratio),bold=True)
                main_surface = pygame.display.set_mode((width, height), flags)

    # Display based on different options, all the display should be able to adapt to the screen size 
    if click == 0:
        main_surface.fill(BLUE)
        click_to_start_text=timer_font.render("Click to start", True, WHITE)
        text_width, text_height = click_to_start_text.get_size()                # These two lines are here to make the content
        x,y=(width - text_width)//2 , (height - text_height)//2                 # able to adapt to the text
        main_surface.blit(click_to_start_text, (x,y))
    elif click == 1:
        main_surface.fill(BLUE)
        if broken_record:
            record_text=record_font.render("Well done! Record broken!!!", True, WHITE)
            text_width, text_height = record_text.get_size()
            x,y=(width - text_width)//2 , (height - text_height)//6
            main_surface.blit(record_text, (x,y))
        else:
            stay_focus_text=record_font.render("You can do better! Focus!!", True, WHITE)
            text_width, text_height = stay_focus_text.get_size()
            x,y=(width - text_width)//2 , (height - text_height)//6
            main_surface.blit(stay_focus_text,(x,y))

        start_again_text=start_again_font.render("Click to start again", True, WHITE)
        text_width, text_height = start_again_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)*7//10

        main_surface.blit(start_again_text, (x,y))
        your_time_text=timer_font.render("Your time: " + str(reaction_time) + " ms", True, WHITE)
        text_width, text_height = your_time_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)*4//10
        main_surface.blit(your_time_text,(x,y))

        record_value_text=timer_font.render("Record: " + str(record) + " ms", True, WHITE)
        text_width, text_height = record_value_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)*5//10
        main_surface.blit(record_value_text,(x,y))
        
    elif click == 2:
        main_surface.fill(BLUE)
        too_soon_text=timer_font.render("Too soon, click to start again", True, WHITE)
        text_width, text_height = too_soon_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)//2
        main_surface.blit(too_soon_text,(x,y))

    pygame.display.flip()  # Update the display

    # When the first click is done, the game really starts
    while play:
        main_surface.fill(RED)
        wait_text=timer_font.render("Wait for green", True, WHITE)
        text_width, text_height = wait_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)//2
        main_surface.blit(wait_text,(x,y))

        # Check whether or not the delay is over
        if pygame.time.get_ticks() - start_delay > random_delay:
            main_surface.fill(GREEN)
            click_as_fast_text=timer_font.render("Click as fast as you can", True, WHITE)
            text_width, text_height = click_as_fast_text.get_size()
            x,y=(width - text_width)//2 , (height - text_height)//2
            main_surface.blit(click_as_fast_text,(x,y))

            if enter == 0:
                start_time = pygame.time.get_ticks()
                enter = 1  # To not enter again in the condition

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


                    # In case of improvement
                    if reaction_time < record:
                        record = reaction_time
                        broken_record=1
                else:
                    click = 2
                    play = False
            if event.type == pygame.VIDEORESIZE:
                # Update the width and height if the window is resized
                screen = width, height = event.w, event.h
                main_surface = pygame.display.set_mode((width, height), flags)
                # The ratio is always calculated with the original size of the window
                ratio_w = standard_w/event.w
                ratio_h = standard_h/event.h

                if ratio_w<1 and ratio_h<1:
                    ratio = min(ratio_w, ratio_h)
                elif ratio_w<1 and ratio_h>1:
                    ratio=ratio_h
                elif ratio_w>1 and ratio_h<1:
                    ratio=ratio_w
                elif ratio_w>1 and ratio_h>1:
                    ratio = max(ratio_w, ratio_h)

                # Update the size of the characters following the window size
                screen= width, height = event.w, event.h
                timer_font = pygame.font.SysFont('Calibri', round(timer_size/ratio),bold=True)
                record_font=pygame.font.SysFont('Calibri',round(record_size/ratio),bold=True)
                start_again_font=pygame.font.SysFont('Calibri',round(start_again_size/ratio),bold=True)
                main_surface = pygame.display.set_mode((width, height), flags)
    

        pygame.display.flip()
    if quit==1: # To get out of the game when we are in the second loop
        home=False

pygame.quit()