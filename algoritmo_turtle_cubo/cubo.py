import turtle

def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(3) 

def draw_line(x1, y1, x2, y2):
    steps = 20 
    for i in range(steps + 1):
        t = i / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        draw_point(x, y)

def draw_cube():
    # Definir los vértices del cubo en 2D (perspectiva simple)
    vertices = [
        (-50, -50), (50, -50), (50, 50), (-50, 50),  
        (-30, -30), (70, -30), (70, 70), (-30, 70)   
    ]
    
    # Dibujar las aristas del cubo con la función de línea
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  
        (4, 5), (5, 6), (6, 7), (7, 4),  
        (0, 4), (1, 5), (2, 6), (3, 7)   
    ]
    
    for edge in edges:
        draw_line(vertices[edge[0]][0], vertices[edge[0]][1],
                  vertices[edge[1]][0], vertices[edge[1]][1])


draw_cube()
turtle.done()
