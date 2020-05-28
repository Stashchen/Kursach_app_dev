import sys
import subprocess

import save_funcs as sf

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from forms.design import Ui_MainWindow
from figures.dome import Dome
from figures.sphere import Sphere
from figures.cylinder import Cylinder

from OpenGL.GL import GL_TRIANGLE_STRIP, GL_LINE_STRIP, GL_POINTS

import threading


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.geometry().x, self.geometry().y = 0, 0  # Задаёт размещение окна

        self.openGLWidget.initializeGL()  # Первичная инициализация окна

        self.binding_starting_widgets()

        self.colors = {
            'Blue-Purple': [(0, 1, 1), (1, 0, 1)],
            'Pink-Yellow': [(1, 0, 1), (1, 1, 0)],
            'Red': (1, 0, 0),
            'Green': (0, 1, 0),
            'Blue': (0, 0, 1),
            'Yellow': (1, 1, 0)
        }

    def binding_starting_widgets(self):
        """ Метод в котором происходит назначение разных виджетов и действий """
        self.dome_btn.clicked.connect(self.show_new_dome_properties)
        self.cylinder_btn.clicked.connect(self.show_new_cylinder_properties)
        self.sphere_btn.clicked.connect(self.show_new_sphere_properties)

        self.listWidget.itemClicked.connect(self.show_selected_item_properties)

        self.actionExcel.triggered.connect(lambda: self.save_file(sf.save_exel))
        self.actionWord.triggered.connect(lambda: self.save_file(sf.save_word))

        self.actionHelp.triggered.connect(self.open_help)
        self.actionExit.triggered.connect(sys.exit)

    def moveEvent(self, event):
        """ Нужно для сохранения фотографии объекта """
        self.geometry = event.pos()

    def show_properties(self):
        """ Динамическое создание виджетов """
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(800, 340, 371, 391))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 351, 120))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.x_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.x_label.setObjectName("x_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.x_label)
        self.x_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.x_edit.setObjectName("x_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.x_edit)
        self.y_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.y_label.setAlignment(QtCore.Qt.AlignCenter)
        self.y_label.setObjectName("y_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.y_label)
        self.y_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.y_edit.setObjectName("y_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.y_edit)
        self.z_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.z_label.setAlignment(QtCore.Qt.AlignCenter)
        self.z_label.setObjectName("z_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.z_label)
        self.z_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.z_edit.setObjectName("z_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.z_edit)
        self.flip_cb = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.flip_cb.setObjectName("flip_cb")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.flip_cb)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.name_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_edit.setObjectName("name_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_edit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 351, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sectors_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.sectors_label.setObjectName("sectors_label")
        self.horizontalLayout.addWidget(self.sectors_label)
        self.sectors_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.sectors_edit.setObjectName("sectors_edit")
        self.horizontalLayout.addWidget(self.sectors_edit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 210, 351, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.color_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.color_label.setFont(font)
        self.color_label.setObjectName("color_label")
        self.horizontalLayout_2.addWidget(self.color_label)
        self.colors_combo = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.colors_combo.setObjectName("colors_combo")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/icons/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colors_combo.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/icons/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colors_combo.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/icons/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colors_combo.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/icons/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colors_combo.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./images/icons/4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colors_combo.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./images/icons/6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colors_combo.addItem(icon5, "")
        self.horizontalLayout_2.addWidget(self.colors_combo)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 250, 351, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.solid_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.solid_rb.setChecked(True)
        self.solid_rb.setObjectName("solid_rb")
        self.verticalLayout.addWidget(self.solid_rb)
        self.lined_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.lined_rb.setObjectName("lined_rb")
        self.verticalLayout.addWidget(self.lined_rb)
        self.dotted_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.dotted_rb.setObjectName("dotted_rb")
        self.verticalLayout.addWidget(self.dotted_rb)
        self.confirm_btn = QtWidgets.QPushButton(self.groupBox)
        self.confirm_btn.setGeometry(QtCore.QRect(210, 340, 155, 41))
        self.confirm_btn.setObjectName("confirm_btn")
        self.delete_btn = QtWidgets.QPushButton(self.groupBox)
        self.delete_btn.setGeometry(QtCore.QRect(10, 340, 91, 41))
        self.delete_btn.setObjectName("delete_btn")
        self.change_btn = QtWidgets.QPushButton(self.groupBox)
        self.change_btn.setGeometry(QtCore.QRect(110, 340, 91, 41))
        self.change_btn.setObjectName("change_btn")

        # Вставка текста в виджеты
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Figure Properties"))
        self.x_label.setText(_translate("MainWindow", "X"))
        self.x_edit.setText(_translate("MainWindow", "0"))
        self.y_label.setText(_translate("MainWindow", "Y"))
        self.y_edit.setText(_translate("MainWindow", "0"))
        self.z_label.setText(_translate("MainWindow", "Z"))
        self.z_edit.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.sectors_label.setText(_translate("MainWindow", "Sectors:"))
        self.sectors_edit.setText(_translate("MainWindow", "20"))
        self.flip_cb.setText(_translate("MainWindow", "Flip"))
        self.color_label.setText(_translate("MainWindow", "Color"))
        self.colors_combo.setItemText(0, _translate("MainWindow", "Blue-Purple"))
        self.colors_combo.setItemText(1, _translate("MainWindow", "Pink-Yellow"))
        self.colors_combo.setItemText(2, _translate("MainWindow", "Red"))
        self.colors_combo.setItemText(3, _translate("MainWindow", "Green"))
        self.colors_combo.setItemText(4, _translate("MainWindow", "Blue"))
        self.colors_combo.setItemText(5, _translate("MainWindow", "Yellow"))
        self.solid_rb.setText(_translate("MainWindow", "solid"))
        self.lined_rb.setText(_translate("MainWindow", "lined"))
        self.dotted_rb.setText(_translate("MainWindow", "dotted"))
        self.confirm_btn.setText(_translate("MainWindow", "Confirm"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.change_btn.setText(_translate("MainWindow", "Change"))

    def show_new_dome_properties(self):
        """ Отображает свойства при создании полусферы. """
        self.show_properties()
        self.dome_btn.setEnabled(False)
        self.cylinder_btn.setEnabled(False)
        self.sphere_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        self.change_btn.setEnabled(False)

        self.name_edit.setText('Dome')

        self.confirm_btn.clicked.connect(self.add_new_dome)

        self.groupBox.show()

    def show_new_sphere_properties(self):
        """ Отображает свойства при создании сферы. """
        self.show_properties()
        self.flip_cb.setEnabled(False)
        self.dome_btn.setEnabled(False)
        self.cylinder_btn.setEnabled(False)
        self.sphere_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        self.change_btn.setEnabled(False)

        self.name_edit.setText('Sphere')

        self.confirm_btn.clicked.connect(self.add_new_sphere)

        self.groupBox.show()

    def show_new_cylinder_properties(self):
        """ Отображает свойства при создании целиндра. """
        self.show_properties()
        self.dome_btn.setEnabled(False)
        self.cylinder_btn.setEnabled(False)
        self.sphere_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        self.change_btn.setEnabled(False)

        self.name_edit.setText('Cylinder')
        self.sectors_label.setText('Height: ')
        self.sectors_edit.setText('2')
        self.confirm_btn.clicked.connect(self.add_new_cylinder)

        self.groupBox.show()

    def show_selected_item_properties(self):
        """ Срабатывает при выборе ранее созданной фигуры"""
        try:
            # Отключение лишних сигналов от кнопки
            self.delete_btn.clicked.disconnect()
            self.change_btn.clicked.disconnect()
        except TypeError:
            pass

        self.groupBox.close()
        index = self.listWidget.currentRow()
        current_figure = self.openGLWidget.figures[index]

        self.set_form_properties(current_figure)
        self.groupBox.show()
        self.confirm_btn.setEnabled(False)
        self.change_btn.setEnabled(True)
        self.delete_btn.setEnabled(True)

        self.change_btn.clicked.connect(lambda: self.change_item_properties(index))
        self.delete_btn.clicked.connect(lambda: self.delete_figure(index))

    def delete_figure(self, index):
        self.openGLWidget.delete_item(index)
        self.listWidget.takeItem(index)
        self.groupBox.close()

    def set_form_properties(self, item):
        """ Заполнение полей свойств ранее выбранной фигуры. """
        self.name_edit.setText(item.name)
        self.x_edit.setText(str(item.x))
        self.y_edit.setText(str(item.y))
        self.z_edit.setText(str(item.z))

        try:
            self.sectors_edit.setText(str(item.sectors))
        except AttributeError:
            self.sectors_edit.setText(str(item.height))

        if item.isFlipped:
            self.flip_cb.setChecked(True)
        else:
            self.flip_cb.setChecked(False)

        for index, color in enumerate(self.colors.items()):
            if item.color == color[1]:
                break

        self.colors_combo.setCurrentIndex(index)

        if item.visual_mode == GL_TRIANGLE_STRIP:
            self.solid_rb.setChecked(True)
        elif item.visual_mode == GL_LINE_STRIP:
            self.lined_rb.setChecked(True)
        else:
            self.dotted_rb.setChecked(True)

    def change_item_properties(self, index):
        """ Изменение данных фигуры """
        item = self.openGLWidget.figures[index]
        if self.solid_rb.isChecked():
            visual_mode = GL_TRIANGLE_STRIP
        elif self.lined_rb.isChecked():
            visual_mode = GL_LINE_STRIP
        else:
            visual_mode = GL_POINTS

        if self.flip_cb.isChecked():
            isFlipped = True
        else:
            isFlipped = False

        color = self.colors[self.colors_combo.currentText()]

        self.listWidget.currentItem().setText(self.name_edit.text())

        item.name = self.name_edit.text()
        item.x = float(self.x_edit.text())
        item.y = float(self.y_edit.text())
        item.z = float(self.z_edit.text())
        if self.sectors_label.text() == 'Height: ':
            item.height = int(self.sectors_edit.text())
        else:
            item.sectors = int(self.sectors_edit.text())

        item.isFlipped = isFlipped
        item.color = color
        item.visual_mode = visual_mode
        self.change_btn.setEnabled(True)
        self.delete_btn.setEnabled(True)

        self.groupBox.close()
        self.openGLWidget.draw()

        self.cylinder_btn.setEnabled(True)
        self.dome_btn.setEnabled(True)

        self.groupBox.close()

    def add_new_dome(self):
        """ Создание полусферы """
        if self.solid_rb.isChecked():
            visual_mode = GL_TRIANGLE_STRIP
        elif self.lined_rb.isChecked():
            visual_mode = GL_LINE_STRIP
        else:
            visual_mode = GL_POINTS

        if self.flip_cb.isChecked():
            isFlipped = True
        else:
            isFlipped = False

        color = self.colors[self.colors_combo.currentText()]

        new_dome = Dome(self.name_edit.text(),
                        self.x_edit.text(),
                        self.y_edit.text(),
                        self.z_edit.text(),
                        self.sectors_edit.text(),
                        isFlipped,
                        color,
                        visual_mode)

        self.openGLWidget.figures.append(new_dome)
        self.listWidget.addItem(QListWidgetItem(str(new_dome)))
        self.groupBox.close()
        self.openGLWidget.draw()

        self.sphere_btn.setEnabled(True)
        self.cylinder_btn.setEnabled(True)
        self.dome_btn.setEnabled(True)

    def add_new_sphere(self):
        """ Создание сферы. """
        if self.solid_rb.isChecked():
            visual_mode = GL_TRIANGLE_STRIP
        elif self.lined_rb.isChecked():
            visual_mode = GL_LINE_STRIP
        else:
            visual_mode = GL_POINTS

        color = self.colors[self.colors_combo.currentText()]

        new_sphere = Sphere(self.name_edit.text(),
                            self.x_edit.text(),
                            self.y_edit.text(),
                            self.z_edit.text(),
                            self.sectors_edit.text(),
                            color,
                            visual_mode)

        self.openGLWidget.figures.append(new_sphere)
        self.listWidget.addItem(QListWidgetItem(str(new_sphere)))
        self.groupBox.close()
        self.openGLWidget.draw()

        self.sphere_btn.setEnabled(True)
        self.cylinder_btn.setEnabled(True)
        self.dome_btn.setEnabled(True)

    def add_new_cylinder(self):
        """ Создание цилиндра """
        if self.solid_rb.isChecked():
            visual_mode = GL_TRIANGLE_STRIP
        elif self.lined_rb.isChecked():
            visual_mode = GL_LINE_STRIP
        else:
            visual_mode = GL_POINTS

        color = self.colors[self.colors_combo.currentText()]

        if self.flip_cb.isChecked():
            isFlipped = True
        else:
            isFlipped = False

        new_cylinder = Cylinder(self.name_edit.text(),
                                self.x_edit.text(),
                                self.y_edit.text(),
                                self.z_edit.text(),
                                self.sectors_edit.text(),
                                isFlipped,
                                color,
                                visual_mode)

        self.openGLWidget.figures.append(new_cylinder)
        self.listWidget.addItem(QListWidgetItem(str(new_cylinder)))
        self.groupBox.close()
        self.openGLWidget.draw()

        self.sphere_btn.setEnabled(True)
        self.cylinder_btn.setEnabled(True)
        self.dome_btn.setEnabled(True)

    def save_file(self, func):
        """ Сохранение данных в файл"""
        self.get_screenshot()
        t = threading.Thread(target=func)
        t.start()

    def open_help(self):
        subprocess.run('xchm help/Help.chm', shell=True)

    def get_screenshot(self):
        # Создаёт фото объекта
        from pyautogui import screenshot
        m_x, m_y = self.geometry.x() + 50, self.geometry.y() + 50
        f_x, f_y = self.openGLWidget.x(), self.openGLWidget.y()
        f_width, f_height = self.openGLWidget.width(), self.openGLWidget.height()

        screenshot('images/photo.png', region=(m_x + f_x, m_y + f_y, f_width - 100, f_height - 50))


if __name__ == '__main__':
    # Старт приложения
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    app.exec_()
