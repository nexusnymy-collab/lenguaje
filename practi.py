from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glPointSize(5)                    # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -8, 8, -1, 1)    # Vista ortográfica 2D

def dibujar_triangulo():
    """Dibuja tres triángulos separados"""
    glClear(GL_COLOR_BUFFER_BIT)

    # ----- Triángulo 1 -----
    glColor3f(1.0, 1.0, 0.0)  # Amarillo
    glBegin(GL_TRIANGLES)
    glVertex2f(-8.0, -3.0)
    glVertex2f(-6.0, 3.0)
    glVertex2f(-4.0, -3.0)
    glEnd()

    # ----- Triángulo 2 -----
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glBegin(GL_TRIANGLES)
    glVertex2f(-1.0, -3.0)
    glVertex2f(1.0, 3.0)
    glVertex2f(3.0, -3.0)
    glEnd()

    # ----- Triángulo 3 -----
    glColor3f(0.0, 0.7, 1.0)  # Celeste
    glBegin(GL_TRIANGLES)
    glVertex2f(6.0, -3.0)
    glVertex2f(7.5, 3.0)
    glVertex2f(9.0, -3.0)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangulos en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutMainLoop()

if __name__ == "__main__":
    main()
