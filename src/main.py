import pygame
import sys
from triangulo import Solution

class Fractal:
    def __init__(self, n, width=800, height=600):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.grid_size = 20
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Fractal")

        self.background_color = (255, 255, 255)
        self.grid_color = (200, 200, 200)
        self.circle_color = (0, 0, 255)
        self.circle_radius = 2

        self.n = n
        self.positions = []
        self.dice = []
        self.vertice = 0
        self.run_fractal = True

        self.screen.fill(self.background_color)

    def draw_grid(self):
        for x in range(0, self.screen_width, self.grid_size):
            pygame.draw.line(self.screen, self.grid_color, (x, 0), (x, self.screen_height))
        for y in range(0, self.screen_height, self.grid_size):
            pygame.draw.line(self.screen, self.grid_color, (0, y), (self.screen_width, y))
        
    def fractal(self):
        sol =  Solution(self.n,self.positions ,self.screen_width, self.screen_height)
        return sol.algoritmo()

    def refresh_background(self):
        self.screen.fill(self.background_color)
        self.draw_grid()

    def run(self):
        running = True
        self.refresh_background()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
           
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        self.positions.append(list(mouse_pos))
                        pygame.draw.circle(self.screen, self.circle_color, mouse_pos, self.circle_radius)
                        if len(self.positions) > 3:
                            self.refresh_background()
                            self.run_fractal = True

                    elif event.button == 3:
                        self.positions = []
                        self.refresh_background()
                        self.run_fractal = True

                if len(self.positions) >= 3 and self.run_fractal:
                    sol = self.fractal()
                    for k in range(len(sol)):
                        pygame.draw.circle(self.screen, self.circle_color, sol[k], self.circle_radius)
                    self.run_fractal = False

            pygame.display.flip()

            

if __name__ == "__main__":
    app = Fractal(10000)
    app.run()