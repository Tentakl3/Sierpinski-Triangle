from random import uniform
import secrets

class Solution():
    def __init__(self,n ,vertices ,width ,length):
        self.dice = []
        self.universe = [width, length]
        self.vertices = vertices
        self.res = []
        self.n = n
    
    def dado_build(self):
        for i in range(len(self.vertices)):
            self.dice.append(i)

    def dado_roll(self):
        return secrets.choice(self.dice)

    def random_vertice(self):
        vi = self.dado_roll()
        return self.vertices[vi]

    def random_punto(self):
        rx = uniform(-self.universe[0]/2,self.universe[0]/2)
        ry = uniform(-self.universe[1]/2,self.universe[1]/2)
        return [rx,ry]

    def cal_punto_medio(self, punto , vertice):
        x3 = (punto[0] + vertice[0])/2
        y3 = (punto[1] + vertice[1])/2
        return [x3,y3]
    
    def algoritmo(self):
        self.dado_build()
        holder = self.random_punto()
        vertice = self.random_vertice()
        self.res.append(self.cal_punto_medio(holder, vertice))

        for j in range(self.n):
            vertice = self.random_vertice()
            self.res.append(self.cal_punto_medio(self.res[j], vertice))

        return self.res
"""
if __name__ == "__main__":
    sol = Solution(10, [[0,0],[6,0],[3,5]], 800, 600)
    sol.algoritmo()
"""
"""
sol = Solution(100000)
sol.random_punto()
res = sol.recursivo([], [])

# Create a scatter plot
plt.scatter(res[0], res[1], color='blue', marker='o')
# Labeling the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Title of the plot
plt.title('Scatter Plot of Points')

# Show the plot
plt.grid(True)
plt.show()
"""