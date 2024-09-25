from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from ui.todo_app import Ui_MainWindow

class Vista(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._boton_agregar = self.pushButton
        self._boton_completar = self.pushButton_2
        self._boton_eliminar = self.pushButton_3


    def conectar_boton_agregar(self, handler):

        self._boton_agregar.clicked.connect(handler)

    def conectar_boton_completar(self, handler):

        self._boton_completar.clicked.connect(handler)

    def conectar_boton_eliminar(self, handler):

        self._boton_eliminar.clicked.connect(handler)

    # Métodos para interactuar con la interfaz
    def obtener_texto_tarea(self):

        return self.lineEdit.text()

    def agregar_tarea_lista(self, tarea):

        self.listWidget.addItem(tarea)

    def obtener_tareas_seleccionadas(self):

        tareas_seleccionadas = []
        for item in self.listWidget.selectedItems():
            tareas_seleccionadas.append(item.text())
        return tareas_seleccionadas

    def eliminar_tarea_lista(self, tarea):

        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            if item.text() == tarea:
                self.listWidget.takeItem(index)
                break

    def marcar_completada_en_lista(self, tarea):

        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            if item.text() == tarea:
                item.setText(f"{tarea} (Completada)")
                item.setForeground(Qt.gray)
                break

