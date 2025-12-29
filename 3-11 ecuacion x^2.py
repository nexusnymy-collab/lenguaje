from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def inicializar():
    glClearColor(0.1, 0.0, 0.0, 1.0)  # Fondo rojo oscuro
    glPointSize(3)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3.0, 3.0, -1.0, 1.0, -1, 1)  # Rango ajustado para ver y=x^2

def dibujar_ecuacion():   
    glClear(GL_COLOR_BUFFER_BIT)

    # ----- Dibujar ejes -----
    glColor3f(1.0, 1.0, 0.0)  # Amarillo
    glBegin(GL_LINES)
    glVertex2f(-3.0, 0.0)
    glVertex2f(3.0, 0.0)     # Eje X
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)    # Eje Y
    glEnd()

    # ----- Dibujar parábola -----
    glColor3f(0.2, 0.8, 1.0)  # Celeste
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-3, 3, 200):
        y = x**2
        glVertex2f(x, y)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Dibujar ecuacion y = x^2 en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_ecuacion)
    glutMainLoop()

if __name__ == "__main__":
    main()

