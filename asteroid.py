from circleshape import  CircleShape
import constants
import pygame
import random 


class Asteroid(CircleShape):
    
    

    def __init__(self,x,y, radius):
        super().__init__(x,y,radius)
        self.nb_vertices = random.randint(10,20)
        self.scale_vertices = [ random.uniform(0.6,1) for i in range(self.nb_vertices)]
    
    def asteroid_shape(self):
        vertices = []
        vect = pygame.Vector2(1, 0)
        for i in range(self.nb_vertices):
            vertices.append(self.position + self.scale_vertices[i]*vect*self.radius)
            vect = vect.rotate(360/self.nb_vertices)

        return vertices

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.asteroid_shape(),2)
    def split(self):
        self.kill()
        if self.radius<= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            split_directions = self.velocity.rotate(-random_angle), self.velocity.rotate(random_angle)
            split_radii = self.radius - constants.ASTEROID_MIN_RADIUS
            
            asteroids = Asteroid(self.position.x, self.position.y, split_radii), Asteroid(self.position.x, self.position.y, split_radii)
            asteroids[0].velocity = split_directions[0]
            asteroids[1].velocity = split_directions[1]



    def update(self,dt):
        self.position += self.velocity * dt