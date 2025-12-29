from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angulo = 0.0

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def dibujar():
    global angulo
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(angulo, 0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.6)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.6, -0.4)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.6, -0.4)
    glEnd()
    glFlush()

def teclado_normal(key, x, y):
    global angulo
    if key == b'n':       # tecla 'n' → gira a la izquierda
        angulo += 5
    elif key == b'm':     # tecla 'm' → gira a la derecha
        angulo -= 5
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Rotacion con N y M - PyOpenGL")
    inicializar()
    glutDisplayFunc(dibujar)
    glutKeyboardFunc(teclado_normal)
    glutMainLoop()

if __name__ == "__main__":
    main()

