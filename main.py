
import sys
from PySide6.QtWidgets import QApplication
from modelo import TODOModelo
from controlador import TODOControlador

if __name__ == "__main__":
    app = QApplication(sys.argv)
    modelo = TODOModelo()
    controlador = TODOControlador(modelo)
    controlador.show()
    sys.exit(app.exec())
