import pygame
from pygame.constants import QUIT
import random as rd

# Initialization and setup
pygame.init()#initie le jeu?
# FPS = pygame.time.Clock()#wtf??? ça sert à rien pour toi
# flags = pygame.RESIZABLE#wtf?????? pareil 
screen = width, height = 1280, 720
main_surface = pygame.display.set_mode(screen)#gère les fenêtres et affichage graphique, ici c'est pour la création de la fenêtre
# Oui en gros le main_surface ça être la partie sur laquelle tu vas changer des choses (écrire, changer le background)
timer_size=80
timer_font = pygame.font.SysFont('Calibri', timer_size,bold=True)
record_size=100 #taille de l'écriture du "Record battu!!" oui
record_font=pygame.font.SysFont('Calibri',record_size,bold=True)#bold = gras, font pour le type de l'écriture etc..
start_again_size=50# taille de l'écriture "Rejouer"
start_again_font=pygame.font.SysFont('Calibri',start_again_size,bold=True)
# Pour être plus rapide tu peux juste écrire comme ça 
# timer_font = pygame.font.SysFont('Calibri', 80,bold=True)
# ça t'enlèves la ligne de définition de la taille d'écriture

# The color as the text have been picked up on the website https://humanbenchmark.com/tests/reactiontime 
# Là c'est l'initialistion des couleurs
GREEN = [0, 255, 0]
RED = [255, 0, 0]
MAUVE = [178, 102, 255]
WHITE = [255, 255, 255]

# Function to generate a random delay
def generate_random_delay():
    return rd.randint(1000, 5000)  # Delay in milliseconds (1 to 5 seconds)

# Variables initialisation
record = 10000#initialisation d'un recors énorme comme ça on est sur qu'il soit battu
# oui exactement, après si tu veux tes pas obliger de faire un truc avec un record c'est plus simple sans

home = True #obligé de faire ça car sinon il y une erreur car True est pour tout
# En gros, ton home=True il sert à faire tourner ta boucle principal, dès que tu le mets sur False, ça sort
click = 0       # variable booléenne pour rentrer dans la zone initiale d'affichage
# initialisation simple de différentes variables
reaction_time = 0   
random_delay = 0
data=[]# liste où il y aura tous les délais pour chaque clic
# oui après cette liste n'est pas forcément utile, à voir ce que tu peux faire avec
quit=0#la croix pour fermer?????
# En gros le quit c'est la variable qui va te permettre de sortir du programme en cliquant sur la croix
# mais quand tu es dans la deuxième boucle while.

# ratio=1 # ça, ça te sert à rien, c'est pour changer la taille de la fenêtre 
# standard_ratio=1  # ça pareil
# standard_screen= standard_w, standard_h=screen # ça pareil

