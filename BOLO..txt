from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0) # Fondo gris oscuro
    glPointSize(3)                  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-15,15, -15, 15, -1, 1) # Vista ortográfica 2D

def dibujar_triangulo():
    """conectar todos los puntos"""
    glClear(GL_COLOR_BUFFER_BIT)

    #parte orejas
    glColor3f(1.0, 1.0, 0.0) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(-8.0, 10.0)    
    glVertex2f(-9.0, 7.0)  
    glVertex2f(-8.0, 4.0)   
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
    glVertex2f(2.0, 6.0)
    glVertex2f(0.0, 7.0)
    glVertex2f(-2.0, 6.0)
    glVertex2f(-3.0, 7.0)
    glVertex2f(-5.0, 9.0)
    glVertex2f(-7.0, 10.0)
    glVertex2f(-8.0, 10.0)
    glEnd()

    #oreja interior izquierdo
    glBegin(GL_LINE_STRIP)
    glVertex2f(-4.0, 5.0)    
    glVertex2f(-4.0, 6.0)  
    glVertex2f(-5.0, 7.0)   
    glVertex2f(-7.0, 9.0)
    glVertex2f(-7.0, 4.0)
    glVertex2f(-6.0, 3.0)
    glVertex2f(-4.0, 5.0)
    glEnd()

    #oreja interior derecho
    glBegin(GL_LINE_STRIP)
    glVertex2f(4.0, 5.0)    
    glVertex2f(4.0, 6.0)  
    glVertex2f(7.0, 9.0)   
    glVertex2f(7.0, 7.0)
    glVertex2f(7.0, 5.0)
    glVertex2f(6.0, 4.0)
    glVertex2f(4.0, 5.0)
    glEnd()

    #parte cara
    glBegin(GL_LINE_STRIP)
    glVertex2f(-7.0, 1.0)    
    glVertex2f(-8.0,-3.0)  
    glVertex2f(-9.0,-7.0)   
    glVertex2f(-8.0,-7.0)
    glVertex2f(-7.0,-6.0)
    glVertex2f(-4.0,-9.0)
    glVertex2f(-1.0,-10.0)
    glVertex2f(1.0,-10.0)
    glVertex2f(4.0,-9.0)
    glVertex2f(7.0,-6.0)
    glVertex2f(8.0,-7.0)
    glVertex2f(9.0,-7.0)
    glVertex2f(8.0,-3.0)
    glVertex2f(7.0, 1.0)
    glEnd()

    #parte nariz
    glBegin(GL_LINE_STRIP)
    glVertex2f(-1.0, 0.0)    
    glVertex2f(-2.0,-4.0)  
    glVertex2f(-3.0,-6.0)   
    glVertex2f(-3.0,-7.0)
    glVertex2f(-1.0,-8.0)
    glVertex2f(1.0,-8.0)
    glVertex2f(3.0,-7.0)
    glVertex2f(3.0,-6.0)
    glVertex2f(2.0,-4.0)  
    glVertex2f(1.0, 0.0)
    glEnd()

    #nariz interior
    glBegin(GL_LINE_STRIP)
    glVertex2f(-1.0,-8.0)    
    glVertex2f(-2.0,-6.0)  
    glVertex2f(-1.0,-5.0)
    glVertex2f(1.0,-5.0)
    glVertex2f(2.0,-6.0)
    glVertex2f(1.0,-8.0)
    glEnd()

    #parte boca iz
    glBegin(GL_LINE_STRIP)
    glVertex2f(-5.0,-3.0)    
    glVertex2f(-4.0,-5.0)  
    glVertex2f(-3.0,-7.0)
    glEnd()

    #parte boca der
    glBegin(GL_LINE_STRIP)
    glVertex2f(3.0,-7.0)
    glVertex2f(4.0,-5.0)
    glVertex2f(5.0,-3.0)
    glEnd()

    #ojo izquierdo
    glBegin(GL_LINE_LOOP)
    glVertex2f(-4.0,0.0)    
    glVertex2f(-5.0,0.0)  
    glVertex2f(-4.0,-1.0)
    glVertex2f(-3.0,-1.0)
    glVertex2f(-2.0,-1.0)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(-4.0,-1.0)
    glVertex2f(-4.0,0.0)
    glVertex2f(-3.0,-1.0)
    glEnd()
    #ojo derecho
    glBegin(GL_LINE_LOOP)
    glVertex2f(4.0,0.0)    
    glVertex2f(5.0,0.0)  
    glVertex2f(4.0,-1.0)
    glVertex2f(3.0,-1.0)
    glVertex2f(2.0,-1.0)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(4.0,-1.0)
    glVertex2f(4.0,0.0)
    glVertex2f(3.0,-1.0)
    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"dibujan un lobo en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutMainLoop()

if __name__ == "__main__":
    main()
