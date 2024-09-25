from PyQt5.QtWidgets import QMessageBox

class ControladorTareas:
    def __init__(self, modelo, vista):
        self.__modelo = modelo
        self.__vista = vista

        self.__vista.conectar_boton_agregar(self.agregar_tarea)
        self.__vista.conectar_boton_eliminar(self.eliminar_tareas)
        self.__vista.conectar_boton_completar(self.marcar_completada)

    def agregar_tarea(self):

        texto_tarea = self.__vista.obtener_texto_tarea()
        if texto_tarea:
            self.__modelo.agregar_tarea(texto_tarea)
            self.__vista.agregar_tarea_lista(texto_tarea)
            self.__vista.lineEdit.clear()

    def eliminar_tareas(self):

        tareas_seleccionadas = self.__vista.obtener_tareas_seleccionadas()
        for tarea in tareas_seleccionadas:
            self.__modelo.eliminar_tarea(tarea)
            self.__vista.eliminar_tarea_lista(tarea)
        if tareas_seleccionadas:
            self.mostrar_mensaje("Tarea eliminadas", "Las tareas seleccionadas fueron eliminadas.")

    def marcar_completada(self):

        tareas_seleccionadas = self.__vista.obtener_tareas_seleccionadas()
        for tarea in tareas_seleccionadas:
            self.__modelo.marcar_completada(tarea)
            self.__vista.marcar_completada_en_lista(tarea)
        if tareas_seleccionadas:
            self.mostrar_mensaje("Tarea completas", "Las tareas seleccionadas fueron completadas.")

    def mostrar_mensaje(self, titulo, mensaje):

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensaje)
        msg_box.exec_()