# Main loop that launches the game
while home:#on est obligé de faire des boucles while avec pygame, oui c'est pour faire tourner la boucle de la fenêtre et donc pour 
    # afficher les informations que l'on souhaite
    play = False#la boucle s'arrête?? Non ça c'est l'intialisation de la variable booléenne de la deuxième boucle
    # La première boucle te sert à afficher ton accueil et la deuxième à jouer, d'où le nom des variables : home et play
    # Le nom des variables n'est jamais un hasard ça permet de savoir aussi ce que le code fait, ça remplace un peu les commentaire
    # En tous cas parfois ça peut éviter d'en mettre
    enter = 0#0 = False en Python donc la même chose que au-dessus????
    # en gros ça c'est pour voir si ta déjà déclencher le chrono quand ton délai aléatoire est fini
    

    # Les boucles for event in pygame.event.get() sont là pour observer si l'utilisateur fait quelque chose avec les périphériques
    # ça peut être la souris ou le clavier ou les deux
    for event in pygame.event.get():
        # c'est donc pour quitter avec la croix
        if event.type == QUIT:  # Quit the game
            home = False

        # ça c'est si tu cliques sur al 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # évènement de type clique sur souris et button ==1 
                                                                       # correpond au clique gauche
            start_delay = pygame.time.get_ticks()    # ça ça met dans une variable le temps auquel ta cliquer et dcp on va s'en servir
                                                     # ensuite pour savoir si le délai est dépassé ou non 
            random_delay = generate_random_delay()   # ça pour ça te génère un temps aléatoire entre 1 et 5 secondes
            play = True    # ça, ça te permet de rentrer dans la deuxième boucle while 
            broken_record=0 # variable booléenne pour savoir si tu rentres dans l'écriture "record battu"
            # Elle est réinitialiser à chaque fois que tu recommence le jeu, c'est pour ça qu'elle est disposé ici dans le code et non
            # avant l'entrer dans la première boucle while. Car sinon une fois que tu l'auras changer sur 1 ou True, tu auras 
            # toujours la phrase "record battu" qui s'affiche, car tu ne la réinitialises pas

        # Tout ça c'est pour la partie adaptation à différentes tailles de fénêtre, je te le laisse dans le cas où tu veux l'utiliser
            # c'est plus propre mais plus complexe à faire, assez dur à comprendre et pas forcément utile pour ce que tu as besoin de 
            # faire principalement
        
        # if event.type == pygame.VIDEORESIZE:
        #         # Update the width and height if the window is resized
        #         ratio_w = standard_w/event.w
        #         ratio_h = standard_h/event.h

        #         if ratio_w<1 and ratio_h<1:
        #             ratio = min(ratio_w, ratio_h)
        #         elif ratio_w<1 and ratio_h>1:
        #             ratio=ratio_h
        #         elif ratio_w>1 and ratio_h<1:
        #             ratio=ratio_w
        #         elif ratio_w>1 and ratio_h>1:
        #             ratio = max(ratio_w, ratio_h)

        #         screen= width, height = event.w, event.h
        #         timer_font = pygame.font.SysFont('Calibri', round(timer_size/ratio),bold=True)
        #         record_font=pygame.font.SysFont('Calibri',round(record_size/ratio),bold=True)
        #         start_again_font=pygame.font.SysFont('Calibri',round(start_again_size/ratio),bold=True)
        #         main_surface = pygame.display.set_mode((width, height), flags)

    # Display based on different options, all the display should be able to adapt to the screen size
    # # ton click == 0 ça représente ton home, l'endroit où tu arrives lorsque tu lances le programme 
    if click == 0:
        main_surface.fill(MAUVE)
        click_to_start_text=timer_font.render("Cliquer pour commencer", True, WHITE)
        # En gros les deux lignes qui suivent, c'est pour pouvoir choisir l'emplacement du texte et ça prend
        # en compte la taille du text, car selon les phrases tu ne vas pas les positionner au même endroit
        text_width, text_height = click_to_start_text.get_size()                # ça ça récupère la taille du texte
        x,y=(width - text_width)//2 , (height - text_height)//2                 # able to adapt to the text
        main_surface.blit(click_to_start_text, (x,y))
        # ce gros block peut se faire en une ligne mais c'est moins précis et tu peux pas faire autant de chose mais tema
        # main_surface.blit(timer_font.render("Cliquer pour commencer", True, WHITE),(screen[0]*3//10,screen[1]*3//10))
        # screen[0] c'est pour choisir l'endroit en largeur, et screen[1] c'est l'endroit en hauteur

    # Le click == 1 représente l'endroit où tu vas afficher le score et tout et tout
    # et ensuite, chaque petit bout de code dans les condition tu peux les faire comme je t'ai montrer en un ligne, comme ça, 
    # ça peut être plus claire et plus concis pour toi
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
        
    # Ton click == 2 représente ton cas où tu vas cliquer avant la fin du délai   
    elif click == 2:
        main_surface.fill(MAUVE)
        too_soon_text=timer_font.render("Trop rapide, clique pour recommencer", True, WHITE)
        text_width, text_height = too_soon_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)//2
        main_surface.blit(too_soon_text,(x,y))

    # comme indiquer ce pygame.display.flip te met à jour ta fenêtre 
    pygame.display.flip()  # Update the display


    # Bon pour l'instant on n'a fait que de l'affichage mais rien ne s'est véritablement passer en terme de jeu
    # on a juste défini les différent cas possible à afficher, lorsque l'on ne joue pas
    # Comme indiquer au dessus la variable play est mise sur True lorsque l'on va cliquer la première fois
    while play:
        # à partir de ce moment là, on va venir afficher l'écran rouge avec la consigne
        main_surface.fill(RED)
        # Ici c'est encore la même histoire, tu peux faire tout en une ligne
        wait_text=timer_font.render("Attend le vert", True, WHITE)
        text_width, text_height = wait_text.get_size()
        x,y=(width - text_width)//2 , (height - text_height)//2
        main_surface.blit(wait_text,(x,y))

        if pygame.time.get_ticks() - start_delay > random_delay:
           # Ici c'est le cas où le délai est dépassé la formule c'est:
           # temps actuel - temps enregistré au moment où on a cliqué > délai aléatoire généré par la fonction au moment où 
           # on a cliqué 
            main_surface.fill(GREEN)
            click_as_fast_text=timer_font.render("Clique le plus vite possible", True, WHITE)
            text_width, text_height = click_as_fast_text.get_size()
            x,y=(width - text_width)//2 , (height - text_height)//2
            main_surface.blit(click_as_fast_text,(x,y))

            if enter == 0: # on retrouve ici le booléeen enter qui permet de savoir si le temps de départ du chono pour le temps 
                            # de réaction à bien été enregistré. Si enter ==1 ça veut dire que le temps est déjà enregistré et donc on 
                            # a pas besoin de rentrer de nouveau dans la condition et de ré enregistré le temps de départ
                start_time = pygame.time.get_ticks()  # on prend donc le temps actuel
                enter = 1           # on oubli pas de dire avec cette variable que le temps de départ est bien enregistré

        # Même boucle que dans l'accueil 
        for event in pygame.event.get():
            if event.type == QUIT:
                # la différence c'est que pour quitter le jeu on doit sortir de deux boucle et donc on doit mettre play sur False et 
                # quit sur 1, car à la toute fin de le boucle home, il y a une condition pour savoir si l'on sort ou pas
                play = False
                quit=1
            # là on va venir voir le clique qui va mesurer le temps de réaction
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Clique gauche comme tout à l'heure
                if pygame.time.get_ticks() - start_delay > random_delay:   # Même condition que pour afficher "Cliquez le plus vite possible"
                    reaction_time = pygame.time.get_ticks() - start_time # ici on calcule le temps de réaction avec les différents
                    # enregistrements de temps que l'on a fait précédemment
                    data.append(reaction_time)  # ça on s'en fout à part si tu veux faire quelque chose avec les temps de réaction derrière 
                    click = 1   # Ici on indique que lorsque l'on va sortir de la boucle play il va falloir aller dans la condition qui 
                    # affiche le score
                    play = False # ici on indique qu'on veut sortir de la boucle de jeu, on retourne à l'accueil à la fin de l'exécution de
                    # la boucle


                    # In case of improvement
                    # Si on bat le record, on le met à jour
                    if reaction_time < record:
                        record = reaction_time
                        broken_record=1 # on vient dire ici qu'il faudra afficher "record battu"
                else: # le else correspond au cas où on a cliquer trop vite et donc que l'on a pas dépasser le délai
                    click = 2   # dans ce cas on indique qu'à la sortie de la boucle de jeu qu'il faudra afficher "trop tôt"
                    play = False # on vient indiquer que l'on veut sortir de la boucle de jeu

            # Tout ça c'est pour la partie adaptation à différentes tailles de fénêtre, je te le laisse dans le cas où tu veux l'utiliser
            # c'est plus propre mais plus complexe à faire, assez dur à comprendre et pas forcément utile pour ce que tu as besoin de 
            # faire principalement

            # if event.type == pygame.VIDEORESIZE:
            #     # Update the width and height if the window is resized
            #     screen = width, height = event.w, event.h
            #     main_surface = pygame.display.set_mode((width, height), flags)
            #     ratio_w = standard_w/event.w
            #     ratio_h = standard_h/event.h

            #     if ratio_w<1 and ratio_h<1:
            #         ratio = min(ratio_w, ratio_h)
            #     elif ratio_w<1 and ratio_h>1:
            #         ratio=ratio_h
            #     elif ratio_w>1 and ratio_h<1:
            #         ratio=ratio_w
            #     elif ratio_w>1 and ratio_h>1:
            #         ratio = max(ratio_w, ratio_h)

            #     screen= width, height = event.w, event.h
            #     timer_font = pygame.font.SysFont('Calibri', round(timer_size/ratio),bold=True)
            #     record_font=pygame.font.SysFont('Calibri',round(record_size/ratio),bold=True)
            #     start_again_font=pygame.font.SysFont('Calibri',round(start_again_size/ratio),bold=True)
            #     main_surface = pygame.display.set_mode((width, height), flags)
    

        pygame.display.flip() #met à jour l'écran exactement
    if quit==1: # ici c'est la condition qui permet de quitter le jeu lorsque l'on se trouve dans la deuxième boucle
        home=False

# Évidemment si l'on vient à sortir des deux boucles il faut que le jeu s'arrête, d'où le pygame.quit()
pygame.quit()

# Pour finir si tu tej la partie adaptative à la taille de la fenêtre et que tu réduis chaque écriture à une ligne 
# ton code en devrait pas être si long que ça. Essaie de comprendre chaque commentaire que j'ai fait même si c'est un peu long
# et pose moi des questions demain si il y a des trucs que tu ne comprends pas.