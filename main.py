import sys

from PyQt5.QtWidgets import QApplication

from controlador import ControladorTareas
from modelo import ModeloTareas
from vista import Vista


def main():
    app = QApplication(sys.argv)


    modelo = ModeloTareas()
    vista = Vista()
    controlador = ControladorTareas(modelo, vista)
    vista.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
