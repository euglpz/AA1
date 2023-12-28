## Predicción de lluvia en Australia
### Instrucciones para correr el proyecto:
* Descargar el proyecto desde <> Code -> Download ZIP
* Extraerlo en su PC (la carpeta se llamará AA1-main por default)
* Abrir VS Code -> File -> Open Folder... (AA1-main)
* Abrimos una nueva terminal
* Creamos un venv: python -m venv venv
* Lo activamos: .\venv\Scripts\activate
* Y dentro de él instalamos los requerimientos: pip install -r .\requirements.txt
* Nos movemos a la carpeta src: cd src
* Corremos python: python

El archivo _AA1_TP_Lopez_Pistelli_ contiene el proyecto completo, está en formato .ipynb, por lo tanto se puede ir corriendo celda a celda.
---
Para correr la app de streamlit:

* En el archivo _app.py_ asegurarse de cambiar las rutas de los archivos .joblib a la ruta donde tengan la carpeta del proyecto.
* En la terminal correr: python -m streamlit run ruta_de_la_carpeta\AA1-main\app.py

  Se abrirá la app localmente en su navegador, podrá elegir los valores que guste de los atributos y observar las predicciones.
