import sys

import save_funcs as sf

from PyQt5.QtWidgets import QMainWindow, QApplication
from forms.design import Ui_MainWindow
from OpenGL.GL import GL_POINTS, GL_LINE_STRIP, GL_TRIANGLE_STRIP
from custom_gl import CustomGL

import threading


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.geometry().x, self.geometry().y = 0, 0 # Задаёт размещение окна

        self.openGLWidget.initializeGL() # Первичная инициализация окна
        self.openGLWidget.paintGL() # Рисование объекта

        self.visual_btns = [self.dots_btn, self.lines_btn, self.solid_btn]
        self.figures_btns = [self.dome_btn, self.piramid_btn]

        # Следующие методы соединяют виджеты с определёнными действиями
        self.lines_btn.clicked.connect(self.change_lines)
        self.dots_btn.clicked.connect(self.change_dots)
        self.solid_btn.clicked.connect(self.change_solid)

        self.sectors_edit.editingFinished.connect(self.set_sectors)

        self.dome_btn.clicked.connect(self.set_dome)
        self.piramid_btn.clicked.connect(self.set_piramid)

        self.actionExcel.triggered.connect(lambda: self.save_file(sf.save_exel))
        self.actionWord.triggered.connect(lambda: self.save_file(sf.save_word))
        #
        # self.actionHelp.triggered.connect()
        self.actionExit.triggered.connect(sys.exit)

    def moveEvent(self, event):
        # Нужно для сохранения фотографии объекта
        self.geometry = event.pos()

    def set_sectors(self):
        if self.openGLWidget.current_figure == CustomGL.draw_dome:
            try:
                self.openGLWidget.sectors = int(self.sectors_edit.text())
                self.update()
            except ValueError:
                self.error_label.setText('Error: Enter Int')
                self.sectors_edit.setText('')
        else:
            self.error_label.setText('Error: No sectors for piramid. Leave it clear')

    def change_lines(self):
        for btn in self.visual_btns:
            btn.setEnabled(True)

        self.lines_btn.setEnabled(False)
        self.openGLWidget.visual_mode = GL_LINE_STRIP
        self.update()

    def change_dots(self):
        for btn in self.visual_btns:
            btn.setEnabled(True)

        self.dots_btn.setEnabled(False)
        self.openGLWidget.visual_mode = GL_POINTS
        self.update()

    def change_solid(self):
        for btn in self.visual_btns:
            btn.setEnabled(True)

        self.solid_btn.setEnabled(False)

        self.openGLWidget.visual_mode = GL_TRIANGLE_STRIP

        self.update()

    def set_dome(self):
        self.openGLWidget.current_figure = CustomGL.draw_dome
        for btn in self.figures_btns:
            btn.setEnabled(True)
        self.dome_btn.setEnabled(False)
        self.update()

    def set_piramid(self):
        self.openGLWidget.current_figure = CustomGL.draw_piramid
        for btn in self.figures_btns:
            btn.setEnabled(True)
        self.piramid_btn.setEnabled(False)
        self.update()

    def save_file(self, func):
        self.get_screenshot()
        t = threading.Thread(target=func)
        t.start()

    def get_screenshot(self):
        # Создаёт фото объекта
        from pyautogui import screenshot
        m_x, m_y = self.geometry.x() + 50, self.geometry.y() + 50
        f_x, f_y = self.openGLWidget.x(), self.openGLWidget.y()
        f_width, f_height = self.openGLWidget.width(), self.openGLWidget.height()

        screenshot('images/photo.png', region=(m_x + f_x, m_y + f_y, f_width - 100, f_height - 50))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    app.exec_()
