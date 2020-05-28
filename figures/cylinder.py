import numpy as np

from figure import Figure

from OpenGL.GL import glVertex3f, glColor3f, glBegin, glEnd, GL_POLYGON, GL_QUAD_STRIP, GL_TRIANGLE_STRIP


class Cylinder(Figure):

    def __init__(self, name, x, y, z, height, isFlipped, color, mode):
        Figure.__init__(self, name, x, y, z, isFlipped, color, mode)
        self.height = int(height)

    def draw(self):
        radius = 1

        if isinstance(self.color, list):
            glColor3f(*self.color[1])
        else:
            glColor3f(*self.color)

        if self.visual_mode == GL_TRIANGLE_STRIP:
            glBegin(GL_POLYGON)
        else:
            glBegin(self.visual_mode)
        angle = 0
        while angle < 2 * np.pi:
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            if self.isFlipped:
                glVertex3f(-self.height / 2 + self.z, x + self.x, y + self.y)
            else:
                glVertex3f(x + self.x, -self.height / 2 + self.z, y + self.y)
            angle += .1
        glEnd()

        if isinstance(self.color, list):
            glColor3f(*self.color[0])
        else:
            glColor3f(*self.color)

        if self.visual_mode == GL_TRIANGLE_STRIP:
            glBegin(GL_QUAD_STRIP)
        else:
            glBegin(self.visual_mode)

        angle = 0
        while angle < 2 * np.pi:
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            if self.isFlipped:
                glVertex3f(self.height / 2 + self.z, x + self.x, y + self.y)
                glVertex3f(-self.height / 2 + self.z, x + self.x, y + self.y)
            else:
                glVertex3f(x + self.x, self.height / 2 + self.z, y + self.y)
                glVertex3f(x + self.x, -self.height / 2 + self.z,  y + self.y)
            angle += .1

        if self.isFlipped:
            glVertex3f(self.height / 2 + self.z, x + self.x, y + self.y)
            glVertex3f(-self.height / 2 + self.z, x + self.x, y + self.y)
        else:
            glVertex3f(x + self.x, self.height / 2 + self.z, y + self.y)
            glVertex3f(x + self.x, -self.height / 2 + self.z,  y + self.y)
        glEnd()

        if isinstance(self.color, list):
            glColor3f(*self.color[1])
        else:
            glColor3f(*self.color)

        if self.visual_mode == GL_TRIANGLE_STRIP:
            glBegin(GL_POLYGON)
        else:
            glBegin(self.visual_mode)
        angle = 0
        while angle < 2 * np.pi:
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            if self.isFlipped:
                glVertex3f(self.height / 2 + self.z, x + self.x, y + self.y)
            else:
                glVertex3f(x + self.x, self.height / 2 + self.z,  y + self.y)
            angle += .1
        glEnd()
