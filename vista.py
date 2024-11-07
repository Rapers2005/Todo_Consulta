

from PySide6.QtWidgets import QWidget
from todo_app import Ui_TODO

class VistaTODO(QWidget):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_TODO()
        self.__ui.setupUi(self)
        self.__configurar_interfaz()

    def __configurar_interfaz(self):
        self.__ui.lineEdit.setPlaceholderText("Escribe una tarea...")

    def obtener_line_edit(self):
        return self.__ui.lineEdit

    def obtener_lista_tareas(self):
        return self.__ui.listWidget
