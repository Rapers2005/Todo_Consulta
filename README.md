TODO Application
Una aplicación de gestión de tareas simple y efectiva, desarrollada en Python utilizando PySide6 y organizada en un patrón de diseño Modelo-Vista-Controlador (MVC).

Descripción
La aplicación TODO permite a los usuarios agregar, marcar como completadas y eliminar tareas de una lista de manera sencilla. El objetivo de esta aplicación es facilitar la gestión de tareas diarias, proporcionando una interfaz gráfica intuitiva y fácil de usar.

Características
Añadir Tarea: Agrega nuevas tareas ingresando texto en un campo de entrada.
Marcar como Completada: Marca una o varias tareas como completadas.
Eliminar Tarea: Elimina las tareas seleccionadas de la lista.
Notificaciones: Muestra mensajes de confirmación o advertencia para informar al usuario sobre las acciones realizadas.
Instalación
Sigue estos pasos para instalar y ejecutar la aplicación en tu entorno local:

1. Clona el Repositorio

git clone https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
2. Configura un Entorno Virtual
Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto:


python -m venv my-venv
source my-venv/bin/activate  # En Linux y macOS
my-venv\Scripts\activate      # En Windows
3. Instala las Dependencias

pip install -r requirements.txt
Nota: Asegúrate de que requirements.txt contenga PySide6 u otras dependencias necesarias.
4. Ejecuta la Aplicación

python main.py
Requisitos
Python: Versión 3.7 o superior.
PySide6: Para la creación de la interfaz gráfica.
Instalación Manual de Dependencias
Si requirements.txt no está disponible, puedes instalar PySide6 manualmente:


pip install PySide6

Estructura del Proyecto
El proyecto está organizado de la siguiente manera:



/tp2
│
├── ui/
│   ├── todo_app.ui         # Archivo .ui de la interfaz gráfica
│  
│
├── controlador.py          # Lógica del controlador (maneja eventos y acciones)
├── modelo.py               # Lógica del modelo (gestiona datos de las tareas)
├── vista.py                # Lógica de la vista (configura la interfaz gráfica)
├── main.py                 # Punto de entrada de la aplicación
└── .gitignore              # Archivo para ignorar archivos no deseados

Cómo Funciona
Interfaz Gráfica: La aplicación utiliza PySide6 para crear una ventana gráfica con un campo de entrada de texto, una lista de tareas y botones para gestionar las tareas. Se puede hacer doble click en ingresar tarea para limpiar 
Modelo-Vista-Controlador (MVC):
Modelo: Gestiona las tareas y su estado (completadas o no).
Vista: Se encarga de la visualización de la interfaz gráfica y actualizaciones.
Controlador: Maneja la lógica de la aplicación y las interacciones del usuario.
Notas Adicionales
Archivos de Caché: El directorio __pycache__ y otros archivos generados por Python están incluidos en .gitignore para mantener el repositorio limpio.

