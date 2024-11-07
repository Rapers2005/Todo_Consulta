

class TODOModelo:
    def __init__(self):
        self.__tareas = []


    def agregar_tarea(self, tarea):
        self.__tareas.append({"tarea": tarea, "completada": False})


    def completar_tarea(self, indice):
        if 0 <= indice < len(self.__tareas):
            self.__tareas[indice]["completada"] = True


    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.__tareas):
            self.__tareas.pop(indice)


    def obtener_tareas(self):
        return self.__tareas.copy()
