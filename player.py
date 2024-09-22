from circleshape import  CircleShape
import pygame
import constants

class Player(CircleShape):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y,constants.PLAYER_RADIUS)
        self.rotation = 0

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
        self.position += forward * constants.PLAYER_SPEED*dt

    def update(self, dt):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.translate(dt)
        
        if keys[pygame.K_s]:
            self.translate(-dt)


    
