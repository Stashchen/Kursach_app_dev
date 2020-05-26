from PyQt5.QtWidgets import QOpenGLWidget

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutSolidCube


# Функция в дальнейшем используется для получения точек
def custom_map(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2


class CustomGL(QOpenGLWidget):
    """ Основной класс, переписывающий виджет OpenGL и добавляющий рисование определённых фигур """

    def __init__(self, parent):
        super().__init__(parent=parent)

    def initializeGL(self):
        self.widget_width = self.frameGeometry().width()
        self.widget_height = self.frameGeometry().height()

        self.x_axis_rotation = 0  # Переменная для вращения по оси x
        self.y_axis_rotation = 0  # Переменная для вращения по оси y

        self.sectors = 20  # Стандартное кол-во секторов полусферы 

        self.visual_mode = GL_TRIANGLE_STRIP  # Стиль отображения фигуры
        self.current_figure = self.draw_dome

        glClearColor(0, 0, 0, 1) # Цвет фона

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT) # Отчищает окно

        glMatrixMode(GL_MODELVIEW) # Ставит вид отображения
        glLoadIdentity() # Подгружает объект

        glRotatef(self.y_axis_rotation, 0, 1, 0) # Вращение по y
        glRotatef(self.x_axis_rotation, 1, 0, 0) # Вращение по x

        if self.current_figure == CustomGL.draw_dome:
            self.current_figure(self.sectors, self.visual_mode)
        else:
            self.current_figure(self.visual_mode)

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION) # Включает режим рисования по проекциям xyz
        glLoadIdentity()
        glOrtho(-2.0, 2.0, -2.0, 2.0, -3.0, 3.0) # Задаёт проекции
        glViewport(0, 0, w, h)

    def mousePressEvent(self, event):
        self.pressed_event = event.pos() # Получаем позицию курсора при нажатии

    def mouseMoveEvent(self, event):
        # Реализация вращения при движении мыши
        self.x_axis_rotation += (360 * (float(event.y()) - float(self.pressed_event.y())) / self.widget_height)
        self.y_axis_rotation += (360 * (float(event.x()) - float(self.pressed_event.x())) / self.widget_width)

        self.pressed_event = event.pos()
        self.update() # Обновялет экран

    @staticmethod
    def draw_dome(a, mode):
        # Отрисовка полусферы. a - секторы
        globe = [] # Хранит массивы с точками

        for i in range(a + 1):
            lat = custom_map(i, 0, a, 0, np.pi)  # Задание широты
            globe.append([])
            for j in range(a + 1):
                lon = custom_map(j, 0, a, 0, np.pi)  # Задание долготы
                x = np.sin(lon) * np.cos(lat)
                y = np.sin(lon) * np.sin(lat)
                z = np.cos(lon)

                globe[i].append((x, y, z))

        for i in range(a):
            glBegin(mode)  # Начало рисования. mode - стиль отрисовки
            glColor3f(0, 1, 1) # Задание цвета
            for j in range(a + 1):
                x, y, z = globe[i][j]
                if j % 2 == 0:
                    glColor3f(1, 0, 1)
                else:
                    glColor3f(0, 1, 1)

                glVertex3f(x, y, z) # Размещение точек
                x, y, z = globe[i + 1][j]

                glVertex3f(x, y, z)

            glEnd() # Окончание рисования

    @staticmethod
    def draw_piramid(mode):
        # Метод для отрисовки пирамиды. Задаёт точки и соединяет их. Сколько точек соединится зависит от mode
        glBegin(mode)
        glColor3f(1, 0, 0)

        glVertex3f(-.5, -.5, -.5)
        glVertex3f(-.5, -.5, .5)
        glVertex3f(0, .5, 0)

        glVertex3f(0, .5, 0)
        glVertex3f(.5, -.5, -.5)
        glVertex3f(-.5, -.5, -.5)
        glVertex3f(0, .5, 0)

        glVertex3f(0, .5, 0)
        glVertex3f(.5, -.5, .5)
        glVertex3f(.5, -.5, -.5)
        glVertex3f(0, .5, 0)

        glVertex3f(0, .5, 0)
        glVertex3f(.5, -.5, .5)
        glVertex3f(-.5, -.5, .5)

        glVertex3f(-.5, -.5, .5)
        glVertex3f(-.5, -.5, -.5)
        glVertex3f(.5, -.5, -.5)
        glVertex3f(.5, -.5, .5)

        glEnd()



