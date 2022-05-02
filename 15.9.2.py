import turtle
class retangulo:
    "receve parametros de um retangulo"
def draw(t, retangulo):
    for i in range(2):
        t.fd(retangulo.width)
        t.lt(90)
        t.fd(retangulo.height)
        t.lt(90)


box = retangulo()
box.width = 100.0
box.height = 200.0
t = turtle.Turtle()
x = draw(t, box)
