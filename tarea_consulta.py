from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.Paciente = QtWidgets.QTabWidget(self.widget)
        self.Paciente.setGeometry(QtCore.QRect(10, 40, 561, 281))
        self.Paciente.setObjectName("Paciente")


        self.widget1 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.widget1.setFont(font)
        self.widget1.setObjectName("widget1")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 20, 171, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("Hospital Provincial")
        self.comboBox_2.addItem("Hospital Centenario")
        self.comboBox_2.addItem("Heca")

        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setGeometry(QtCore.QRect(360, 100, 88, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Continuar")
        self.Paciente.addTab(self.widget1, "Efector")


        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(0, 20, 221, 25))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("Nombre y Apellido")
        self.comboBox_4.addItem("Matrícula")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(310, 20, 113, 25))
        self.lineEdit.setPlaceholderText("Ingrese su nombre completo aquí")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 100, 88, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Continuar")
        self.Paciente.addTab(self.tab_4, "Médico Solicitante")


        self.widget2 = QtWidgets.QWidget()
        self.widget2.setObjectName("widget2")
        self.comboBox = QtWidgets.QComboBox(self.widget2)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 141, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("Paciente Nuevo")
        self.comboBox.addItem("Paciente en Tratamiento")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 90, 88, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Continuar")
        self.Paciente.addTab(self.widget2, "Paciente")


        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 20, 211, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("Primera vez")
        self.comboBox_3.addItem("Renovación de tratamiento")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 90, 88, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("Continuar")
        self.Paciente.addTab(self.tab_3, "Solicitud")




        self.widget3 = QtWidgets.QWidget()
        self.widget3.setObjectName("widget3")



        self.label = QtWidgets.QLabel(self.widget3)
        self.label.setGeometry(QtCore.QRect(20, 30, 66, 17))
        self.label.setObjectName("label")
        self.label.setText("Droga")


        self.comboBox_6 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_6.setGeometry(QtCore.QRect(110, 20, 211, 25))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("Paracetamol")
        self.comboBox_6.addItem("Ibuprofeno")
        self.comboBox_6.addItem("Enalapril")
        self.comboBox_6.addItem("Calcio")


        self.label_2 = QtWidgets.QLabel(self.widget3)
        self.label_2.setGeometry(QtCore.QRect(5, 80, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Presentación")


        self.comboBox_5 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_5.setGeometry(QtCore.QRect(110, 70, 121, 25))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("Comprimidos")
        self.comboBox_5.addItem("Ampollas")
        self.comboBox_5.addItem("Capsulas")


        self.label_3 = QtWidgets.QLabel(self.widget3)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 66, 17))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Dosis")


        self.comboBox_7 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_7.setGeometry(QtCore.QRect(110, 120, 86, 25))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("1gr")
        self.comboBox_7.addItem("500ml")
        self.comboBox_7.addItem("25ml")
        self.comboBox_7.addItem(".50gr")


        self.label_4 = QtWidgets.QLabel(self.widget3)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 161, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Tiempo de Tratamiento")


        self.comboBox_8 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_8.setGeometry(QtCore.QRect(210, 170, 86, 25))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("1 mes")
        self.comboBox_8.addItem("2 meses")
        self.comboBox_8.addItem("3 meses")
        self.comboBox_8.addItem("4 meses")


        self.pushButton_5 = QtWidgets.QPushButton(self.widget3)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 200, 88, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText("Continuar")

        self.Paciente.addTab(self.widget3, "Tratamiento")



        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")


        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 20, 141, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setText("Adjuntar Archivo")


        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 210, 88, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText("Continuar")


        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setGeometry(QtCore.QRect(240, 160, 88, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setText("Guardar")


        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 60, 281, 70))
        self.textEdit_2.setObjectName("textEdit_2")


        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 111, 20))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Observaciones")

        self.Paciente.addTab(self.tab, "Resumen Historia Clinica")


        self.widget4 = QtWidgets.QWidget()
        self.widget4.setObjectName("widget4")


        self.pushButton_8 = QtWidgets.QPushButton(self.widget4)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 20, 141, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setText("Adjuntar Archivo")


        self.label_6 = QtWidgets.QLabel(self.widget4)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 111, 17))
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Observaciones")


        self.textEdit_3 = QtWidgets.QTextEdit(self.widget4)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 80, 250, 70))  # Ajusta el tamaño y la posición según sea necesario
        self.textEdit_3.setObjectName("textEdit_3")

        self.pushButton_9 = QtWidgets.QPushButton(self.widget4)
        self.pushButton_9.setGeometry(QtCore.QRect(410, 210, 88, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setText("Continuar")


        self.pushButton_12 = QtWidgets.QPushButton(self.widget4)
        self.pushButton_12.setGeometry(QtCore.QRect(260, 150, 88, 25))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setText("Guardar")

        self.Paciente.addTab(self.widget4, "Laboratorio")


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")


        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(30, 10, 411, 70))

        self.textEdit.setObjectName("textEdit")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(360, 190, 171, 25))

        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setText("Solicitar y Terminar")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(67, 100, 141, 25))

        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setText("Guardar comentario")


        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setGeometry(QtCore.QRect(17, 190, 201, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setText("Eliminar consulta y pedido")

        self.pushButton_14.clicked.connect(self.eliminar_consulta_y_volver)
        self.Paciente.addTab(self.tab_2, "Justificación de Pedido")

        MainWindow.setCentralWidget(self.widget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.Paciente.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(self.go_to_next_tab)
        self.pushButton_2.clicked.connect(self.go_to_next_tab)
        self.pushButton_3.clicked.connect(self.go_to_next_tab)
        self.pushButton_4.clicked.connect(self.go_to_next_tab)
        self.pushButton_5.clicked.connect(self.go_to_next_tab)
        self.pushButton_7.clicked.connect(self.go_to_next_tab)
        self.pushButton_9.clicked.connect(self.go_to_next_tab)


        self.pushButton_10.clicked.connect(self.solicitar_y_terminar)


        self.comboBox_4.currentIndexChanged.connect(self.update_placeholder)


        self.pushButton_6.clicked.connect(self.abrir_dialogo_archivo)
        self.pushButton_8.clicked.connect(self.abrir_dialogo_archivo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestión de Pacientes"))

    def go_to_next_tab(self):

        current_index = self.Paciente.currentIndex()
        next_index = current_index + 1

        if next_index < self.Paciente.count():
            self.Paciente.setCurrentIndex(next_index)
        else:
            print("Ya estás en la última pestaña")

    def solicitar_y_terminar(self):



        if (self.comboBox_2.currentText() == "" or
            self.comboBox_6.currentText() == "" or
            self.comboBox_5.currentText() == "" or
            self.comboBox_7.currentText() == "" or
            self.comboBox_8.currentText() == "" or
            self.comboBox_4.currentText() == ""):

            QtWidgets.QMessageBox.warning(None, "Error", "Debe completar todos los campos antes de continuar.")
            return

            # Proceder con la solicitud si todo está completo
        QtWidgets.QMessageBox.information(None, "Éxito", "¡Solicitud completada con éxito!")



    def validar_campos(self):

        if not self.lineEdit.text():
            QMessageBox.warning(None, "Error", "Por favor, ingrese el nombre y apellido o número de matrícula.")
            return False

        return True

    def update_placeholder(self):

        seleccion = self.comboBox_4.currentText()
        if seleccion == "Nombre y Apellido":
            self.lineEdit.setPlaceholderText("Ingrese su nombre completo aquí")
        elif seleccion == "Matrícula":
            self.lineEdit.setPlaceholderText("Ingrese su número de matrícula aquí")

    def abrir_dialogo_archivo(self):
        """Abre un diálogo para seleccionar un archivo"""
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(None, "Adjuntar archivo", "", "Todos los archivos (*)",
                                                 options=opciones)
        if archivo:
            print(f"Archivo seleccionado: {archivo}")
            # Aquí podrías actualizar un label o almacenar la ruta del archivo

    def eliminar_consulta_y_volver(self):
        """Borra todos los campos de las pestañas y vuelve a la primera pestaña."""


        self.textEdit.clear()
        self.textEdit_3.clear()

        self.Paciente.setCurrentIndex(0)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
