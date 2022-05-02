import math
class circle:
    "def circle(x, y, radius):"
class point:
    """Represents a point in 2-D space."""
def distancia_entre_pontos(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
def point_in_circle(point, circle):
    d = distancia_entre_pontos(point, circle.center)
    print(d)
    return d <= circle.radius

circulo = circle()
circulo.center = point()
circulo.center.x = 150.0
circulo.center.y = 100.0
circulo.radius = 75.0
ponto = point()
ponto.x = 30
ponto.y = 40
point_in_circle(ponto, circulo)

