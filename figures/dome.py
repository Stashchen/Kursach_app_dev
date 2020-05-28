import numpy as np

from figure import Figure

from OpenGL.GL import glVertex3f, glColor3f, glBegin, glEnd


class Dome(Figure):

    def __init__(self, name, x, y, z, sectors, isFlipped, color, mode):
        Figure.__init__(self, name, x, y, z, isFlipped, color, mode)
        self.sectors = int(sectors)

    def draw(self):
        # Отрисовка полусферы. a - секторы
        self.vertices = []  # Хранит массивы с точками

        for i in range(self.sectors + 1):
            if self.isFlipped:
                lat = self.custom_map(i, 0, self.sectors, -np.pi, 0)  # Задание широты
            else:
                lat = self.custom_map(i, 0, self.sectors, 0, np.pi)
            self.vertices.append([])
            for j in range(self.sectors + 1):
                lon = self.custom_map(j, 0, self.sectors, 0, np.pi)  # Задание долготы
                x = np.sin(lon) * np.cos(lat)
                y = np.sin(lon) * np.sin(lat)
                z = np.cos(lon)

                self.vertices[i].append((x + self.x, y + self.y, z + self.z))

        for i in range(self.sectors):
            glBegin(self.visual_mode)  # Начало рисования. mode - стиль отрисовки

            for j in range(self.sectors + 1):
                x, y, z = self.vertices[i][j]
                if isinstance(self.color, list):
                    if j % 2 == 0:
                        glColor3f(*self.color[0])
                    else:
                        glColor3f(*self.color[1])
                else:
                    glColor3f(*self.color)

                glVertex3f(x, y, z)  # Размещение точек
                x, y, z = self.vertices[i + 1][j]

                glVertex3f(x, y, z)

            glEnd()  # Окончание рисования
