from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(4)
    glLineWidth(2)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -8, 8, -1, 1)  # Plano XY (más alto para el lobo)

def dibujar_lobo():
    """Dibuja el contorno geométrico del lobo"""
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)  # Amarillo

    # --- CONTORNO DEL LADO IZQUIERDO ---
    glBegin(GL_LINE_STRIP)
    coords = [
        (-1, -6), (-3, -5), (-4, -3), (-5, -1), (-6, 1),
        (-7, 3), (-5, 5), (-3, 6), (-2, 4), (-1, 3),
        (-2, 1), (-1, 0)
    ]
    for x, y in coords:
        glVertex2f(x, y)
    glEnd()

    # --- CONTORNO DEL LADO DERECHO (SIMÉTRICO) ---
    glBegin(GL_LINE_STRIP)
    coords = [
        (1, -6), (3, -5), (4, -3), (5, -1), (6, 1),
        (7, 3), (5, 5), (3, 6), (2, 4), (1, 3),
        (2, 1), (1, 0)
    ]
    for x, y in coords:
        glVertex2f(x, y)
    glEnd()

    # --- OREJA IZQUIERDA ---
    glBegin(GL_LINE_LOOP)
    coords = [(-5, 5), (-6, 6), (-5, 7), (-4, 6)]
    for x, y in coords:
        glVertex2f(x, y)
    glEnd()

    # --- OREJA DERECHA ---
    glBegin(GL_LINE_LOOP)
    coords = [(5, 5), (6, 6), (5, 7), (4, 6)]
    for x, y in coords:
        glVertex2f(x, y)
    glEnd()

    # --- OJOS ---
    glBegin(GL_LINE_STRIP)
    coords = [(-3, 1), (-2, 2), (-1, 1)]
    for x, y in coords:
        glVertex2f(x, y)
    glEnd()

    glBegin(GL_LINE_STRIP)
    coords = [(3, 1), (2, 2), (1, 1)]
    for x, y in coords:
        glVertex2f(x, y)
    glEnd()

    # --- NARIZ ---
    glBegin(GL_LINE_LOOP)
    coords = [(-1, -2), (1, -2), (0, -3)]
    for x, y in coords:
        glVertex2f(x, y)
    glEnd()

    # --- LÍNEA CENTRAL ---
    glBegin(GL_LINES)
    glVertex2f(0, -3)
    glVertex2f(0, 3)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Lobo Geometrico en OpenGL - Computacion Grafica")
    inicializar()
    glutDisplayFunc(dibujar_lobo)
    glutMainLoop()

if __name__ == "__main__":
    main()
