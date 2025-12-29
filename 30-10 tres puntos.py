from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0) # Fondo gris oscuro
    glPointSize(3)                  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10,10, -4, 4, -1, 1) # Vista ortográfica 2D

def dibujar_triangulo():
    """Dibuja 3 puntos formando un triángulo"""
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 1.0, 0.0) # Color amarillo
    glBegin(GL_LINE_STRIP)

   
    glVertex2f(-8.0, 3.0)    # Vértice superior izquierdo
    glVertex2f(-8.0, -3.0)  # Vértice inferior izquierdo
    glVertex2f(-4.0, -3.0)   # Vértice inferior derecho
    glVertex2f(-4.0, 3.0)   # Vértice superior derecho
    glEnd()
    
    glBegin(GL_LINE_STRIP)
    glVertex2f(-2.0, -3.0)    # Vértice superior izquierdo
    glVertex2f(-2.0, 3.0)  # Vértice inferior izquierdo
    glVertex2f( 2.0, -3.0)   # Vértice inferior derecho
    glVertex2f( 2.0, 3.0)   # Vértice superior derecho
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex2f(5.0, -3.0)    # Vértice superior izquierdo
    glVertex2f(7.0, 3.0)  # Vértice inferior izquierdo
    glVertex2f(9.0, -3.0)   # Vértice inferior derecho
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(6, 0)    # barra del medio
    glVertex2f(8, 0)    # barra del medio
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangulo de puntos en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutMainLoop()

if __name__ == "__main__":
    main()
