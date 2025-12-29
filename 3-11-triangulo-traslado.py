from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

posx = 0.0
posy = 0.0

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def dibujar_triangulo():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 1.0, 0.0)
    glTranslatef(posx, posy, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()
    glFlush()

def keyboard(key, x, y):
    global posx, posy
    paso = 0.05
    if key == GLUT_KEY_UP:
        posy += paso
    elif key == GLUT_KEY_DOWN:
        posy -= paso
    elif key == GLUT_KEY_LEFT:
        posx -= paso
    elif key == GLUT_KEY_RIGHT:
        posx += paso
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Movimiento de Triangulo - PyOpenGL")
    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutSpecialFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
