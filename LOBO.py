from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0) # Fondo gris oscuro
    glPointSize(3)                  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-20,20, -10, 10, -1, 1) # Vista ortográfica 2D

def dibujar_triangulo():
    """Dibuja 3 puntos formando un triángulo"""
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 1.0, 0.0) # Color amarillo
    glBegin(GL_LINE_STRIP)
    glVertex2f(-8.0, 10.0)    # Vértice superior izquierdo
    glVertex2f(-9.0, 7.0)  # Vértice inferior izquierdo
    glVertex2f(-8.0, 4.0)   # Vértice inferior derecho
    glVertex2f(-7.0, 1.0)
    glVertex2f(-3.0, 4.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(3.0, 4.0)
    glVertex2f(7.0, 1.0)
    glVertex2f(8.0, 4.0)
    glVertex2f(9.0, 7.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(7.0, 10.0)
    glVertex2f(5.0, 9.0)
    glVertex2f(3.0, 7.0)
    glVertex2f(0.0, 7.0)
    glVertex2f(-3.0, 7.0)
    glVertex2f(-5.0, 9.0)
    glVertex2f(-7.0, 10.0)
    glVertex2f(-8.0, 10.0) # Vértice superior derecho
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
