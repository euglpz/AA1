## Predicción de lluvia en Australia

Este proyecto se basa en la predicción de lluvia en Australia a partir de un conjunto de datos que contiene datos climáticos de los últimos diez años.

Para el desarrollo del proyecto se utilizó la librería scikit-learn para el preprocesamiento de datos, implementación de modelos y evaluación de métricas y TensorFlow para el entrenamiento de redes neuronales.

Se realizaron modelos de clasificación para determinar si lloverá o no al día siguiente y modelos de regresión para determinar la cantidad de precipitaciones.

Por último, se utilizó streamlit para crear una aplicación con la que ejecutar los modelos seleccionados y comprobar su rendimiento. 


---

This project is based on the prediction of rainfall in Australia from a dataset containing climatic data for the last ten years.

For the development of the project we used the scikit-learn library for data pre-processing, model implementation and metric evaluation and TensorFlow for neural network training.

There were performed classification models to determine whether or not it will rain the next day and regression models to determine the amount of rainfall.

Finally, streamlit was used to build an app to run the selected models to test their performance.


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
