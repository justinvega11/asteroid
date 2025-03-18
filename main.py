# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids,updateable, drawable)
    Player.containers = (updateable, drawable)
    Shot.containers = (shots,updateable,drawable)


    asteroidfield = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    

    while(True):
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
          screen.fill("black")
          updateable.update(dt)
          for asteroid in asteroids:
               if not asteroid.collision_check(player):
                    print("Game over!")
                    return
               for bullet in shots:
                    if not asteroid.collision_check(bullet):
                         bullet.kill()
                         asteroid.split()

          for draw in drawable:
               draw.draw(screen)
               
          
          pygame.display.flip()
          
          dt = clock.tick(60) / 1000

if __name__ == "__main__":
        main()
