from PyQt5.QtWidgets import QOpenGLWidget

from OpenGL.GL import *


class CustomGL(QOpenGLWidget):
    """ Основной класс, переписывающий виджет OpenGL и добавляющий рисование определённых фигур """

    def __init__(self, parent):
        super().__init__(parent=parent)

    def initializeGL(self):
        self.widget_width = self.frameGeometry().width()
        self.widget_height = self.frameGeometry().height()

        self.x_axis_rotation = 0  # Переменная для вращения по оси x
        self.y_axis_rotation = 0  # Переменная для вращения по оси y

        self.figures = []  # Все фигуры

        glClearColor(0, 0, 0, 1) # Цвет фона

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Отчищает окно

        glMatrixMode(GL_MODELVIEW) # Ставит вид отображения
        glLoadIdentity() # Подгружает объект

        glRotatef(self.y_axis_rotation, 0, 1, 0) # Вращение по y
        glRotatef(self.x_axis_rotation, 1, 0, 0) # Вращение по x

        for figure in self.figures:
            figure.draw()

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION) # Включает режим рисования по проекциям xyz
        glLoadIdentity()
        glOrtho(-5.0, 5.0, -5.0, 5.0, -5.0, 5.0) # Задаёт проекции
        glViewport(0, 0, w, h)

    def mousePressEvent(self, event):
        self.pressed_event = event.pos() # Получаем позицию курсора при нажатии

    def mouseMoveEvent(self, event):
        # Реализация вращения при движении мыши
        self.x_axis_rotation += (180 * (float(event.y()) - float(self.pressed_event.y())) / self.widget_height)
        self.y_axis_rotation += (180 * (float(event.x()) - float(self.pressed_event.x())) / self.widget_width)

        self.pressed_event = event.pos()
        self.update() # Обновялет экран

    def draw(self):
        for figure in self.figures:
            figure.draw()

    def delete_item(self, index):
        del self.figures[index]



