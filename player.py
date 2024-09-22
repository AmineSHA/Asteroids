from circleshape import  CircleShape
import pygame
import constants
from shot import *

class Player(CircleShape):
    

    def __init__(self, x, y):
        super().__init__(x, y,constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0.0 
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius /1.5
        
        a = self.position + forward * self.radius 
        b = self.position - forward * self.radius - right 
        d = self.position - 0.75 * forward * self.radius 
        c = self.position - forward * self.radius + right
        
        return [a,b,d,c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED*dt 

    def translate(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def shoot(self):
        self.shot_timer = constants.PLAYER_SHOOT_COOLDOWN
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        corner = self.position + forward * self.radius
        shot = Shot(corner.x,corner.y)
        shot.velocity = forward * constants.SHOT_SPEED_PLAYER

    def update(self, dt):
        
        self.shot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.translate(dt)
        
        if keys[pygame.K_s]:
            self.translate(-dt)

        if keys[pygame.K_SPACE]: 
            if self.shot_timer<=0:
                self.shoot()



    
