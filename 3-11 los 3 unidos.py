from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variables globales
angulo = 0.0
posx = 0.0
posy = 0.0
escala = 1.0

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def dibujar():
    global angulo, posx, posy, escala
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Aplicar transformaciones en orden: traslado → rotación → escala
    glTranslatef(posx, posy, 0.0)
    glRotatef(angulo, 0.0, 0.0, 1.0)
    glScalef(escala, escala, 1.0)

    # Dibujar triángulo RGB
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)   # Rojo
    glVertex2f(0.0, 0.6)
    glColor3f(0.0, 1.0, 0.0)   # Verde
    glVertex2f(-0.6, -0.4)
    glColor3f(0.0, 0.0, 1.0)   # Azul
    glVertex2f(0.6, -0.4)
    glEnd()

    glFlush()

# Movimiento con las flechas
def teclas_especiales(key, x, y):
    global posx, posy
    paso = 0.1
    if key == GLUT_KEY_UP:
        posy += paso
    elif key == GLUT_KEY_DOWN:
        posy -= paso
    elif key == GLUT_KEY_LEFT:
        posx -= paso
    elif key == GLUT_KEY_RIGHT:
        posx += paso
    glutPostRedisplay()

# Rotación y escala con teclas normales
def teclado_normal(key, x, y):
    global angulo, escala
    if key == b'n':        # Rotar izquierda
        angulo += 5
    elif key == b'm':      # Rotar derecha
        angulo -= 5
    elif key == b'+':      # Aumentar tamaño
        escala += 0.1
    elif key == b'-':      # Disminuir tamaño
        escala = max(0.1, escala - 0.1)  # Evita tamaño negativo
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangulo - Movimiento, Rotacion y Escala (PyOpenGL)")
    inicializar()
    glutDisplayFunc(dibujar)
    glutSpecialFunc(teclas_especiales)
    glutKeyboardFunc(teclado_normal)
    glutMainLoop()

if __name__ == "__main__":
    main()
