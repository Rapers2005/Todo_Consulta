

from PySide6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from PySide6.QtCore import Qt
from ui.todo_app import Ui_TODO

class TODOControlador(QMainWindow):
    def __init__(self, modelo):
        super().__init__()
        self.__ui = Ui_TODO()
        self.__ui.setupUi(self)
        self.__modelo = modelo


        self.__ui.pushButton.clicked.connect(self.__agregar_tarea)
        self.__ui.pushButton_2.clicked.connect(self.__marcar_tarea_completada)
        self.__ui.pushButton_3.clicked.connect(self.__eliminar_tarea)

        self.__ui.lineEdit.mouseDoubleClickEvent = self.__limpiar_campo_ingresartarea

    def __limpiar_campo_ingresartarea(self, event):
        self.__ui.lineEdit.clear()

    def __agregar_tarea(self):
        texto_tarea = self.__ui.lineEdit.text()
        if texto_tarea:
            item = QListWidgetItem(texto_tarea)
            item.setCheckState(Qt.Unchecked)
            self.__ui.listWidget.addItem(item)
            self.__ui.lineEdit.clear()
        else:
            self.__mostrar_mensaje("La tarea no puede estar vacía.", "Advertencia")

    def __marcar_tarea_completada(self):
        for index in range(self.__ui.listWidget.count()):
            item = self.__ui.listWidget.item(index)
            if item.checkState() == Qt.Checked:
                if "(Completada)" not in item.text():
                    item.setText(f"{item.text()} (Completada)")
                    item.setCheckState(Qt.Unchecked)

        self.__mostrar_mensaje("¡Tareas completadas!", "Éxito")

    def __eliminar_tarea(self):
        tareas_eliminadas = False

        for index in reversed(range(self.__ui.listWidget.count())):
            item = self.__ui.listWidget.item(index)
            if item.checkState() == Qt.Checked:
                if "(Completada)" in item.text():
                    self.__mostrar_mensaje("La tarea completada no se puede eliminar.", "Advertencia")
                    return
                else:
                    self.__modelo.eliminar_tarea(index)
                    self.__ui.listWidget.takeItem(index)
                    tareas_eliminadas = True

        if tareas_eliminadas:
            self.__mostrar_mensaje("¡Tareas eliminadas!", "Éxito")

    def __mostrar_mensaje(self, mensaje, titulo="Información"):
        QMessageBox.information(self, titulo, mensaje)
