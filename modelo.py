class ModeloTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, tarea):

        self.__tareas.append({'tarea': tarea, 'completada': False})

    def eliminar_tarea(self, tarea, donde=None):

        self.__tareas = [t for t in self.__tareas if t['tarea'] != tarea]

    def marcar_completada(self, tarea):

        for t in self.__tareas:
            if t['tarea'] == tarea:
                t['completada'] = True

    def obtener_tareas(self):

        return self.__tareas
