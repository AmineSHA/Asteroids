import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import *
def main():

    print("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots  = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        
        for element in updatable:
            element.update(dt)
        
        for asteroid  in asteroids:
            if asteroid.isColliding(player):
                print("Game over!")
                raise SystemExit("Exiting program")
            
            for shot in shots:
                if shot.isColliding(asteroid):
                    asteroid.split()
                    shot.kill()
        
        screen.fill((0,0,0))

        for element in drawable: 
            element.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

        
        
        


    

if __name__ == "__main__":
    main()
