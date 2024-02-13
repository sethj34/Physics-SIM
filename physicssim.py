import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Free Fall Simulation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EARTHCOLOR = (2, 60, 167)
JUPITERCOLOR = (188, 175, 178)
VENUSCOLOR = (255, 181, 104)
MARSCOLOR = (135, 32, 44)

g_earth = 9.8
g_jupiter = 23.1
g_venus = 8.9
g_mars = 3.7

deltat = 0.1
ivelocity = 0

def earth(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

def jupiter(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

def venus(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

def mars(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)


def main():
    run = True
    clock = pygame.time.Clock()

    objectypos_earth = 200
    objectypos_jupiter = 200
    objectypos_venus = 200
    objectypos_mars = 200

    radius = 25
    coefelasticpotene = 0.76

    velocity_earth = ivelocity
    velocity_jupiter = ivelocity
    velocity_venus = ivelocity
    velocity_mars = ivelocity

    fontpath = "C:/Users/sethj/AppData/Local/Microsoft/Windows/Fonts/Gidole-Regular.ttf"
    fontsize = 50
    font = pygame.font.Font(fontpath, fontsize)

    text_earth = font.render("Earth", True, WHITE)
    text_jupiter = font.render("Jupiter", True, WHITE)
    text_venus = font.render("Venus", True, WHITE)
    text_mars = font.render("Mars", True, WHITE)

    while run:
        clock.tick(200)
        WIN.fill(BLACK)

        WIN.blit(text_earth, (((WIDTH / 5) - 58), 150))
        WIN.blit(text_jupiter, (((2 * WIDTH / 5) - 76), 150))
        WIN.blit(text_venus, (((3 * WIDTH / 5) - 69), 150))
        WIN.blit(text_mars, (((4 * WIDTH / 5) - 55), 150))

        earth(WIN, EARTHCOLOR, (WIDTH / 5, objectypos_earth), radius)
        jupiter(WIN, JUPITERCOLOR, ((2 * WIDTH / 5), objectypos_jupiter), radius)
        venus(WIN, VENUSCOLOR, ((3 * WIDTH / 5), objectypos_venus), radius)
        mars(WIN, MARSCOLOR, ((4 * WIDTH / 5), objectypos_mars), radius)

        # EARTH

        velocity_earth += g_earth * deltat
        objectypos_earth += velocity_earth * deltat

        if objectypos_earth + radius > HEIGHT:
            objectypos_earth = HEIGHT - radius
            velocity_earth *= -coefelasticpotene

        # jupiter
            
        velocity_jupiter += g_jupiter * deltat
        objectypos_jupiter += velocity_jupiter * deltat

        if objectypos_jupiter + radius > HEIGHT:
            objectypos_jupiter = HEIGHT - radius
            velocity_jupiter *= -coefelasticpotene
        
        # VENUS
            
        velocity_venus += g_venus * deltat
        objectypos_venus += velocity_venus * deltat

        if objectypos_venus + radius > HEIGHT:
            objectypos_venus = HEIGHT - radius
            velocity_venus *= -coefelasticpotene

        # MARS
            
        velocity_mars += g_mars * deltat
        objectypos_mars += velocity_mars * deltat

        if objectypos_mars + radius > HEIGHT:
            objectypos_mars = HEIGHT - radius
            velocity_mars *= -coefelasticpotene


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False

    pygame.quit()
    sys.exit()
    

main()

# REFERENCES
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html
# https://fontlibrary.org/en/font/gidole-regular
# https://www.scienceworld.ca/resource/elastic-energy/
# https://www.pygame.org/docs/